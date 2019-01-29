from PIL import Image, ImageDraw, ImageFont
import os

def generateImg(strText1, strText2, strText3, strText4, strFileName):
    strFontFilePath = "usr/share/fonts/truetype/freefont/FreeMono.ttf"
    fontsize = 30

    # This create a width x height image, with background color
    img = Image.new('RGB', (200, 130), color = (255, 255, 255))     
    dPtr = ImageDraw.Draw(img)

    #drawAvatar.line([0, 0.33 * ySize, xSize, 0.33 * ySize],\
    #fill = (255, 100, 0), width = 3)
    
    # starting position (x,y), content, text color
    if os.path.exists("/usr/share/fonts/truetype/freefont/FreeMono.ttf"):      
      fnt = ImageFont.truetype(strFontFilePath, fontsize)
    else:
      print('Font file not found')

    dPtr.text((10,10), strText1, font=fnt, fill=(0,0,0))
    dPtr.text((10,35), strText2, font=fnt, fill=(0,0,0))    
    dPtr.text((10,40), strText3, font=fnt, fill=(0,0,0))    
    dPtr.text((10,70), strText4, font=fnt, fill=(0,0,0))    
    ImgPath =strFileName
    
    if os.path.exists(ImgPath):      
      os.remove(ImgPath)
      img.save(ImgPath)
      print("Replace existing file", ImgPath)
    else:
      img.save(ImgPath)
      print("Create file ",ImgPath)

