# *_*coding:utf-8 *_*
from PIL import Image
import numpy as np
import os
from src import SobelFilter

def task3():
    folder_path = "../data/task3/"
    imgs = os.listdir(folder_path)
    imgNum = len(imgs)

    sobelkernel_h = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    sobelkernel_v = sobelkernel_h.T

    for i in range(imgNum):
        img = Image.open(folder_path+imgs[i])
        img = np.array(img)
        output_h = SobelFilter.Sobelfilter(img, sobelkernel_h)
        output_v = SobelFilter.Sobelfilter(img, sobelkernel_v)
        #magnitude
        G = np.sqrt(np.square(output_h)+np.square(output_v))
        print(G)
        #orientation
        theta = np.arctan(output_v/output_h)
        print(theta)
        output = Image.fromarray(G, 'RGB')
        output.save("../output/task3/magnitude_" + imgs[i])

        output_h = Image.fromarray(output_h, 'RGB')
        output_h.save("../output/task3/horizontal_"+imgs[i])

        output_v = Image.fromarray(output_v, 'RGB')
        output_v.save("../output/task3/vertical_" + imgs[i])
    return 0
