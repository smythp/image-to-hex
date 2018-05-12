from PIL import Image
import sys

im = Image.open(sys.argv[1])

pixels = im.load()

x_pixels, y_pixels = im.size

output_array = []

for y_pixel in range(0, y_pixels):
    x_array = []

    for x_pixel in range(0, x_pixels):
        rgb_value = pixels[x_pixel, y_pixel]

        hex_code = '#%02x%02x%02x' % rgb_value[:3]

        x_array.append(hex_code)

    output_array.append(x_array)

                    
with open('hex.txt', 'w') as out_file:
    for x_row in output_array:
        for hex in x_row:
            out_file.write(hex + ' ')
