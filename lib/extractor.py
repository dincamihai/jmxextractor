from lxml import etree


class Extractor(object):

    XPATHS=dict(
        TEST_PLAN_NAME="hashTree/TestPlan",
        NUM_THREADS="hashTree/hashTree/ThreadGroup/stringProp[@name='ThreadGroup.num_threads']",
        RAMP_TIME="hashTree/hashTree/ThreadGroup/stringProp[@name='ThreadGroup.ramp_time']",
        DOMAIN="hashTree/hashTree/hashTree/ConfigTestElement/stringProp[@name='HTTPSampler.domain']",
        CONCURENT_POOL="hashTree/hashTree/hashTree/ConfigTestElement/stringProp[@name='HTTPSampler.concurrentPool']",
        URLS="hashTree/hashTree/hashTree/hashTree/HTTPSamplerProxy",
    )

    def __init__(self, jmx_path):
        with open('tests/sample.jmx', 'rb') as jmx:
            self.tree = etree.parse(jmx)
            self.root = self.tree.getroot()

    @property
    def test_plan_name(self):
        return self.root.find(self.XPATHS['TEST_PLAN_NAME']).get('testname')

    @property
    def num_threads(self):
        return int(self.root.find(self.XPATHS['NUM_THREADS']).text)

    @property
    def ramp_time(self):
        return int(self.root.find(self.XPATHS['RAMP_TIME']).text)

    @property
    def domain(self):
        return self.root.find(self.XPATHS['DOMAIN']).text

    @property
    def concurrent_pool(self):
        return int(self.root.find(self.XPATHS['CONCURENT_POOL']).text)

    @property
    def urls(self):
        urls = []
        for node in self.root.findall(self.XPATHS['URLS']):
            urls.append(
                dict(
                    path=node.find("./stringProp[@name='HTTPSampler.path']").text,
                    method=node.find("./stringProp[@name='HTTPSampler.method']").text
                )
            )
        return urls
