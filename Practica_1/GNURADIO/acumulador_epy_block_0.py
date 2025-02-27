
from gnuradio import gr
import numpy as np

class Accumulator(gr.sync_block):
    def __init__(self):
        gr.sync_block.__init__(self,
            name="Accumulator",
            in_sig=[np.float32],
            out_sig=[np.float32])
        # Estado interno para guardar la suma acumulada
        self.cum_sum = 0.0

    def work(self, input_items, output_items):
        in0 = input_items[0]
        out = output_items[0]
        # Acumula cada muestra y asigna la suma a la salida
        for i, sample in enumerate(in0):
            self.cum_sum += sample
            out[i] = self.cum_sum

        # Depuración: imprime algunos valores del bloque
        print("Procesando", len(in0), "muestras | Primer valor:", out[0], 
              "Último valor:", out[-1], "Estado acumulado:", self.cum_sum)
        return len(out)
