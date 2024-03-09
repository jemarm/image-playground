import sys
import os
from PIL import Image

# path = sys.argv[1]
# directory = sys.argv[2]


# grab first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]

# check if new/ exists, if not create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    if '.DS_Store' not in filename:
        img = Image.open(f'{image_folder}{filename}')
        clean_name = os.path.splitext(filename)[0]
        img.save(f'{output_folder}{clean_name}.png', 'png')
        print('all done!')


# # grab first and second arguement
# input_directory = "./Pokedex/"

# output_directory = "./PNG_Pokedex"

# # check if new/exists if not create it
# os.makedirs(output_directory, exist_ok=True)


# # loop through pokedex,
# for filename in os.listdir(input_directory):
#     if filename.endswith(".jpg"):
#         # convert images to png
#         with Image.open(os.path.join(input_directory, filename)) as img:
#             # save to the new folder
#             png_filename = os.path.splitext(filename)[0] + ".png"
#             img.save(os.path.join(output_directory, png_filename))
#             print(f"Converted {filename} to {png_filename}")
