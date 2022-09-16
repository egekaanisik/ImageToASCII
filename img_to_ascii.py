import numpy as np
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
import os

# Main method
def main():
    img_path = Path(input("Path: ").strip(" \"")) # get image path
    scale = int(input("Scale (1-100)%: ").strip()) # get scale

    # check scale
    if scale < 1 or scale > 100:
        raise ValueError("Scale must be between 1 and 100.")

    img_raw = Image.open(img_path) # open image

    # calculate the new resolution
    h = int(img_raw.height * scale/100)
    w = int(img_raw.width * scale/100)

    print("\nThe raw photo resolution will be ({}, {}), and the output will be ({}, {}) after the ASCII transformation.".format(w, h, w*10, h*10))
    img_resized = img_raw.resize((w, h)) # resize the image

    print("Converting image to grayscale...")
    img = img_resized.convert("L") # convert the image to grayscale

    print("Getting character representations of each pixel...")
    img_array = np.asarray(img) # get image array
    ascii_list = np.full((h, w), fill_value="") # create a new array for ASCII values

    # transform every pixel to ASCII
    ascii_text = ""
    for i in range(h):
        for j in range(w):
            ch = getDensityChar(img_array[i][j]) # get ASCII representation by density
            ascii_list[i][j] = ch
            ascii_text += ch
        ascii_text += "\n"

    print("Filling the new image...")
    ascii_image = Image.new("RGB", (w*10, h*10), (255, 255, 255)) # create a new blank image 10 times larger than the resized image
    font = ImageFont.truetype("consola.ttf", 10) # create the font
    draw = ImageDraw.Draw(ascii_image) # create the instance for drawing

    # draw ASCII representations to the new image pixel-by-pixel
    for i in range(h):
        for j in range(w):
            draw.text((j*10, i*10), ascii_list[i][j], font=font, fill=(0, 0, 0), align='center')
    print("Done!")

    # get paths for saving results
    img_save_path = Path.joinpath(img_path.parent, "ASCII_" + img_path.name)
    text_save_path = Path.joinpath(img_path.parent, "ASCII_" + img_path.stem + ".txt")

    ascii_image.save(img_save_path) # save image
    with open(text_save_path, "w") as file: file.write(ascii_text) # save text

    # open results
    os.startfile(text_save_path)
    os.startfile(img_save_path)

    print("The ASCII image is saved to {},".format(img_save_path.absolute()))
    print("and the ASCII text is saved to {}.".format(text_save_path.absolute()))

# Method to convert a pixel to an ASCII character based on the average RGB value of the pixel.
def getDensityChar(pixel_value):
    chars = "@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-`" # ASCII density string
    chunk_list = np.array_split(range(0, 256), len(chars)) # split the RGB values into pieces
    
    # get the ASCII character for the pixel
    for i in range(len(chunk_list)): # for every RGB group
        if pixel_value in chunk_list[i]: # if the pixel's RGB value is in the current group
            return chars[i] # return the char at index i

# run the main method if the script is run directly
if __name__=='__main__':
    main()

