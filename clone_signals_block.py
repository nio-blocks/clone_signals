from nio.block.base import Block
from nio.signal.base import Signal
from nio.util.discovery import discoverable
from copy import deepcopy


@discoverable
class CloneSignals(Block):
    """ Clone Signals block.

    Performs a deepcopy on signals.

    """

    def process_signals(self, signals):
        """ Overridden from the block interface.

        """
        fresh_signals = []

        for signal in signals:
           fresh_signals.append(deepcopy(signal))

        self.notify_signals(fresh_signals)
