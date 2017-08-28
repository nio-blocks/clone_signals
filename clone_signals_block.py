from nio.block.base import Block
from nio.properties import VersionProperty
from copy import deepcopy


class CloneSignals(Block):
    """ Clone Signals block.

    Performs a deepcopy on signals.

    """
    version = VersionProperty("1.0.0")

    def process_signals(self, signals):
        """ Overridden from the block interface.

        """
        fresh_signals = []

        for signal in signals:
            fresh_signals.append(deepcopy(signal))

        self.notify_signals(fresh_signals)
