from typing import Tuple
import numpy as np
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
import os

class Resolution:
    """
    Image size holder.
    """
    
    def __init__(self, width: int, height: int):
        """
        Creates a resolution object for holding an image's size.

        :param width: Image width.
        :param height: Image height.
        
        """

        self.width = width
        self.height = height

    def get_tuple(self) -> Tuple:
        """
        Get the tuple representation of the resolution:

        :returns: A tuple with the values (width, height).

        """

        return (self.width, self.height)

    def __str__(self) -> str:
        """
        Get the string representation of the resolution.

        :returns: A string with the values (width, height).

        """

        return str(self.get_tuple())

class ImageToASCII:
    """
    Convert an image to its ASCII representation.
    """

    def __init__(self, img_path, scale=100, print_log=False):
        """
        Opens the given image and prepares it for transformation. This does not apply the transformation.
        To convert it to ASCII, call execute() method afterwards.

        :param img_path: A filename (string) or a :py:class:`~pathlib.PIL` object of the image to be converted.
        :param scale: The image scale. (must be between 1-100)
        :exception TypeError: If ``img_path`` is not a valid type.
        :exception ValueError: If ``scale`` is not between 1 and 100.

        """
        
        # validate the type of img_path
        if isinstance(img_path, str):
            self._img_path = Path(img_path)
        elif isinstance(img_path, Path):
            self._img_path = img_path
        else:
            raise TypeError("img_path must be a string or a pathlib.Path object.")

        # check scale
        if scale < 1 or scale > 100:
            raise ValueError("Scale must be between 1 and 100.")

        # set the fields
        self._img_raw = Image.open(self._img_path) # open image
        self._img = None
        self._str = None
        self._logging = print_log
        self._scale = scale

    def execute(self):
        """
        Converts the image to ASCII.
        """

        # get the new resolutions
        resized_res = self.get_resized_res() # resized resolution
        output_res = self.get_output_res() # output resolution

        if self._logging: print("The resized photo resolution will be {}, and the output will be {} after the ASCII transformation.".format(str(resized_res), str(output_res)))
        img_resized = self._img_raw.resize(resized_res.get_tuple()) # resize the image

        if self._logging: print("Converting image to grayscale...")
        img = img_resized.convert("L") # convert the image to grayscale

        if self._logging: print("Getting character representations of each pixel...")
        img_array = np.asarray(img) # get image array
        ascii_list = np.full(resized_res.get_tuple(), fill_value="") # create a new array for ASCII values

        # transform every pixel to ASCII
        ascii_text = ""
        for i in range(resized_res.height):
            for j in range(resized_res.width):
                ch = self._get_density_char(img_array[i][j]) # get ASCII representation by density
                ascii_list[i][j] = ch
                ascii_text += ch
            ascii_text += "\n"

        if self._logging: print("Filling the new image...")
        ascii_image = Image.new("RGB", output_res.get_tuple(), (255, 255, 255)) # create a new blank image with the output resolution
        font = ImageFont.truetype("consola.ttf", 10) # create the font
        draw = ImageDraw.Draw(ascii_image) # create the instance for drawing

        # draw ASCII representations to the new image pixel-by-pixel
        for i in range(resized_res.height):
            for j in range(resized_res.width):
                draw.text((j*10, i*10), ascii_list[i][j], font=font, fill=(0, 0, 0), align='center')
        if self._logging: print("Done!")

        # set the outputs as fields
        self._img = ascii_image
        self._str = ascii_text

    def get_ascii_image(self) -> Image.Image :
        """
        Get the ASCII-converted image.

        :returns: An :py:class:`~PIL.Image.Image` object with the converted image data.
        :exception RuntimeError: If the operation is not executed yet.

        """

        if self._img is None:
            raise RuntimeError("The operation is not executed yet.")
        return self._img

    def get_raw_image(self) -> Image.Image :
        """
        Get the raw image.

        :returns: An :py:class:`~PIL.Image.Image` object with the raw image data.

        """

        return self._img_raw

    def get_ascii_text(self) -> str :
        """
        Get the ASCII-converted text.

        :returns: A string with the converted image data.
        :exception RuntimeError: If the operation is not executed yet.

        """

        if self._str is None:
            raise RuntimeError("The operation is not executed yet.")
        return self._str

    def get_image_path(self) -> Path:
        """
        Get the input image's path.

        :returns: A :py:class:`~pathlib.PIL` object with the path data.

        """

        return self._img_path

    def get_scale(self) -> int:
        """
        Get the scale that the image is resized with.

        :returns: The image scale.

        """

        return self._scale

    def get_original_res(self) -> Resolution:
        """
        Get the original resolution.

        :returns: A :py:class:`~img_to_ascii.Resolution` object with the original resolution.

        """

        return Resolution(self._img_raw.width, self._img_raw.height)

    def get_resized_res(self) -> Resolution:
        """
        Get the resized resolution before the image transformation.

        :returns: A :py:class:`~img_to_ascii.Resolution` object with the resized resolution.

        """

        w = int(self._img_raw.width * self._scale/100) # calculate width
        h = int(self._img_raw.height * self._scale/100) # calculate height
        return Resolution(w, h)

    def get_output_res(self) -> Resolution:
        """
        Get the output resolution after the image transformation.

        :returns: A :py:class:`~img_to_ascii.Resolution` object with the output resolution.

        """

        resized = self.get_resized_res()
        return Resolution(resized.width*10, resized.height*10)

    def _get_density_char(self, pixel_value):
        """
        Converts a pixel to an ASCII character based on the average RGB value of the pixel.

        :returns: A character that represents the density of the pixel.

        """

        chars = "@QB#NgWM8RDHdOKq9$6khEPXwmeZaoS2yjufF]}{tx1zv7lciL/\\|?*>r^;:_\"~,'.-`" # ASCII density string
        chunk_list = np.array_split(range(0, 256), len(chars)) # split the RGB values into pieces
        
        # get the ASCII character for the pixel
        for i in range(len(chunk_list)): # for every RGB group
            if pixel_value in chunk_list[i]: # if the pixel's RGB value is in the current group
                return chars[i] # return the char at index i

# run the main method if the script is run directly
if __name__=='__main__':
    img_path = Path(input("Path: ").strip(" \"")) # get image path
    scale = int(input("Scale (1-100)%: ").strip()) # get scale
    print()

    img_to_ascii = ImageToASCII(img_path, scale=scale, print_log=True) # create instance

    # get paths for saving results
    img_save_path = Path.joinpath(img_path.parent, "ASCII_" + img_path.name)
    text_save_path = Path.joinpath(img_path.parent, "ASCII_" + img_path.stem + ".txt")

    img_to_ascii.execute() # execute the transformation

    ascii_image = img_to_ascii.get_ascii_image() # get the output image
    ascii_text = img_to_ascii.get_ascii_text() # get the output text

    ascii_image.save(img_save_path) # save image
    with open(text_save_path, "w") as file: file.write(ascii_text) # save text

    # open results
    os.startfile(text_save_path)
    os.startfile(img_save_path)

    print("The ASCII image is saved to {},".format(img_save_path.absolute()))
    print("and the ASCII text is saved to {}.".format(text_save_path.absolute()))