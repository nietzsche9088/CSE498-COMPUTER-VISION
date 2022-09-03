# *_*coding:utf-8 *_*
import numpy as np
def Gkernel(img, size, sigma):
    H, W, C = img.shape

    # zero padding
    pad = size // 2
    I = np.zeros((H + pad * 2, W + pad * 2, C), np.float32)
    I[pad:pad + H, pad:pad + W] = img.copy().astype(np.float32)

    K = np.zeros((size, size), np.float32)
    for x in range(-pad, -pad + size):
        for y in range(-pad, -pad + size):
            K[x + pad, y + pad] = np.exp(-(x ** 2 + y ** 2) / (2 * (sigma ** 2)))
    K /= (2 * np.pi * (sigma ** 2))
    # by 1/sum essential
    K /= K.sum()

    tmp = I.copy()
    for c in range(C):
        for y in range(H):
            for x in range(W):
                I[y + pad, x + pad, c] = np.sum(K * tmp[y:y + size, x:x + size, c])

    I = np.clip(I, 0, 255)
    # cut
    I = I[pad:pad + H, pad:pad + W].astype(np.uint8)
    return I