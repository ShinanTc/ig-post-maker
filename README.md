### TECH STACK USED:

Programming Language: Python 🐍
Image Processing: Pillow (PIL) 🖼
Data Handling: Pandas 📊
Font Management: Custom TTF Font (Bricolage Grotesque) 🎨

### HOW TO RUN?

# Quote Image Generator

## Description
This script generates motivational quote images based on a provided CSV file. The text is formatted and centered on a template image with proper line wrapping. Users can select a specific template before generating the images.

---

## Installation & Setup

### 1. Create and Activate a Virtual Environment
```bash
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate on macOS/Linux
venv\Scripts\activate  # Activate on Windows
```

### 2. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 3. Prepare the CSV File
Place a `content.csv` file with the one containing the quotes. You can generate a fresh CSV using ChatGPT or manually create one.

### 4. Provide a Base Template
Ensure that you have a template image inside the `templates` directory. The project is currently optimized for a specific base template. Adjustments may be needed for different templates.

### 5. Include a Font File
- Place a `.ttf` font file in the root directory.
- If the font file is missing, download the required font from [Google Fonts](https://fonts.google.com/) and place it in the root folder.
- Update the `font_path` variable in `generate_quotes.py` to reflect the correct font file name.

### 6. Run the Script
```bash
python generate_quotes.py
```

---

## Usage
When executing the script, you will be prompted to choose a template:
```
Choose a template:
A) Freaking Monday Post
B) Weekend Mode Post
```
- Enter `A` to use `freakin-monday.png`.
- Enter `B` to use `weekend-mode.png`.

Once executed, the script will generate the quote images inside the `generated_posts` directory. 🎉

---

## Output
All generated images will be saved in:
```
/generated_posts/
```
Each image will be labeled sequentially as `quote_1.png`, `quote_2.png`, etc.

---

## Notes
- The script automatically wraps text to fit within the template.
- Padding is applied to avoid text overlapping.
- Ensure your CSV file follows the correct format with a column named `Quote`.

Happy Generating! 🚀