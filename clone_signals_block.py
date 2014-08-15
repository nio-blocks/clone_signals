from nio.common.block.base import Block
from nio.common.signal.base import Signal
from nio.common.discovery import Discoverable, DiscoverableType
from copy import deepcopy


@Discoverable(DiscoverableType.block)
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
