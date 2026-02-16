#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`apqueue` module

:author: `FIL - Faculté des Sciences et Technologies -
          Univ. Lille <http://portail.fil.univ-lille1.fr>`_

:date: 2015, september
:last revision: 2024, March

A module for queue data structure.

:Provides:

* class ApQueue

and methods

* `enqueue`
* `dequeue`
* `is_empty`
"""
from typing import TypeVar
T = TypeVar('T')

class ApQueueEmptyError(Exception):
    """
    Exception for empty stacks
    """
    def __init__(self, msg):
        self.message = msg


class ApQueue():
    """
    $$$ ap_queue = ApQueue()
    $$$ ap_queue.is_empty()
    True
    $$$ ap_queue.enqueue(1)
    $$$ ap_queue.is_empty()
    False
    $$$ ap_queue.enqueue(2)
    $$$ str(ap_queue)
    '→2|1→'
    $$$ ap_queue.dequeue()
    1
    $$$ ap_queue.dequeue()
    2
    $$$ ap_queue.is_empty()
    True
    $$e ap_queue.dequeue()
    ApQueueEmptyError
    """
    ARROW = chr(0x2192)

    def __init__(self):
        """
        build  a new empty queue
        precondition: none
        """
        self.__content = []

    def enqueue(self, elt: T):
        """
        insert an element at the begining of the queue
        precondition: none
        """
        self.__content.insert(0, elt)

    def dequeue(self) -> T:
        """
        return the element on top of self
        Side effect: self contains an element less
        precondition: self must be non empty
        """
        if len(self.__content) > 0:
            res = self.__content.pop()
        else:
            raise ApQueueEmptyError('empty queue, nothing to dequeue')
        return res

    def is_empty(self) -> bool:
        """
        return:
          * ``True`` if s is empty
          * ``False`` otherwise
        precondition: none
        """
        return self.__content == []

    def __str__(self) -> str:
        """
        return the string representation of this queue.
        """
        return ApQueue.ARROW + \
            "|".join(str(el) for el in self.__content) + \
            ApQueue.ARROW

    def __len__(self) -> int:
        """
        return the length of this queue
        """
        return len(self.__content)

if __name__ == '__main__':
    import apl1test
    apl1test.testmod('apqueue.py')
