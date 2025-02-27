import numpy as np
from gnuradio import gr

class blk (gr. sync_block ):

    def __init__ ( self ) : # only default arguments here
        gr. sync_block . __init__ (
            self ,
            name ='e_Acum',#ill show up in GRC
            in_sig =[ np. float32 ],
            out_sig =[ np. float32 ]
    )
    def work (self , input_items , output_items ):
        x = input_items [0] # Senial de entrada .
        y0 = output_items [0] # Promedio de la senial
    
        y0 [:]= np. cumsum (x)
        

        return len (y)