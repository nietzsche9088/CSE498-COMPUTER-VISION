# *_*coding:utf-8 *_*
from PIL import Image
import numpy as np
import os
from src import SobelFilter
from src import GaussianFilter

def task3():
    np.seterr(divide='ignore', invalid='ignore')
    folder_path = "../data/task3/"
    imgs = os.listdir(folder_path)
    imgNum = len(imgs)

    #sobelkernel_h = np.array([[1,0,-1],[2,0,-2],[1,0,-1]])
    #sobelkernel_v = sobelkernel_h.T

    for i in range(imgNum):
        img = Image.open(folder_path+imgs[i]).convert('RGB')
        img = np.array(img)
        img = GaussianFilter.Gkernel(img,3,1.0)
        '''output_h = SobelFilter.Sobelfilter(img)
        output_v = SobelFilter.Sobelfilter(img)
        #magnitude
        G = np.sqrt(np.square(output_h)+np.square(output_v))
        #orientation
        theta = np.arctan(output_v/output_h)
        #print(theta)'''
        output_h, output_v, output = SobelFilter.Sobelfilter(img)
        output = Image.fromarray(output,'RGB')
        output.save("../output/task3/smooth_magnitude_" +imgs[i])

        output_h = Image.fromarray(output_h,'RGB')
        output_h.save("../output/task3/smooth_horizontal_"+imgs[i])

        output_v = Image.fromarray(output_v,'RGB')
        output_v.save("../output/task3/smooth_vertical_" +imgs[i])
    return 0
