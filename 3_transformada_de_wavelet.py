import numpy as np
import soundfile as sf
import pywt
import matplotlib.pyplot as plt

def comprimir_audio_wavelet(audio_data, wavelet='haar', nivel=7, umbral=0.01):
    """
    Comprime el audio utilizando la DWT, eliminando coeficientes pequeños.
    
    :param audio_data: Datos de audio (array de NumPy).
    :param wavelet: Tipo de wavelet a usar ('haar', 'db1', 'sym2', etc.).
    :param nivel: Nivel de descomposición.
    :param umbral: Porcentaje del valor máximo para eliminar coeficientes pequeños.
    :return: Audio comprimido y coeficientes modificados.
    """
    # Aplicar la DWT al audio
    coeffs = pywt.wavedec(audio_data, wavelet, level=nivel)
    
    # Filtrar coeficientes pequeños
    coeffs_filtrados = [
        np.where(np.abs(c) < umbral * np.max(np.abs(c)), 0, c) for c in coeffs
    ]
    
    # Reconstruir el audio comprimido usando la IDWT
    audio_comprimido = pywt.waverec(coeffs_filtrados, wavelet)
    
    return audio_comprimido, coeffs_filtrados

def graficar_coefs_wavelet(coeffs, nivel):
    """
    Grafica los coeficientes de la DWT (originales o filtrados).
    """
    fig, axes = plt.subplots(len(coeffs), 1, figsize=(10, 8))
    fig.suptitle('Coeficientes de la Transformada Wavelet (Filtrados)', fontsize=16)
    
    for i, coef in enumerate(coeffs):
        if i == 0:
            title = "Aproximación (Nivel {})".format(nivel)
        else:
            title = "Detalle (Nivel {})".format(nivel - i + 1)
        axes[i].plot(coef, color='blue')
        axes[i].set_title(title, fontsize=10)
        axes[i].set_xlim(0, len(coef))
        axes[i].tick_params(axis='x', which='both', bottom=False, labelbottom=False)
    
    plt.tight_layout()
    plt.subplots_adjust(top=0.9)
    plt.show()

# Cargar el archivo de audio
audio_file = 'Recursos/In_Piano.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Comprimir el audio utilizando la DWT
wavelet = 'haar'
nivel = 7
umbral = 0.1  # Ajusta este valor para mayor o menor compresión
audio_comprimido, coeffs_filtrados = comprimir_audio_wavelet(audio_data, wavelet, nivel, umbral)

# Asegúrate de que los valores estén dentro del rango permitido por el formato WAV
audio_comprimido = np.clip(audio_comprimido, -1.0, 1.0)

# Guardar el audio comprimido
output_file = 'Recursos/In_Piano_comprimido.wav'
sf.write(output_file, audio_comprimido, sample_rate)

print(f"Archivo comprimido guardado como: {output_file}")

# Graficar los coeficientes filtrados
graficar_coefs_wavelet(coeffs_filtrados, nivel)
