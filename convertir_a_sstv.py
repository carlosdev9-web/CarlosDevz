from PIL import Image
from pysstv.color import Robot36
import numpy as np
import wave

# Cargar la imagen recibida (debe llamarse "imagen.jpg")
image = Image.open("imagen.jpg")

# Redimensionar para SSTV (320x240)
image = image.resize((320, 240))

# Crear señal SSTV
sstv = Robot36(image, 44100)
audio = sstv.gen_audio()

# Guardar como WAV
with wave.open("sstv.wav", 'w') as f:
    f.setnchannels(1)
    f.setsampwidth(2)
    f.setframerate(44100)
    f.writeframes(np.array(audio).astype(np.int16).tobytes())

print("Listo: sstv.wav generado")
