from PIL import Image

def jpgs_to_pdf(image_paths, output_path):
    """
    Converts a list of JPG image paths to a single PDF.
    Assumes all images are RGB or converts them if needed.

    Parameters:
        image_paths (list of str): Paths to JPG images.
        output_path (str): Output path for the PDF.

    Returns:
        None
    """
    images = []
    for path in image_paths:
        img = Image.open(path).convert("RGB")
        images.append(img)

    if images:
        images[0].save(output_path, save_all=True, append_images=images[1:])
