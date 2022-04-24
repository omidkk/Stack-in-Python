# Stack-in-Python

This project contains a stack implementation. Unit tests for the function are provided.

#### Technologies
- python 3

#### Prerequisites
- Install packages defined in requirements.txt

#### Usage

Install the package, and add following to the your code.

```
    from src.stack import Stack
```


#### Test
```sh
$ pytest test/test_stack.py
```

#### Content

Currently includes:
- Pop: Returns last element of stack, and removes it from stack.
- Push: Adds new item to the stack.
- Peek: Returns last element of stack, without removing.
- Size: Returns number of items in the list.
- Empty: Checks whether stack is empty or not