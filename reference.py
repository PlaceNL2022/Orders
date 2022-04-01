import json
from PIL import Image

im = Image.open('reference.png') 
pix = im.load()

color_mappings = {
	'#FF4500': 2,
	'#FFA800': 3,
	'#FFD635': 4,
	'#00A368': 6,
	'#7EED56': 8,
	'#2450A4': 12,
	'#3690EA': 13,
	'#51E9F4': 14,
	'#811E9F': 18,
	'#B44AC0': 19,
	'#FF99AA': 23,
	'#9C6926': 25,
	'#000000': 27,
	'#898D90': 29,
	'#D4D7D9': 30,
	'#FFFFFF': 31
}
orders = []

def rgb_to_hex(rgb):
	return '#' + (('%02x%02x%02x' % rgb).upper())

formatted_out = '[\n'

for x in range(1000):
	for y in range(1000):
		colors = pix[x, y]
		if colors[3] == 0:
			continue
		hex = rgb_to_hex((colors[0], colors[1], colors[2]))
		colorid = color_mappings[hex]
		orders.append([x, y, colorid])
		formatted_out += '[' + str(x) + ', ' + str(y) + ', ' + str(colorid) + '],\n'

formatted_out += ']'

print(formatted_out)
