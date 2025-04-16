from PIL import Image
import os
def convert_image(input_path, output_format):
    try:
        img = Image.open(input_path)
        base = os.path.splitext(input_path)[0]
        output_path = f"{base}.{output_format.lower()}"
        img.save(output_path, output_format.upper())
        print(f"Image converted successfully: {output_path}")
    except Exception as e:
        print("Error:", e)
convert_image("sample.jpg", "png") 
