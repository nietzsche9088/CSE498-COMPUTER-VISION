# *_*coding:utf-8 *_*
import numpy as np
#import cv2
def Meanfilter(img, size):
    K = np.full((size, size), 1 / (size ** 2))

    H, W, C = img.shape

    # zero padding
    pad = size // 2
    I = np.zeros((H + pad * 2, W + pad * 2, C), np.float32)
    I[pad:pad + H, pad:pad + W] = img.copy().astype(np.float32)
    #I = cv2.copyMakeBorder(img,pad,pad,pad,pad,cv2.BORDER_REPLICATE)
    tmp = I.copy()

    for c in range(C):
        for y in range(H):
            for x in range(W):
                I[y + pad, x + pad, c] = np.sum(K * tmp[y:y + size, x:x + size, c])
    I = np.clip(I, 0, 255)

    # cut
    I = I[pad:pad + H, pad:pad + W].astype(np.uint8)
    return I