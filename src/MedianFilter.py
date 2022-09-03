# *_*coding:utf-8 *_*
import numpy as np

def Medianfilter(img, size):
    H, W, C = img.shape

    # zero padding
    pad = size // 2
    I = np.zeros((H + pad * 2, W + pad * 2, C), np.float32)
    I[pad:pad + H, pad:pad + W] = img.copy().astype(np.float32)
    tmp = I.copy()

    for c in range(C):
        for y in range(H):
            for x in range(W):
                I[y + pad, x + pad, c] = np.median(tmp[y:y + size, x:x + size, c])
    I = np.clip(I, 0, 255)
    # cut
    I = I[pad:pad + H, pad:pad + W].astype(np.uint8)
    return I