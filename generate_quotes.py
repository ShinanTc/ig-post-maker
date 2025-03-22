import os
import pandas as pd
from PIL import Image, ImageDraw, ImageFont

# Prompt user for template choice
print("Choose a template:")
print("A: Freaking Monday Post")
print("B: Weekend Mode Post")
template_choice = input("Enter your choice (A/B): ").strip().upper()

# Determine template file based on choice
template_map = {
    "A": "templates/freakin-monday.png",
    "B": "templates/weekend-mode.png"
}
template_path = template_map.get(template_choice)

if not template_path:
    print("❌ Invalid choice. Please restart and choose A or B.")
    exit()

# Load the CSV file containing quotes
csv_file = "content.csv"
df = pd.read_csv(csv_file)

# Font settings
font_path = "BricolageGrotesque_72pt-Bold.ttf"  # Ensure this font exists
font_size = 60
text_color = "#dcfb73"
padding = 80  # Space from left & right edges

# Open template to get image size
image = Image.open(template_path)
image_width, image_height = image.size

# Define max text width considering padding
max_text_width = image_width - (2 * padding)

# Create output folder
output_folder = "generated_posts"
os.makedirs(output_folder, exist_ok=True)

# Process each quote
for index, row in df.iterrows():
    quote = row["Quote"]
    
    # Open template image
    image = Image.open(template_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    
    # Function to wrap text within max width
    def wrap_text(text):
        words = text.split()
        wrapped_lines = []
        line = ""
        
        for word in words:
            test_line = f"{line} {word}".strip()
            text_width = draw.textbbox((0, 0), test_line, font=font)[2]
            if text_width < max_text_width:
                line = test_line
            else:
                wrapped_lines.append(line)
                line = word
        wrapped_lines.append(line)
        return wrapped_lines

    # Wrap the quote
    lines = wrap_text(quote)
    
    # Calculate text height and position
    line_height = font_size + 10
    total_text_height = len(lines) * line_height
    y_start = (image_height - total_text_height) // 2

    # Draw each line
    for i, line in enumerate(lines):
        text_width = draw.textbbox((0, 0), line, font=font)[2]
        x = max((image_width - text_width) // 2, padding)
        draw.text((x, y_start + i * line_height), line, font=font, fill=text_color)
    
    # Save the generated image
    output_path = os.path.join(output_folder, f"quote_{index+1}.png")
    image.save(output_path)
    print(f"✅ Generated: {output_path}")

print("🎉 All posts have been generated successfully!")