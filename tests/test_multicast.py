from queue import Queue

import pytest

from queue_utilities import Multicast


def queues_for_test():
    return Queue(), Queue()


def test_can_close_select():
    multicast = Multicast(*queues_for_test())
    multicast.stop()
    assert multicast.is_stopped == True
