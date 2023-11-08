#importe as bibliotecas
import suaBibSignal
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
from math import *
import time
import sys
from scipy.io import wavfile

#funções a serem utilizadas
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        sys.exit(0)

#converte intensidade em Db, caso queiram ...
def todB(s):
    sdB = 10*np.log10(s)
    return(sdB)

samplerate, data = wavfile.read('StarWars3.wav')

