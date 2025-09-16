import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  
    """Es un VCO de dos entradas:
    Q: para manipular la fase en radianes,
    A: para manipular la amplitud."""

    def __init__(self):
        gr.sync_block.__init__(
            self,
            name='e_VCO_fase_fc',
            in_sig=[np.float32, np.float32],
            out_sig=[np.complex64]
        )

    def work(self, input_items, output_items):
        Q = input_items[0]
        A = input_items[1]
        Sec = output_items[0]
        Sec[:] = A * np.exp(1.j * Q)
        return len(Sec)
