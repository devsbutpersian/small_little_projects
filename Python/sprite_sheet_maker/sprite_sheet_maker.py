from PIL import Image



image_num = int(input("number of images: "))

row = int(input("row: "))
column = int(input("column: "))

img = Image.open('0.png')

width = img.size[0]
height = img.size[1]

img.close()

empty_image = Image.new("RGBA", (width * column, height * row), (255, 255, 255, 0))

image_pasted = 0

for i in range(row):
    if image_pasted == image_num:
        break
    for j in range(column):
        
        img = Image.open(str(image_pasted) + '.png')
        empty_image.paste(img, (width * j, height * i))

        img.close()
        
        image_pasted += 1
        if image_pasted == image_num:
            break

empty_image.save("finall_image.png")
empty_image.close()