from djhl.core.apps import CoreConfig


def test_core():
    assert CoreConfig.name == "core"
