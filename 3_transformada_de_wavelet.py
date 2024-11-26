import numpy as np
import soundfile as sf
import pywt
import matplotlib.pyplot as plt

# Cargar el archivo de audio
audio_file = 'Recursos/Prueba de audio 2.wav'
audio_data, sample_rate = sf.read(audio_file)

# Si el archivo tiene más de un canal (estéreo), procesamos solo el primer canal
if len(audio_data.shape) > 1:
    audio_data = audio_data[:, 0]

# Comprimir el audio utilizando la DWT
wavelet = 'haar'
nivel = 7
umbral = 0.3  # Ajusta este valor para mayor o menor compresión
coeffs = pywt.wavedec(audio_data, wavelet)

# Filtrar coeficientes pequeños
coeffs_filtrados = [
    np.where(np.abs(c) < umbral * np.max(np.abs(c)), 0, c) for c in coeffs
]

# Reconstruir el audio comprimido usando la IDWT
audio_comprimido = pywt.waverec(coeffs_filtrados, wavelet)

# Asegúrate de que los valores estén dentro del rango permitido por el formato WAV
audio_comprimido = np.clip(audio_comprimido, -1.0, 1.0)

# Guardar el audio comprimido
output_file = 'Recursos/Prueba de audio 2_____comprai.wav'
sf.write(output_file, audio_comprimido, sample_rate)

print(f"Archivo comprimido guardado como: {output_file}")

# Graficar los coeficientes filtrados
fig, axes = plt.subplots(len(coeffs_filtrados), 1, figsize=(10, 8))
fig.suptitle('Coeficientes de la Transformada Wavelet (Filtrados)', fontsize=16)

for i, coef in enumerate(coeffs_filtrados):
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
