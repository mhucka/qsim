import sys
from unittest.mock import MagicMock

cirq_mock = MagicMock()
numpy_mock = MagicMock()
sys.modules['cirq'] = cirq_mock
sys.modules['numpy'] = numpy_mock

class Gate:
    pass

class IdentityGate(Gate):
    def num_qubits(self):
        return 1

cirq_mock.Gate = Gate
cirq_mock.IdentityGate = IdentityGate
cirq_mock.ControlledGate = type('ControlledGate', (Gate,), {})
cirq_mock.XPowGate = type('XPowGate', (Gate,), {})
cirq_mock.YPowGate = type('YPowGate', (Gate,), {})
cirq_mock.ZPowGate = type('ZPowGate', (Gate,), {})
cirq_mock.HPowGate = type('HPowGate', (Gate,), {})
cirq_mock.CZPowGate = type('CZPowGate', (Gate,), {})
cirq_mock.CXPowGate = type('CXPowGate', (Gate,), {})
cirq_mock.PhasedXPowGate = type('PhasedXPowGate', (Gate,), {})
cirq_mock.PhasedXZGate = type('PhasedXZGate', (Gate,), {})
cirq_mock.XXPowGate = type('XXPowGate', (Gate,), {})
cirq_mock.YYPowGate = type('YYPowGate', (Gate,), {})
cirq_mock.ZZPowGate = type('ZZPowGate', (Gate,), {})
cirq_mock.SwapPowGate = type('SwapPowGate', (Gate,), {})
cirq_mock.ISwapPowGate = type('ISwapPowGate', (Gate,), {})
cirq_mock.PhasedISwapPowGate = type('PhasedISwapPowGate', (Gate,), {})
cirq_mock.FSimGate = type('FSimGate', (Gate,), {})
cirq_mock.TwoQubitDiagonalGate = type('TwoQubitDiagonalGate', (Gate,), {})
cirq_mock.ThreeQubitDiagonalGate = type('ThreeQubitDiagonalGate', (Gate,), {})
cirq_mock.CCZPowGate = type('CCZPowGate', (Gate,), {})
cirq_mock.CCXPowGate = type('CCXPowGate', (Gate,), {})
cirq_mock.CSwapGate = type('CSwapGate', (Gate,), {})
cirq_mock.MatrixGate = type('MatrixGate', (Gate,), {})
cirq_mock.MeasurementGate = type('MeasurementGate', (Gate,), {})

sys.modules['qsimcirq.qsim_decide'] = MagicMock()
sys.modules['qsimcirq._version'] = MagicMock()
sys.modules['qsimcirq._version'].__version__ = "1.0.0"
sys.modules['qsimcirq.qsim_basic'] = MagicMock()
sys.modules['qsimcirq.qsim_avx512'] = MagicMock()

# Avoid importing QSimSimulator, just import qsim_circuit
import qsimcirq.qsim_circuit as qc

print(qc._cirq_gate_kind(IdentityGate()))
