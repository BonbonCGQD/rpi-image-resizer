# RPi LCD Image Resizer

A simple Python GUI application to resize images for common Raspberry Pi LCD modules.

## Features
- Presets for common RPi LCD resolutions: 320x240, 480x320, 800x480, 1024x600.
- Multiple resizing modes:
  - **Pad (Fit):** Keeps aspect ratio, adds black borders to fill the target resolution.
  - **Crop (Fill):** Keeps aspect ratio, scales to the larger dimension, and crops excess.
  - **Stretch:** Ignores aspect ratio, stretches the image to the target resolution.

## Installation (Note you should have python installed)
link: https://www.python.org/ftp/python/3.13.13/python-3.13.13-amd64.exe

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Select an image file.
3. Choose the target resolution and resize mode.
4. Click "Resize and Save" to choose a destination and save the image.

