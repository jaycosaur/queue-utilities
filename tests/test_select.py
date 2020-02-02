from queue import Queue

import pytest

from queue_utilities import Select


def queues_for_test():
    return Queue(), Queue()


def test_can_close_select():
    s = Select(*queues_for_test())
    s.stop()
    assert s.is_stopped == True


def test_select_can_switch_on_queues():
    a, b = queues_for_test()
    s = Select(a, b)
    a.put(1)
    b.put(2)
    for (which_q, message) in s:
        if which_q is a:
            assert message == 1
        if which_q is b:
            assert message == 2
            s.stop()
