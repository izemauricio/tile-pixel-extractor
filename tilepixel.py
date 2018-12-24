import sys
from PIL import Image
print('Argv str: ' + str(sys.argv))
print('Argv len: ' + str(len(sys.argv)))
if (len(sys.argv) != 3):
	print('Usage: python ' + sys.argv[0] + ' image_name.png varname')
	exit()
img = Image.open('./' + sys.argv[1])
pix = img.load()
print(img.size)
img2 = Image.new('RGBA',(img.size[0],img.size[1]))
pix2 = img2.load()
file = open(sys.argv[1] + '.js','w')
file.write('var ' + sys.argv[2] + ' = [')
file.write(str(img.size[0])+','+str(img.size[1])+',')
yvalues = range(img.size[1])
xvalues = range(img.size[0])
lasty = yvalues[-1]
lastx = xvalues[-1]
for y in yvalues:
	for x in xvalues:
		r = (pix[x,y][0])
		g = (pix[x,y][1])
		b = (pix[x,y][2])
		a = (pix[x,y][3])
		pix2[x,y] = (r,g,b,a)
		file.write(str(r)+','+str(g)+','+str(b)+','+str(a))
		if x != lastx:
			file.write(',')
	if y == lasty and x == lastx:
			file.write('];')
	if y != lasty and x == lastx:
		file.write(',')
img2.save(sys.argv[2] + '_result.png')