import numpy as np
import soundfile as sf
from scipy.fftpack import dct
import matplotlib.pyplot as plt

# Cargar el archivo de audio
audio_file = 'Recursos/In_Piano.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Aplicar la DCT al audio
dct_data = dct(audio_data, type=2, norm='ortho')

# Normalizar los coeficientes de la DCT en el rango [-1, 1]
dct_normalizado = 2 * (dct_data - np.min(dct_data)) / (np.max(dct_data) - np.min(dct_data)) - 1

# Graficar los coeficientes DCT normalizados
grafica_puntos = 2000  # Número máximo de puntos para graficar (ajústalo según tu necesidad)
dct_indices = np.linspace(0, len(dct_data) - 1, grafica_puntos, dtype=int)

plt.figure(figsize=(10, 5))
plt.stem(dct_indices, dct_normalizado[dct_indices], linefmt='b-', markerfmt='bo', basefmt=" ", label='Coeficientes DCT Normalizados')
plt.title('Coeficientes DCT Normalizados en [-1, 1]')
plt.xlabel('Índice de Frecuencia')
plt.ylabel('Amplitud Normalizada')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
