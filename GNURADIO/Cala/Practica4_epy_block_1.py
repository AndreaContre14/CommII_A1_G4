"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from scipy.signal import welch
from gnuradio import gr

class psd_mpsk(gr.sync_block):
    """
    Bloque que calcula la PSD de una señal M-PSK usando Welch
    """
    def __init__(self, samp_rate=1e6, nfft=1024, avg='mean'):
        gr.sync_block.__init__(self,
            name="psd_mpsk",
            in_sig=[np.complex64],
            out_sig=[np.float32])  # PSD es real

        self.samp_rate = samp_rate
        self.nfft = 1024
        self.avg = 'mean'
        self.window = 'hamming'

    def work(self, input_items, output_items):
        in0 = input_items[0]

        # Calcular PSD
        f, Pxx = welch(in0, fs=self.samp_rate, window=self.window, nperseg=self.nfft)

        # Normalizar y entregar una sola vez por ejecución
        Pxx_dB = 10 * np.log10(Pxx + 1e-12)

        # Asegurarse que output_items tenga espacio suficiente
        n_output = min(len(output_items[0]), len(Pxx_dB))
        output_items[0][:n_output] = Pxx_dB[:n_output]

        return n_output
