# *_*coding:utf-8 *_*
from PIL import Image
import numpy as np
import os
from src import GuassianFilter



def task1():
    folder_path = "../data/task1/"
    imgs = os.listdir(folder_path)
    imgNum = len(imgs)
    for i in range(imgNum):
        img = Image.open(folder_path+imgs[i])
        img = np.array(img)

        G = GuassianFilter.Gkernel(img, 3, 1.0)
        D = img - G
        I = img + D

        output = Image.fromarray(I, 'RGB')
        output.save("../output/task1/enhanced_"+imgs[i])
    return 0
