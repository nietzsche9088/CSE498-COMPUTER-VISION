# *_*coding:utf-8 *_*
from PIL import Image
import numpy as np
import os
from src import GaussianFilter, MeanFilter, MedianFilter
import time
import matplotlib.pyplot as plt

def task2():
    np.seterr(divide='ignore', invalid='ignore')
    folder_path = "../data/task2/"
    imgs = os.listdir(folder_path)
    imgNum = len(imgs)
    for i in range(imgNum):
        img = Image.open(folder_path+imgs[i]).convert('RGB')
        img = np.array(img)
        output1 = MeanFilter.Meanfilter(img, 3)
        output1 = Image.fromarray(output1,'RGB')
        output1.save("../output/task2/Mean_"+imgs[i])
        output2 = GaussianFilter.Gkernel(img, 3, 1.0)
        output2 = Image.fromarray(output2,'RGB')
        output2.save("../output/task2/Gaussian_"+imgs[i])
        output3 = MedianFilter.Medianfilter(img, 3)
        output3 = Image.fromarray(output3,'RGB')
        output3.save("../output/task2/Median_"+imgs[i])

        '''img1 = Image.open(folder_path + imgs[0])
        img1 = np.array(img1)
        size_batch = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
        intervel = []
        for i in size_batch:
            start = time.time()
            output = GaussianFilter.Gkernel(img1, i, 1.0)
            end = time.time()
            intervel.append(end - start)
        plt.plot(size_batch, intervel)
        plt.savefig("../output/task2/Size_time.jpg")'''
    return 0
