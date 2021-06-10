from PIL import Image
from time import sleep

fileName = input("Path to file: ")
im = Image.open(fileName)
print(im.format, im.size, im.mode)

pixels = im.load()
width, height = im.size
pixelArray = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(pixels[x, y])
    pixelArray.append(row)

averageArray = []
for row in pixelArray:
    averageRow = []
    for each in row:
        sum = 0
        for val in each:
            sum += val
        avg = int(sum/3)
        averageRow.append(avg)
    averageArray.append(averageRow)

lumArray = []
for row in pixelArray:
    lumRow = []
    for each in row:
        lum = int(each[0]*.21+each[1]*0.72+each[2]*0.07)
        lumRow.append(lum)
    lumArray.append(lumRow)

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for row in lumArray:
    charRow = ''
    for each in row:
        #each = each*-1+255 ##Invert
        i = int(each * 20 / 255)
        charRow += chars[i]*3
    print(charRow)
    sleep(0.05)
