from pydub import AudioSegment
import os

def convertir_mp3_a_wav(ruta_mp3):
    # Verificar que el archivo exista
    if not os.path.exists(ruta_mp3):
        print("El archivo MP3 no existe.")
        return None
    
    # Ruta para el archivo WAV de salida
    ruta_salida = os.path.splitext(ruta_mp3)[0] + "_convertido.wav"
    
    # Convertir de MP3 a WAV
    try:
        audio = AudioSegment.from_mp3(ruta_mp3)
        audio.export(ruta_salida, format="wav")
        print(f"Archivo convertido a WAV: {ruta_salida}")
        return ruta_salida
    except Exception as e:
        print(f"Error al convertir MP3 a WAV: {e}")
        return None

# Ruta del archivo MP3
archivo_mp3 = "C:/Users/jjrod/Documents/DSP/PROYECTO/Recursos/Audio_DCT_20241126_071635_Reducido_20241126_071701.mp3"

# Convertir el archivo
convertir_mp3_a_wav(archivo_mp3)
