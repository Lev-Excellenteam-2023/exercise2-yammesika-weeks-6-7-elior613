from PIL import Image
im = Image.open('code.PNG','r')
px = im.load()
l=[]
for column in range(im.size[0]):
    l+=([chr(row) for row in range(im.size[1]) if px[column,row]!=255])
code=''
for i in l:
    code+=i
print (code)

