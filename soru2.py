import numpy as np
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt

def changeImageSize(maxWidth,
                    maxHeight,
                    image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]

    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])

    newImage = image.resize((newWidth, newHeight))
    return newImage


F = Image.open('1-2.bmp').convert('L')

F = changeImageSize(100, 100, F)
F.save('F.jpg','JPEG')
F_pixel = F.load()
pixel = []
count = 0
density=0
for x in range(100):
    for y in range(100):
        pixel.append(F_pixel[x, y])
        density=density+F_pixel[x, y]
        count = count + 1
pixel.sort()
# pixel.reverse()

n, bins, patches = plt.hist(pixel, 20, density=True, facecolor='g', alpha=0.75)


plt.title('Histogram of Picture')
plt.axis([-5, 260, 0, 0.023])
plt.autoscale()
plt.grid(True)
plt.show()

img = np.zeros([100,100,3],dtype=np.uint8)
img.fill(255)
for x in range(100):
    for y in range(100):
        if(F_pixel[x, y]>165):
            img[x,y]=[255,0,0]
        else:
            img[x,y]=[0,0,0]

img = Image.fromarray(img, 'RGB')
img=img.rotate(270)
img=img.transpose(Image.FLIP_LEFT_RIGHT)
img.show()
img.save('colored.png','PNG')


area = (0, 50, 50, 100)
cropped_img = F.crop(area)
cropped_img.show()
cropped_img.save('crpped.png','PNG')

density=density/10000
print(density)


grey = np.zeros([100,100],dtype=np.uint8)
grey.fill(122)

for x in range(100):
    for y in range(100):
        if(F_pixel[x,y]>density):
            grey[x,y]=F_pixel[x,y]-density
        else:
            grey[x, y] =0
grey=Image.fromarray(grey, 'L')
grey=grey.rotate(270)
grey=grey.transpose(Image.FLIP_LEFT_RIGHT)
grey.show()
grey.save('dark.png','PNG')