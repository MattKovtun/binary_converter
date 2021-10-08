from PIL import Image
import binascii
import io
import os
import sys


def convert_binaries_to_jpgs(filename, folder):
    data = []
    
    # creating output directory if it doesn't exist
    if not os.path.exists(folder):
        os.mkdir(folder)
        
    # reading binaries
    with open(filename, encoding='utf-16') as f:
        header = f.readline()
        for line in f:
            data.append(line.strip().split())
    
    # transforming binaries to jpgs
    for image_id, image_binary in data:
        try:
            unhexed = binascii.unhexlify(image_binary.encode())
            image = Image.open(io.BytesIO(unhexed))
            rgb_im = image.convert('RGB')        
        except:
            print(f'Error occured in {image_id} binary')
            continue
        rgb_im.save(folder + '/' + image_id + '.jpg')

if __name__ == "__main__":
    binary_file = 'images.txt'
    output_folder = 'images_jpg'
    
    if len(sys.argv) > 1:
        binary_file = sys.argv[1]
        output_folder = sys.argv[2]
    
    convert_binaries_to_jpgs(binary_file, output_folder)