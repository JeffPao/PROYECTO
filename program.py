"""
Librerías necesarias
    1. matplotlib
    2. scipy
    3. 
"""
from pathlib import Path  # Para directorios flexibles
import scipy.io.wavfile as wav  # Para cargar archivos de audio .wav
import matplotlib.pyplot as plt  # Comandos de matplotlib
import numpy as np  # Para las gráficas

# ====== CARGAR AUDIO Y VERIFICAR QUE EL ARCHIVO EXISTA ======
carpeta_principal = Path('Recursos')
nombre_archivo = 'Ma_Originals_Heartbeatwithreverb_200.wav'
ruta_archivo = carpeta_principal / nombre_archivo

if ruta_archivo.exists():
    # Cargar el archivo de audio
    frecuencia_muestreo, datos_audio = wav.read(ruta_archivo)
    print(f'Frecuencia de muestreo: {frecuencia_muestreo} Hz')
    print(f'Tamaño de datos de audio: {datos_audio.shape}')

    # Si los datos son estéreo, tomar solo un canal para trabajar
    if len(datos_audio.shape) > 1:
        datos_audio = datos_audio[:, 0]  # Usar solo el canal izquierdo

    
    # ====== GRÁFICA DE LA SEÑAL ORIGINAL ======
    duracion = len(datos_audio) / frecuencia_muestreo
    tiempo = np.linspace(0., duracion, len(datos_audio))
    plt.figure(figsize=(10, 8))
    plt.plot(tiempo, datos_audio, color='blue')
    plt.ylabel("Amplitud")
    plt.title("Forma de Onda del Audio")
    plt.grid()

    plt.show()
else:
    print("El archivo no existe en la ruta especificada.")
