from Myro import *
        
def lightGraph():
    g = makePicture(600, 300)
    show(g)
    black = makeColor(0, 0, 0)
    for i in range(600):
        v = (2**16 - getLight('left'))/2
        setPixel(g, i, v, black)
    
def otherLightGraph():
    g = makePicture(200, 200)
    show(g)
    black = makeColor(0, 0, 0)
    for i in range(getWidth(g)):
        v = (2**16 - getLight('left'))/2
        for j in range(v):
            setPixel(g, i, j, black)
    
left = makePicture('left.jpg')
right = makePicture('right.jpg')

def makeAnaglyph(left,right):
    output = makePicture(getWidth(left),getHeight(left))
    for x in range(getWidth(left)):
        for y in range (getHeight(right)):
            target = getPixel(output,x,y)
            leftPix = getPixel(left,x,y)
            rightPix = getPixel(right,x,y)
            setRed(target,getRed(leftPix))
            setGreen(target,getGreen(rightPix))
            setBlue(target,getBlue(rightPix))
    return output
    show(output)

def anaglyph(left,right):
    output = makePicture(getWidth(left),getHeight(left))
    for x in range(getWidth(left)):
        for y in range(getHeight(left)):
            target = getPixel(output,x,y)
            left_pix = getPixel(left,x,y)
            right_pix = getPixel(right,x,y)
            setRed(target,getRed(left_pix))
            setGreen(target,getGreen(right_pix))
            setBlue(target,getBlue(right_pix))
    return output

show (anaglyph(left,right))
