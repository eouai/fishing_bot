from PIL import Image
import os
import argparse

def rescale_image(directory, size):
	for img in os.listdir(directory):
		im = Image.open(directory=img)
		im_resized = im.resize(size, Image.ANTIALIAS)
		im_resized.save(directory=img)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Rescale Image")
	parser.add_argument('-d', '--directory', type=str, required=True, help='')
	parser.add_argument('-s', '--size', type=int, nargs=2, required=True)
	args = parser.parse_args()
	rescale_image(args.directory, args.size)
