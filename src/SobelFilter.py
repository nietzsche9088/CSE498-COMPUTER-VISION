# *_*coding:utf-8 *_*
import numpy as np
def Sobelfilter(img):
    H, W, C = img.shape

    sobelkernel_h = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    sobelkernel_v = sobelkernel_h.T

    # zero padding
    size = 3
    pad = size // 2
    I = np.zeros((H + pad * 2, W + pad * 2, C), np.float32)
    I[pad:pad + H, pad:pad + W] = img.copy().astype(np.float32)
    I_x = I.copy()
    I_y = I.copy()
    tmp_x = I.copy()
    tmp_y = I.copy()
    I = np.zeros(shape=(H, W, C))
    for c in range(C):
        for y in range(H):
            for x in range(W):
                I_x[y + pad, x + pad, c] = np.sum(sobelkernel_h * tmp_x[y:y + size, x:x + size, c])
                I_y[y + pad, x + pad, c] = np.sum(sobelkernel_v * tmp_y[y:y + size, x:x + size, c])
                I[y,x,c] = np.sqrt(I_x[y + pad, x + pad, c]**2 + I_y[y + pad, x + pad, c]**2)

    I_x = np.clip(I_x, 0, 255)
    I_y = np.clip(I_y, 0, 255)
    I = np.clip(I, 0, 255)
    # cut
    I = I[0: H, 0: W].astype(np.uint8)
    I_x = I_x[pad:pad + H, pad:pad + W].astype(np.uint8)
    I_y = I_y[pad:pad + H, pad:pad + W].astype(np.uint8)
    return I_x,I_y,I