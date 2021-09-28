from PIL import Image, ImageDraw,ImageFilter
def editImg(rect_img,bg_color):
    width, height = rect_img.size
    print(width,height)
    if width == height:
        return rect_img
    elif width > height:
        bg_img = Image.new(rect_img.mode,(width,width),bg_color ) 
        bg_img.paste(rect_img,(0,(width-height)//2))
        return bg_img
    else:
        bg_img = Image.new(rect_img.mode,(height,height),bg_color ) 
        bg_img.paste(rect_img,((width-height)//2),0)
        return bg_img

img = Image.open("download.png")
width = 288
height = 144
new_img = editImg(img,(255,255,255)).resize((width,height),Image.LANCZOS)
new_img.save("resized.png",quality = 95)