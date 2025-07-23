import os
from PIL import Image
from rembg import remove

def remove_bg_and_apply_backgrounds(sharpened_image):
    """
    Removes background from the sharpened image and overlays it onto 5 preset backgrounds.
    """
    # Convert PIL image to bytes for rembg
    with Image.new("RGBA", sharpened_image.size) as canvas:
        fg = remove(sharpened_image)

    # Load backgrounds
    bg_dir = "static/backgrounds"
    background_files = sorted(os.listdir(bg_dir))[:5]
    output_images = []

    for bg_file in background_files:
        bg_path = os.path.join(bg_dir, bg_file)
        background = Image.open(bg_path).convert("RGBA")
        background = background.resize(sharpened_image.size)

        # Composite
        composed = Image.alpha_composite(background, fg)
        output_images.append(composed.convert("RGB"))

    return output_images
