from unittest.mock import patch
from ..clone_signals_block import CloneSignals
from nio.util.support.block_test_case import NIOBlockTestCase
from nio.common.signal.base import Signal


class FlavorSignal(Signal):
    def __init__(self, flavor, size=None):
        self.flavor = flavor
        self.size = size
        self._hidden = True


class TestCloneSignals(NIOBlockTestCase):

    def setUp(self):
        super().setUp()
        self.last_notified = []

    def signals_notified(self, signals, output_id='default'):
        self.last_notified = signals

    def test_pass(self):
        signals = [FlavorSignal("banana")]
        attrs = signals[0].__dict__
        blk = CloneSignals()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals(signals)
        # change original signal
        signals[0].flavor = "rotten banana"
        signals[0]._hidden = False
        # and test that the notified signal did not change
        self.assertEqual(self.last_notified[0].flavor, "banana")
        self.assertEqual(self.last_notified[0]._hidden, True)
