from collections import namedtuple

from storyruntime.utils.TypeUtils import TypeUtils


def test_isnamedtuple():
    namedtuple_obj = namedtuple(
        'NamedTupleObj',
        ['key']
    )

    assert TypeUtils.isnamedtuple(namedtuple_obj(
        key='key'
    )) is True
    assert TypeUtils.isnamedtuple(namedtuple_obj) is False
    assert TypeUtils.isnamedtuple(('a', 'b', 'c')) is False
    assert TypeUtils.isnamedtuple({}) is False
    assert TypeUtils.isnamedtuple(1) is False
    assert TypeUtils.isnamedtuple('a') is False
    assert TypeUtils.isnamedtuple(False) is False
