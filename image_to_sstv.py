from pysstv.color import MartinM1
from PIL import Image

def image_to_sstv(image_path, output_path):
    image = Image.open(image_path).convert("RGB")
    resized = image.resize((320, 256))
    sstv = MartinM1(resized, 8000, 16)
    sstv.write_wav(output_path)

image_path = 'descarga.png'
output_path = 'salida_martin.wav'

image_to_sstv(image_path, output_path)
