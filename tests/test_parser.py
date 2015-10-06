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
    assert extractor.test_plan_name == 'My test plan'


def test_extract_num_threads(extractor):
    assert extractor.num_threads == 50


def test_extract_ramp_time(extractor):
    assert extractor.ramp_time == 60


def test_extract_domain(extractor):
    assert extractor.domain == 'test.loadimpact.com'


def test_extract_concurrent_pool(extractor):
    assert extractor.concurrent_pool == 4


def test_extract_paths(extractor):
    expected = ['/', '/news.php', '/', '/flip_coin.php', '/flip_coin.php']
    assert [url['path'] for url in extractor.urls] == expected
