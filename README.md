# Image Resizer - Sample Package

This package contains:
- `input_images/` : 8 sample images (various sizes & formats).
- `output_images/` : empty folder where resized images will be saved.
- `image_resizer.py` : a Python script (uses Pillow) to batch resize & convert.
- `README.md` : this file.

## Quick Steps (Windows / macOS / Linux)

1. Download and unzip the file `image_resizer_samples.zip`.
2. Open a terminal (or Command Prompt / PowerShell) and `cd` into the unzipped folder.
3. (Optional) Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate    # Windows (PowerShell)
   ```
4. Install Pillow:
   ```bash
   pip install pillow
   ```
5. Run the resizer (example — resizes to 800x800 and converts to PNG, preserving aspect ratio):
   ```bash
   python image_resizer.py -i input_images -o output_images --width 800 --height 800 --format PNG --keep-aspect
   ```
   Or to force exact size (may distort aspect ratio):
   ```bash
   python image_resizer.py -i input_images -o output_images --width 800 --height 800 --format JPEG
   ```
6. Check `output_images/` for the results.

## Notes
- Use `--keep-aspect` to preserve aspect ratio (uses thumbnail).
- Supported output formats depend on your Pillow build (PNG and JPEG are always supported).
- If you want to process only certain files, move them into `input_images/` or edit the script.

## Troubleshooting
- If saving to WEBP/JPEG fails, ensure your Pillow supports that format.
- If text on sample images looks small, open the images and view at larger zoom.

Enjoy! If you want me to:
- Add drag-and-drop support,
- Make a GUI (Tkinter) version,
- Create a GitHub-ready repo and commit/push,
say which one and I'll prepare it.
