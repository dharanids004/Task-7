# image_resizer.py
# Simple batch image resizer & converter using Pillow.
# Usage:
#   python image_resizer.py -i input_images -o output_images --width 800 --height 800 --format PNG --keep-aspect
import os
from PIL import Image
import argparse

def main():
    parser = argparse.ArgumentParser(description='Batch resize and convert images.')
    parser.add_argument('-i','--input', default='input_images', help='Input folder with images')
    parser.add_argument('-o','--output', default='output_images', help='Output folder (will be created)')
    parser.add_argument('--width', type=int, default=800, help='Target width in pixels')
    parser.add_argument('--height', type=int, default=800, help='Target height in pixels')
    parser.add_argument('--format', default='PNG', help='Output format (PNG, JPEG, WEBP, etc.)')
    parser.add_argument('--keep-aspect', action='store_true', help='Maintain aspect ratio using thumbnail (no distortion)')
    args = parser.parse_args()

    os.makedirs(args.output, exist_ok=True)
    supported = ('.png','.jpg','.jpeg','.bmp','.gif','.webp',' .tiff')
    for fname in os.listdir(args.input):
        if not fname.lower().endswith(('.png','.jpg','.jpeg','.bmp','.gif','.webp','.tiff')):
            continue
        inpath = os.path.join(args.input, fname)
        try:
            img = Image.open(inpath)
        except Exception as e:
            print(f"Failed to open {inpath}: {e}")
            continue

        if args.keep_aspect:
            img.thumbnail((args.width, args.height), Image.LANCZOS)
        else:
            img = img.resize((args.width, args.height), Image.LANCZOS)

        base = os.path.splitext(fname)[0]
        out_ext = args.format.lower().lstrip('.')
        outname = f"{base}.{out_ext}"
        outpath = os.path.join(args.output, outname)

        # Convert to RGB for formats that do not support transparency if needed
        save_img = img
        if args.format.upper() in ('JPEG','JPG') and img.mode in ('RGBA','LA'):
            save_img = img.convert('RGB')

        try:
            save_img.save(outpath, args.format.upper())
            print(f"Saved: {outpath}")
        except Exception as e:
            print(f"Failed to save {outpath}: {e}")

if __name__ == '__main__':
    main()
