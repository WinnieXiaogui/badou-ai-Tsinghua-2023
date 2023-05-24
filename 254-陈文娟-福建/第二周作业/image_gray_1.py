
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

# 灰度化
img = cv2.imread("lenna.png")    # 获取图像每个点的RGB值,并存在img中，是numpy.ndarray类
# print(type(img),img)
h , w =img.shape[:2]     # shape函数：读取矩阵或数组的长度
print(h,w)      # type(img)：<class 'numpy.ndarray'>
'''
shape的用法：
img.shape[ : 2] 表示取彩色图片的长、宽。
img.shape[ : 3] 则表示取彩色图片的长、宽、通道。

关于img.shape[0]、[1]、[2]
img.shape[0]：图像的垂直尺寸（高度）
img.shape[1]：图像的水平尺寸（宽度）
img.shape[2]：图像的通道数

在矩阵中，[0]就表示行数，[1]则表示列数。
'''

# a = img.dtype
# print(a)
img_gray = np.zeros([h,w],img.dtype)
# 准备一张与img大小一样的数列，img.dtype是img的数据类型
# img.dtype运行后得到dtype（‘uint8’）表示储存这些像素值的数字数uint8类型(0-255)。 dtype表示数据类型
# k=0
for i in range(h):
    for j in range(w):
        m = img[i,j]
        # k=k+1
        # print(m, k)
        # break
        img_gray[i,j] = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3) # 彩色转换成灰色[0~255]
# print (img_gray)
print("image show gray: %s"%img_gray)
cv2.imshow("image show gray",img_gray)


'''
waitKey（）的作用
1、waitKey()–这个函数是在一个给定的时间内(单位ms)等待用户按键触发;如果用户没有按下 键,则接续等待(循环）
2、如果设置waitKey(0),则表示程序会无限制的等待用户的按键事件'''


plt.subplot(221)
img = plt.imread("lenna.png") 
# img = cv2.imread("lenna.png", False)
plt.imshow(img)
print("---image lenna----")
print(img)

# 灰度化
img_gray = rgb2gray(img)
plt.subplot(222)
plt.imshow(img_gray,cmap='gray')
print("---image_gray lenna----")
print(img_gray)

# 二值化
img_binary = np.zeros([h,w],img_gray.dtype)
for i in range(h):
    for j in range(w):
        if img_gray[i][j]<0.5:
            img_binary[i][j] = 0
        else:
            img_binary[i][j] = 1

'''
img_binary = np.where(img_gray < 0.5,0,1)
print("-----imge_binary------")
print(img_binary)
print(img_binary.shape)
'''
plt.subplot(223)
plt.imshow(img_binary,cmap='gray')
print("---image_binary lenna----")
plt.show()











