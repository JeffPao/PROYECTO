import numpy as np  
import soundfile as sf
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt

def aplicar_dct(audio_data):
    """
    Aplica la Transformada Discreta del Coseno (DCT) a los datos de audio.
    
    :param audio_data: Datos de audio (array de NumPy).
    :return: Coeficientes DCT.
    """
    return dct(audio_data, type=2, norm='ortho')

def comprimir_audio_con_dct(audio_data, umbral=0.01):
    """
    Comprime el audio utilizando la DCT y eliminando coeficientes de baja magnitud.
    
    :param audio_data: Datos de audio (array de NumPy).
    :param umbral: Umbral para eliminar coeficientes de baja magnitud (entre 0 y 1).
    :return: Audio comprimido y coeficientes DCT filtrados.
    """
    # Aplicar la DCT al audio
    dct_data = aplicar_dct(audio_data)
    
    # Establecer el umbral para eliminar coeficientes pequeños
    max_val = np.max(np.abs(dct_data))  # Valor máximo en los coeficientes DCT
    dct_filtered = np.where(np.abs(dct_data) > umbral * max_val, dct_data, 0)
    
    # Realizar la IDCT para reconstruir el audio comprimido
    audio_comprimido = idct(dct_filtered, type=2, norm='ortho')
    
    return audio_comprimido, dct_data, dct_filtered






# Cargar el archivo de audio
audio_file = 'Recursos/In_Piano.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Calcular los coeficientes DCT
dct_data = aplicar_dct(audio_data)

# Comprimir el audio utilizando la DCT
audio_comprimido, dct_data, dct_filtered = comprimir_audio_con_dct(audio_data, umbral=0.001)

# Asegúrate de que los valores estén dentro del rango permitido por el formato WAV
audio_comprimido = np.clip(audio_comprimido, -1.0, 1.0)

# Guardar el archivo de audio comprimido
output_file = 'Recursos/In_Piano_comprimido.wav'
sf.write(output_file, audio_comprimido, sample_rate)




# Parámetro para reducir puntos en la gráfica (submuestreo)
grafica_puntos = 2000  # Número de puntos máximo para graficar (ajústalo según tu necesidad)

# Crear índices de submuestreo para graficar
dct_indices = np.linspace(0, len(dct_data) - 1, grafica_puntos, dtype=int)

# Graficar los coeficientes DCT
plt.figure(figsize=(10, 6))
plt.stem(dct_indices, dct_data[dct_indices], linefmt='b-', markerfmt='bo', basefmt=" ", label='Coeficientes DCT')
plt.title('Coeficientes DCT (Dominio de la Frecuencia)')
plt.xlabel('Índice de Frecuencia')
plt.ylabel('Amplitud')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
