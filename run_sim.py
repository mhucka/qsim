import sys
sys.path.insert(0, '.')

import cirq
import qsimcirq
from qsimcirq.qsim_circuit import QSimCircuit

qsim_simulator = qsimcirq.QSimSimulator()

circuit = cirq.Circuit()

print("Running compute_amplitudes on empty circuit with empty bitstrings")
try:
    print(qsim_simulator.compute_amplitudes(circuit, bitstrings=[]))
except Exception as e:
    print(f"Exception: {e}")
