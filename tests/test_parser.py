import pytest
from lxml import etree


XPATHS = dict(
    TEST_PLAN_NAME=dict(
        xpath='hashTree/TestPlan',
        attribute='testname'
    ),
    NUM_THREADS=dict(
        xpath="hashTree/hashTree/ThreadGroup/stringProp[@name='ThreadGroup.num_threads']",
    )
)


@pytest.fixture
def root():
    with open('tests/sample.jmx', 'rb') as jmx:
        tree = etree.parse(jmx)
        return tree.getroot()


def test_extract_test_plan_name(root):
    xpath, attribute = XPATHS['TEST_PLAN_NAME'].values()
    assert root.find(xpath).get(attribute) == 'My test plan'


def test_extract_num_threads(root):
    [xpath] = XPATHS['NUM_THREADS'].values()
    assert int(root.find(xpath).text) == 50
