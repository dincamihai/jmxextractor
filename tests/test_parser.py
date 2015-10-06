import pytest
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


@pytest.fixture
def root():
    with open('tests/sample.jmx', 'rb') as jmx:
        tree = etree.parse(jmx)
        return tree.getroot()


@pytest.fixture
def extractor():
    return Extractor('tests/sample.jmx')


def test_extract_test_plan_name(extractor):
    assert extractor.testplanname == 'My test plan'


def test_extract_num_threads(extractor):
    assert extractor.num_threads == 50
