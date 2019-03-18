from . import test_normal_ghe

def test_test_normal_ghe():
    assert test_normal_ghe.apply("Jane") == "hello Jane"
