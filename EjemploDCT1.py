import numpy as np
import soundfile as sf
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt

def aplicar_umbral_frecuencia(audio_data, frecuencia_de_corte, frecuencia_de_muestreo):
    """
    Aplica un umbral en Hz sobre la DCT del audio, eliminando coeficientes correspondientes a frecuencias altas.
    
    :param audio_data: Datos de audio (array de NumPy).
    :param frecuencia_de_corte: Frecuencia de corte en Hz.
    :param frecuencia_de_muestreo: Frecuencia de muestreo en Hz.
    :return: Audio filtrado usando el umbral en frecuencia.
    """
    # Realizar la DCT sobre la señal de audio
    dct_data = dct(audio_data, type=2, norm='ortho')
    
    # Calcular el índice de la DCT que corresponde a la frecuencia de corte
    N = len(audio_data)
    indice_corte = int(frecuencia_de_corte * N / frecuencia_de_muestreo)
    
    # Filtrar los coeficientes DCT mayores que el índice de corte
    dct_data[indice_corte:] = 0  # Eliminar coeficientes de alta frecuencia
    
    # Realizar la IDCT para reconstruir la señal filtrada
    audio_filtrado = idct(dct_data, type=2, norm='ortho')
    
    return audio_filtrado, dct_data

# Cargar el archivo de audio
audio_file = 'Recursos/Prueba de audio 2.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Definir la frecuencia de corte y la frecuencia de muestreo
frecuencia_de_corte = 500  # Por ejemplo, cortar a 500 Hz
frecuencia_de_muestreo = sample_rate  # Frecuencia de muestreo de la señal de audio

# Aplicar el umbral de frecuencia en la DCT
audio_filtrado, dct_data = aplicar_umbral_frecuencia(audio_data, frecuencia_de_corte, frecuencia_de_muestreo)

# Asegúrate de que los valores estén dentro del rango permitido por el formato WAV
audio_filtrado = np.clip(audio_filtrado, -1.0, 1.0)

# Guardar el archivo de audio filtrado
output_file = 'Recursos/Prueba de audio 2_filtrado.wav'
sf.write(output_file, audio_filtrado, sample_rate)

# Graficar los resultados
time = np.linspace(0, len(audio_data) / sample_rate, num=len(audio_data))
plt.figure(figsize=(15, 10))

# Señal original
plt.subplot(3, 1, 1)
plt.plot(time, audio_data, label='Señal Original')
plt.title('Señal Original (Dominio del Tiempo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

# Coeficientes DCT (originales)
plt.subplot(3, 1, 2)
plt.stem(dct_data, use_line_collection=True)
plt.title('Coeficientes DCT (Dominio de la Frecuencia)')
plt.xlabel('Índice de Frecuencia')
plt.ylabel('Amplitud')
plt.grid(True)

# Señal filtrada
plt.subplot(3, 1, 3)
plt.plot(time, audio_filtrado, label='Señal Filtrada', color='orange')
plt.title('Señal Filtrada (Dominio del Tiempo)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

print(f"El archivo de audio filtrado ha sido guardado como {output_file}")
