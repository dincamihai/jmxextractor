from lxml import etree


class Extractor(object):

    TEST_PLAN_NAME=dict(
        xpath='hashTree/TestPlan',
        attribute='testname'
    )

    NUM_THREADS=dict(
        xpath="hashTree/hashTree/ThreadGroup/stringProp[@name='ThreadGroup.num_threads']",
    )

    def __init__(self, jmx_path):
        with open('tests/sample.jmx', 'rb') as jmx:
            self.tree = etree.parse(jmx)
            self.root = self.tree.getroot()

    @property
    def testplanname(self):
        xpath, attribute = self.TEST_PLAN_NAME.values()
        return self.root.find(xpath).get(attribute)

    @property
    def num_threads(self):
        return int(self.root.find(self.NUM_THREADS['xpath']).text)
