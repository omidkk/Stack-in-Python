from src.custom_exceptions.empty_stack import EmptyStackException


class Stack:
    """
    This class implements the stack data structure, and its functionalities
    """

    def __init__(self):
        self.stack = []

    def pop(self):
        """
        Return last element of stack and remove it from stack
        :return: last item
        """
        if self.stack:
            return self.stack.pop()
        raise EmptyStackException("EmptyStackException")

    def push(self, item):
        """
        appends the item to the end of stack
        :param item: element to insert
        :return: None
        """
        self.stack.append(item)

    def peek(self):
        """
        Retruns the last element, without removing from the stack
        :return:
        """
        if self.stack:
            return self.stack[-1]
        raise EmptyStackException("EmptyStackException")

    def size(self) -> int:
        """
        Returns the size of stack
        :return: integer
        """
        return len(self.stack)

    def empty(self) -> bool:
        """
        Checks whether stack is empty or not
        :return: boolean
        """
        is_empty = True
        if self.stack:
            is_empty = False
        return is_empty
