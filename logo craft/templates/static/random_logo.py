import random
import os
from PIL import Image, ImageDraw, ImageFont

# Directory for saving logo images
LOGO_DIR = 'static/logos'

if not os.path.exists(LOGO_DIR):
    os.makedirs(LOGO_DIR)

def generate_logo():
    # Image size and background color
    width, height = 200, 200
    bg_color = random.choice(['#FF5733', '#33FF57', '#3357FF', '#FFFF33'])
    
    # Create a blank image with the selected background color
    img = Image.new('RGB', (width, height), bg_color)
    draw = ImageDraw.Draw(img)
    
    # Random text for the logo
    text = random.choice(['Logo1', 'Logo2', 'Logo3', 'LogoX'])
    font = ImageFont.load_default()  # Using default font for simplicity
    
    # Get text size and position it in the center
    text_width, text_height = draw.textsize(text, font)
    text_position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Add the text to the image
    text_color = random.choice(['#FFFFFF', '#000000'])
    draw.text(text_position, text, fill=text_color, font=font)
    
    # Save the generated logo image
    logo_filename = f"logo_{random.randint(1, 10000)}.png"
    logo_path = os.path.join(LOGO_DIR, logo_filename)
    img.save(logo_path)
    
    # Return the path of the saved logo
    return logo_path
