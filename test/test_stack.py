import random

import pytest

from src.custom_exceptions.empty_stack import EmptyStackException
from src.stack import Stack


@pytest.fixture
def test_input():
    return [5, 10.25, "a", "test"]


def test_push(test_input):
    stack = Stack()
    for item in test_input:
        stack.push(item)


def test_pop(test_input):
    stack = Stack()
    random.shuffle(test_input)
    for item in test_input:
        stack.push(item)
    assert test_input[-1] == stack.pop()
    assert test_input[-2] == stack.pop()
    assert test_input[-3] == stack.pop()
    assert test_input[-4] == stack.pop()
    with pytest.raises(EmptyStackException):
        stack.pop()


def test_peek(test_input):
    stack = Stack()
    with pytest.raises(EmptyStackException):
        stack.peek()
    random.shuffle(test_input)
    for item in test_input:
        stack.push(item)
    assert test_input[-1] == stack.peek()
    assert test_input[-1] == stack.peek()


def test_size(test_input):
    stack = Stack()
    assert stack.size() == 0
    for item in test_input:
        stack.push(item)
    assert stack.size() == 4


def test_empty(test_input):
    stack = Stack()
    assert stack.empty() is True
    for item in test_input:
        stack.push(item)
    assert stack.empty() is False
