import numpy as np
from gnuradio import gr

class blk(gr.sync_block):
    def __init__(self):
        # Inicializamos el bloque, señal de entrada y salida de tipo float32
        gr.sync_block.__init__(self, name='e_Diff', in_sig=[np.float32], out_sig=[np.float32])
    
    def work(self, input_items, output_items):
        x = input_items[0]  # Señal de entrada
        y0 = output_items[0]  # Señal de salida (diferencia)
        
        # Calculamos la diferencia entre muestras consecutivas
        y0[1:] = np.diff(x)  # La diferencia entre cada par de muestras consecutivas
        y0[0] = 0  # Asignamos 0 al primer valor, ya que no tiene diferencia anterior
        
        return len(output_items[0])  # Debemos devolver el tamaño de la salida