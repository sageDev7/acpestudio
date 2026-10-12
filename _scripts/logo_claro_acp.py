"""Versión clara del logo de ACP repartiendo el color por "rojez" y no por distancia al negro.
En el JPG original el bordó tiene zonas muy oscuras (casi negras) y bordes con ruido: por distancia
de color quedaban manchas marfil dentro del rojo. Acá cada píxel se mezcla entre marfil y bordó
según cuánto domina el rojo sobre el verde/azul, con una transición suave para los bordes."""
import os
import numpy as np
from PIL import Image, ImageFilter
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IVORY = np.array([0xF3, 0xED, 0xE3], float)
BORDO = np.array([0xA8, 0x3A, 0x33], float)   # un punto más claro que #93312C para que se lea sobre fondo oscuro

def claro(src, dst):
    im = np.array(Image.open(os.path.join(D, src)).convert("RGBA")).astype(float)
    rgb, a = im[..., :3], im[..., 3]
    red = rgb[..., 0] - np.maximum(rgb[..., 1], rgb[..., 2])          # cuánto domina el rojo
    w = ((red - 18) / 40).clip(0, 1)
    # suavizar el peso para que el ruido del JPG no deje motas sueltas
    wi = Image.fromarray((w * 255).astype(np.uint8)).filter(ImageFilter.MedianFilter(5)).filter(ImageFilter.GaussianBlur(0.8))
    w = np.array(wi).astype(float)[..., None] / 255
    out = IVORY * (1 - w) + BORDO * w
    Image.fromarray(np.dstack([out, a]).clip(0, 255).astype(np.uint8), "RGBA").save(os.path.join(D, dst))
    print("ok", dst)

claro("logo.png", "logo-claro.png")
claro("isotipo.png", "isotipo-claro.png")
