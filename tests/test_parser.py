import pytest
from lib.extractor import Extractor


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


def test_extract_ramp_time(extractor):
    assert extractor.ramp_time == 60
