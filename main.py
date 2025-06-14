import turtle
from PIL import Image


pen = turtle.Turtle()
pen.speed(100)
turtle.colormode(255)

def dot_pic(a, b, c):
    pen.pencolor((a, b, c))
    pen.penup()
    pen.goto(row - 200,  (col * -1) + 200)
    pen.pendown()
    pen.dot()
    
try:
    image = Image.open('ml5.jpg')
    pix = image.load()
    im_width = image.size[0]
    im_hight = image.size[1]

    for row in range(im_width):
        for col in range(im_hight):
            r1 = pix[row, col][0] #red pixel
            g1 = pix[row, col][1] #green
            b1 = pix[row, col][2] #blue
            pixel_tuple = (r1, g1, b1)
            dot_pic(r1, g1, b1)
except:
    print('Have not a file or bad name!')

turtle.done()