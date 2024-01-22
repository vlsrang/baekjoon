# import library
import numpy as np
from PIL import Image
from PIL import ImageFilter


def BGR2GRAY(img):
    img=np.array(img)
    b = img[:, :, 0].copy()
    g = img[:, :, 1].copy()
    r = img[:, :, 2].copy()
    out = 0.2126 * r + 0.7152 * g + 0.0722 * b

    return out
    

def binalization(img, th=128):
    img[img < th] = 0
    img[img >= th] = 255

    return img

# 이미지 불러오기
img=Image.open('9주차/Audrey.png')
result=np.array(img)


##### do not edit here #####
result = BGR2GRAY(result)
result = binalization(result)
result = Image.fromarray(result.astype('uint8'))

result.save('./result.png')

result.show()
