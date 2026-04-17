# RPi LCD Image Resizer

A simple Python GUI application to resize images for common Raspberry Pi LCD modules.

## Features
- Presets for common RPi LCD resolutions: 320x240, 480x320, 800x480, 1024x600.
- Multiple resizing modes:
  - **Pad (Fit):** Keeps aspect ratio, adds black borders to fill the target resolution.
  - **Crop (Fill):** Keeps aspect ratio, scales to the larger dimension, and crops excess.
  - **Stretch:** Ignores aspect ratio, stretches the image to the target resolution.

## Installation

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

## GitHub Push Instructions

If you want to push this to your own GitHub repository:
1. Create a new repository on GitHub.
2. Run the following commands:
   ```bash
   git branch -M main
   git remote add origin <YOUR_GITHUB_REPO_URL>
   git push -u origin main
   ```