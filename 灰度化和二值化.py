import numpy as np
import cv2

img = cv2.imread("cb.jpg")
h, w, _ = img.shape

# 灰度化
img_gray = np.zeros([h, w], img.dtype)
for i in range(h):
    for j in range(w):
        bgr = img[i, j]
        img_gray[i, j] = int(bgr[0] * 0.2 + bgr[1] * 0.36 + bgr[2] * 0.44)
print(img_gray, "img_gray")
cv2.imwrite("test_gray.jpg", img_gray)

# 二值化
img_cb = np.zeros([h, w], img.dtype)
for i in range(h):
    for j in range(w):
        bgr = img_gray[i, j]
        img_cb[i, j] = 0 if bgr < 127 else 255
print(img_cb, "img_cb")
cv2.imwrite("test_bw.jpg", img_cb)