import fitz  # Import the PyMuPDF library
from PIL import Image
import io

def generate_image_array_from_pdfs(pdf_files):
    images = []  # Initialize an array to store images

    for pdf_file in pdf_files:
        doc = fitz.open(pdf_file)  # Open the PDF file
        for page in doc:  # Iterate through each page
            pix = page.get_pixmap()  # Render page to a pixmap (an image)
            img = pix.tobytes("png")  # Convert the pixmap to PNG bytes (in memory)
            images.append(img)  # Append the PNG image bytes to the array
    
    doc.close()  # Close the PDF file
    return images  # Return the array of images


def scale_image(image_bytes, square_size = 512):
    """
    Scale the image to fit within a 512x512 square, maintaining aspect ratio.

    Args:
    - image_bytes (bytes): The original image in bytes.

    Returns:
    - bytes: The scaled image in bytes.
    """
    # Convert bytes to a PIL Image
    image = Image.open(io.BytesIO(image_bytes))
    
    # Calculate the target size to maintain aspect ratio
    target_size = square_size
    original_width, original_height = image.size
    ratio = min(target_size / original_width, target_size / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Convert the PIL Image back to bytes
    img_byte_arr = io.BytesIO()
    resized_image.save(img_byte_arr, format='PNG')  # Save as PNG
    scaled_image_bytes = img_byte_arr.getvalue()
    
    return scaled_image_bytes
