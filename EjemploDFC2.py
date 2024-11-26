import numpy as np
import soundfile as sf
from scipy.fftpack import dct, idct
from scipy.signal import butter
import matplotlib.pyplot as plt

# Parámetros del filtro Butterworth
corte_filtro = 0.05
orden_filtro = 2
amplificar = 1.5

# Cargar el archivo de audio
audio_file = 'Recursos/Prueba de audio 2.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Aplicar la DCT al audio
dct_data = dct(audio_data, type=2, norm='ortho')

# Crear un filtro Butterworth de paso bajo
N = len(dct_data)
freqs = np.fft.fftfreq(N)
freqs = np.abs(freqs) / 0.5  # Normalización respecto a Nyquist
filtro = 1 / (1 + (freqs / corte_filtro) ** (2 * orden_filtro))

# Aplicar el filtro a los coeficientes DCT
dct_filtrada = (dct_data * filtro) * amplificar

# Realizar la IDCT para reconstruir el audio filtrado
audio_filtrado = idct(dct_filtrada, type=2, norm='ortho')

# Asegúrate de que los valores estén dentro del rango permitido por el formato WAV
audio_filtrado = np.clip(audio_filtrado, -1.0, 1.0)

# Guardar el archivo de audio filtrado
output_file = 'Recursos/Prueba de audio 2_filtrado.wav'
sf.write(output_file, audio_filtrado, sample_rate)

# Graficar resultados
grafica_puntos = 2000  # Número máximo de puntos para graficar (ajústalo según tu necesidad)
indices = np.linspace(0, len(audio_data) - 1, grafica_puntos, dtype=int)
time = np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data))

plt.figure(figsize=(15, 10))

# Señal original (submuestreada)
plt.subplot(3, 1, 1)
plt.plot(time[indices], audio_data[indices], label='Señal Original')
plt.title('Señal Original (Dominio del Tiempo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Coeficientes DCT (submuestreados para mejor rendimiento)
dct_indices = np.linspace(0, len(dct_data) - 1, grafica_puntos, dtype=int)
plt.subplot(3, 1, 2)
plt.stem(dct_indices, dct_data[dct_indices], linefmt='b-', markerfmt='bo', basefmt=" ", label='Coeficientes DCT Originales')
plt.stem(dct_indices, dct_filtrada[dct_indices], linefmt='r-', markerfmt='ro', basefmt=" ", label='Coeficientes DCT Filtrados')
plt.title('Coeficientes DCT Filtrados (Dominio de la Frecuencia)')
plt.xlabel('Índice de Frecuencia')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Señal filtrada (submuestreada)
plt.subplot(3, 1, 3)
plt.plot(time[indices], audio_filtrado[indices], label='Señal Filtrada', color='orange')
plt.title('Señal Filtrada (Dominio del Tiempo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print(f"El archivo de audio filtrado ha sido guardado como {output_file}")
