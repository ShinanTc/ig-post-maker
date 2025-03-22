import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Load the CSV file containing quotes
csv_file = "content.csv"
df = pd.read_csv(csv_file)

# Load the template image
template_path = "template.png"
font_path = "BricolageGrotesque_72pt-Bold.ttf"  # Ensure this font exists
output_folder = "generated_posts"

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Font settings
font_size = 60
text_color = "#dcfb73"
padding = 80  # Space from left & right edges

# Open template to get image size
image = Image.open(template_path)
image_width, image_height = image.size

# Define max text width considering padding
max_text_width = image_width - (2 * padding)  # Leaves equal space on both sides

# Process each quote
for index, row in df.iterrows():
    quote = row["Quote"]

    # Open template image
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)

    # Load custom font
    font = ImageFont.truetype(font_path, font_size)

    # Function to wrap text within max width
    def wrap_text(text):
        words = text.split()
        wrapped_lines = []
        line = ""

        for word in words:
            test_line = f"{line} {word}".strip()
            text_width = draw.textbbox((0, 0), test_line, font=font)[2]  # Get text width
            if text_width < max_text_width:
                line = test_line  # Add word to current line
            else:
                wrapped_lines.append(line)  # Store the full line
                line = word  # Start a new line with current word
        wrapped_lines.append(line)  # Add last line
        return wrapped_lines

    # Wrap the entire quote naturally
    lines = wrap_text(quote)

    # Calculate total text height
    line_height = font_size + 10  # Adjust line spacing
    total_text_height = len(lines) * line_height

    # Calculate starting Y position for centering
    y_start = (image_height - total_text_height) // 2

    # Draw each line
    for i, line in enumerate(lines):
        text_width = draw.textbbox((0, 0), line, font=font)[2]  # Get text width
        x = (image_width - text_width) // 2  # Center text with padding
        x = max(x, padding)  # Ensure it doesn't go beyond the left padding
        draw.text((x, y_start + i * line_height), line, font=font, fill=text_color)

    # Save the generated image
    output_path = os.path.join(output_folder, f"quote_{index+1}.png")
    image.save(output_path)

    print(f"✅ Generated: {output_path}")

print("🎉 All posts have been generated successfully!")
