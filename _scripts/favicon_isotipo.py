"""Favicon de ACP con el isotipo original (negro + bordó) sobre papel. El ícono del logo mide ~174 px:
se escala con Lanczos en Pillow (más limpio que dejarlo al navegador)."""
import os
from PIL import Image
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
iso = Image.open(os.path.join(D, "isotipo.png")).convert("RGBA")
W = 450
iso = iso.resize((W, round(iso.height * W / iso.width)), Image.LANCZOS)
fav = Image.new("RGBA", (512, 512), (0xF3, 0xED, 0xE3, 255))
fav.alpha_composite(iso, ((512 - iso.width) // 2, (512 - iso.height) // 2))
fav.convert("RGB").save(os.path.join(D, "favicon.png"))
print("ok favicon.png", iso.size)
