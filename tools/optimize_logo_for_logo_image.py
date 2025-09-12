from PIL import Image, ImageOps
import os

repo_root = os.path.dirname(os.path.dirname(__file__))
input_name = 'logo-image.png'
output_name = 'logo-image-optimized.jpg'
input_path = os.path.join(repo_root, input_name)
output_path = os.path.join(repo_root, output_name)

W, H = 1200, 630

if not os.path.exists(input_path):
    print('Input file not found:', input_path)
    raise SystemExit(1)

img = Image.open(input_path).convert('RGBA')
# Fit into box keeping aspect
img.thumbnail((W, H), Image.LANCZOS)

# Create solid background and paste centered
background = Image.new('RGBA', (W, H), (255,255,255,255))
img_w, img_h = img.size
pos = ((W - img_w) // 2, (H - img_h) // 2)
background.paste(img, pos, img)

# Convert to RGB and save as JPEG with quality to reduce size
background.convert('RGB').save(output_path, format='JPEG', quality=82, optimize=True)
print('Saved optimized image:', output_path)
print('Size (bytes):', os.path.getsize(output_path))
