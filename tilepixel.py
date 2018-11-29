from PIL import Image
img = Image.open('./input.png')
pix = img.load()
print(img.size)
img2 = Image.new('RGB',(img.size[0],img.size[1]))
pix2 = img2.load()
file = open('output.txt','w')
file.write(str(img.size[0])+','+str(img.size[1])+',');
for y in range(img.size[1]):
	for x in range(img.size[0]):
		r = (pix[x,y][0])
		g = (pix[x,y][1])
		b = (pix[x,y][2])
		a = (pix[x,y][3])
		pix2[x,y] = (r,g,b,a)
		file.write(str(r)+','+str(g)+','+str(b)+','+str(a)+',')
img2.save('new.png')