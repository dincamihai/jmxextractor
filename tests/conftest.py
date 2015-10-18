import pytest
import json
import os


@pytest.fixture
def single_argument_config():
    return [
        {
            "path": "stringProp[@name='Argument.name']",
            "key": 'name',
            "source": {'type': 'text'}
        },
        {
            "path": "stringProp[@name='Argument.value']",
            "key": 'value',
            "source": {'type': 'text'}
        }
    ]


@pytest.fixture
def arguments_config(single_argument_config):
    return [
        {
            "path": "elementProp[@name='HTTPsampler.Arguments']/collectionProp/elementProp",
            "key": "arguments",
            "many": True,
            "config": single_argument_config
        }
    ]


@pytest.fixture
def single_target_config(single_argument_config):
    return [
        {
            "path": "stringProp[@name='HTTPSampler.path']",
            "key": "path",
            "source": {'type': 'text'}
        },
        {
            "path": "stringProp[@name='HTTPSampler.method']",
            "key": 'method',
            "source": {'type': 'text'}
        },
        {
            "path": "elementProp[@name='HTTPsampler.Arguments']/collectionProp/elementProp",
            "key": "arguments",
            "many": True,
            "config": single_argument_config
        }
    ]


@pytest.fixture
def targets_config(single_target_config):
    return [
        {
            "path": "hashTree/hashTree/hashTree/hashTree/HTTPSamplerProxy",
            "key": "targets",
            "many": True,
            "config": single_target_config
        }
    ]


@pytest.fixture
def config(single_target_config):
    return [
        dict(
            path="hashTree/TestPlan",
            key='test_plan_name',
            source={'type': 'attribute', 'attribute_name': 'testname'}
        ),
        dict(
            path="hashTree/hashTree/ThreadGroup/stringProp[@name='ThreadGroup.num_threads']",
            key='num_threads',
            source={'type': 'text', 'cast': 'int'}
        ),
        dict(
            path="hashTree/hashTree/ThreadGroup/stringProp[@name='ThreadGroup.ramp_time']",
            key='ramp_time',
            source={'type': 'text', 'cast': 'int'}
        ),
        dict(
            path="hashTree/hashTree/hashTree/ConfigTestElement/stringProp[@name='HTTPSampler.domain']",
            key='domain',
            source={'type': 'text'}
        ),
        dict(
            path="hashTree/hashTree/hashTree/ConfigTestElement/stringProp[@name='HTTPSampler.concurrentPool']",
            key='concurrent_pool',
            source={'type': 'text', 'cast': 'int'}
        ),
        {
            "path": "hashTree/hashTree/hashTree/hashTree/HTTPSamplerProxy",
            "key": "targets",
            "many": True,
            "config": single_target_config
        }
    ]


@pytest.fixture
def config_mapping(config):
    return dict(zip(
        [
            'test_plan_name_config',
            'num_threads_config',
            'ramp_time_config',
            'domain_config',
            'concurrent_pool_config',
            'targets_config'
        ],
        [[it] for it in config]
    ))
