import sys
from unittest.mock import MagicMock

# Mock out cirq, qsim_decide, and _version
cirq_mock = MagicMock()
numpy_mock = MagicMock()
sys.modules['cirq'] = cirq_mock
sys.modules['numpy'] = numpy_mock
sys.modules['qsimcirq.qsim_decide'] = MagicMock()
sys.modules['qsimcirq._version'] = MagicMock()
sys.modules['qsimcirq._version'].__version__ = "1.0.0"
sys.modules['qsimcirq.qsim_basic'] = MagicMock()
sys.modules['qsimcirq.qsim_avx512'] = MagicMock()

class IdentityGate:
    def num_qubits(self):
        return 1

cirq_mock.IdentityGate = IdentityGate

from qsimcirq.qsim_circuit import TYPE_TRANSLATOR

print("TYPE_TRANSLATOR keys:")
for key in TYPE_TRANSLATOR.keys():
    try:
        print(f" - {key.__name__}")
    except AttributeError:
        pass
