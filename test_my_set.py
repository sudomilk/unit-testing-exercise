import pytest
from my_set import MySet

def test_add_to_set():
    item = 'foo'
    my_set = MySet()
    my_set.add(item)
    assert my_set.items == ['foo']

def test_no_duplicates():
    item = 'foo'
    my_set = MySet()
    my_set.add(item)
    my_set.add(item)
    assert my_set.items == ['foo']

def test_remove_items():
    item = 'foo'
    my_set = MySet()
    my_set.add(item)
    my_set.remove(item)
    assert my_set.items == []
