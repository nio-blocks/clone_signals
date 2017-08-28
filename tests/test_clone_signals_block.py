from nio.block.terminals import DEFAULT_TERMINAL
from nio.testing.block_test_case import NIOBlockTestCase
from nio.signal.base import Signal

from ..clone_signals_block import CloneSignals


class FlavorSignal(Signal):
    def __init__(self, flavor, size=None):
        self.flavor = flavor
        self.size = size
        self._hidden = True


class TestCloneSignals(NIOBlockTestCase):

    def test_pass(self):
        signals = [FlavorSignal("banana")]
        blk = CloneSignals()
        self.configure_block(blk, {})
        blk.start()
        blk.process_signals(signals)
        # change original signal
        signals[0].flavor = "rotten banana"
        signals[0]._hidden = False
        # and test that the notified signal did not change
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0].flavor,
                         "banana")
        self.assertEqual(self.last_notified[DEFAULT_TERMINAL][0]._hidden, True)
