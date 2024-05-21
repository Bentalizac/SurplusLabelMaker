from PIL import Image, ImageDraw, ImageFont

def convert(inputFile, outputFile):

    # Read the text file
    with open(inputFile, 'r') as file:
        text = file.read()

    # Set the new image dimensions and font
    width, height = 1500, 600  # Set the desired width and height
    font = ImageFont.truetype("_internal/Aileron-Black.otf", size=90)

    # Create a new image with a white background
    image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(image)

    # Write the text on the image
    draw.multiline_text((30, 30), text, fill='black', font=font)

    # Save the image as PNG
    image.save(outputFile)
