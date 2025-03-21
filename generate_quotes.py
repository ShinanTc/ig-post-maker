import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
import gdown  # To download the font automatically

# Load CSV (ensure it has only one column: "Quote")
df = pd.read_csv("coding_motivation_quotes.csv")

# Strip spaces from column names
df.columns = df.columns.str.strip()

# Print column names to verify
print("CSV Columns:", df.columns)

# Paths
template_path = "template.png"  # Ensure this file exists
output_folder = "generated_posts/"
font_path = "BricolageGrotesque-Regular.ttf"  # Ensure this file is in the project folder
font = ImageFont.truetype(font_path, 60)

# Google Drive link for Bricolage Grotesque Regular font
font_url = "https://drive.google.com/uc?id=1TjBf0A2K4tV4KMkgJYkgU1IQGnZkUbxQ"

# Check if font exists, if not, download it
if not os.path.exists(font_path):
    print("🔽 Downloading Bricolage Grotesque font...")
    gdown.download(font_url, font_path, quiet=False)

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Font settings
font_size = 60
font_color = "#dcfb73"  # Light yellow-green color

# Iterate through each quote and generate an image
for index, row in df.iterrows():
    quote = row["Quote"]  # Only one column

    # Open the template image
    img = Image.open(template_path)
    draw = ImageDraw.Draw(img)

    # Load font
    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"❌ Font '{font_path}' is missing! Exiting program.")
        exit()

    # Define text position (adjust as needed)
    text_position = (100, 250)  # Change coordinates based on your design

    # Add quote text with updated font
    draw.text(text_position, quote, font=font, fill=font_color)

    # Save the image
    output_path = f"{output_folder}post_{index+1}.png"
    img.save(output_path)
    print(f"✅ Generated: {output_path}")

print("🎉 All posts generated successfully!")