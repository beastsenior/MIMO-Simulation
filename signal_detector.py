import numpy as np

class Signal_Detector():

    #martched filter
    def MF(self, H, Rx_sig):
        Tx_sig_hat = np.dot(np.conj(H).T , Rx_sig)
        return Tx_sig_hat