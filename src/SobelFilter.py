# *_*coding:utf-8 *_*
import numpy as np
def Sobelfilter(img, filter):
    H, W, C = img.shape

    # zero padding
    size = filter.shape[0]
    pad = size // 2
    I = np.zeros((H + pad * 2, W + pad * 2, C), np.float32)
    I[pad:pad + H, pad:pad + W] = img.copy().astype(np.float32)

    tmp = I.copy()
    for c in range(C):
        for y in range(H):
            for x in range(W):
                I[y + pad, x + pad, c] = np.sum(filter * tmp[y:y + size, x:x + size, c])

    I = np.clip(I, 0, 255)
    # cut
    I = I[pad:pad + H, pad:pad + W].astype(np.uint8)
    return I