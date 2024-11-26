import numpy as np
import soundfile as sf
from scipy.fftpack import dct, idct

def comprimir_audio_con_dct(audio_data, umbral=0.01):
    """
    Comprime el audio utilizando la DCT y eliminando coeficientes de baja magnitud.
    
    :param audio_data: Datos de audio (array de NumPy).
    :param umbral: Umbral para eliminar coeficientes de baja magnitud (entre 0 y 1).
    :return: Audio comprimido.
    """
    # Aplicar la DCT al audio
    dct_data = dct(audio_data, type=2, norm='ortho')
    
    # Establecer el umbral para eliminar coeficientes pequeños
    max_val = np.max(np.abs(dct_data))  # El valor máximo en el conjunto de coeficientes DCT
    dct_data[np.abs(dct_data) < umbral * max_val] = 0  # Eliminar coeficientes de baja magnitud
    
    # Realizar la IDCT (transformada inversa) para reconstruir el audio comprimido
    audio_comprimido = idct(dct_data, type=2, norm='ortho')
    
    return audio_comprimido

# Cargar el archivo de audio
audio_file = 'Recursos/In_Piano.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Comprimir el audio utilizando la DCT
audio_comprimido = comprimir_audio_con_dct(audio_data, umbral=0.01)

# Asegúrate de que los valores estén dentro del rango permitido por el formato WAV
audio_comprimido = np.clip(audio_comprimido, -1.0, 1.0)

# Guardar el archivo de audio comprimido
output_file = 'Recursos/In_Piano_comprimido.wav'
sf.write(output_file, audio_comprimido, sample_rate)

print(f"El archivo de audio comprimido ha sido guardado como {output_file}")
