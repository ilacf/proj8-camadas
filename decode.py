#Importe todas as bibliotecas
import suaBibSignal as sbs
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import time
import soundfile
from scipy import signal
from scipy.fftpack import fft

audio_modulado, samplerate = soundfile.read('modulado.wav')
print("oi", max(audio_modulado), min(audio_modulado))

calculo_fourier = sbs.signalMeu()
frequencias, amplitudes = calculo_fourier.calcFFT(audio_modulado, samplerate)

print("oi", max(frequencias), min(frequencias))

if max(frequencias) < 18000 and min(frequencias) > 10000:
    print("Confirmado que o sinal esta entre 10kHz e 18kHz")

# demodular audio
audio_duration = len(audio_modulado)/samplerate
t = np.linspace(0, audio_duration, len(audio_modulado), endpoint=False)

w = 2 * np.pi * 14000
portadora = 1 * np.sin(w*t)

audio_demodulado = audio_modulado / portadora

# filtrar frequencias
nyq_rate = samplerate/2
width = 5.0/nyq_rate
ripple_db = 60.0 #dB
N , beta = signal.kaiserord(ripple_db, width)
cutoff_hz = 4000.0
taps = signal.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))

audio_filtrado = signal.lfilter(taps, 1.0, audio_demodulado)
sd.play(audio_filtrado)
time.sleep(5)

# grafico 5
plt.plot(t, audio_demodulado)
plt.xlabel("tempo")
plt.ylabel("sinal de audio demodulado")
plt.show()

# grafico 6
calculo_fourier.plotFFT(audio_demodulado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio demodulado")
plt.show()

# grafico 7
calculo_fourier.plotFFT(audio_filtrado, samplerate)
plt.xlabel("frequencia")
plt.ylabel("sinal de audio demodulado e filtrado")
plt.show()