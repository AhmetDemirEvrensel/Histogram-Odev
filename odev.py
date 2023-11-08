import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('resimler/suleymanseba.jpg', cv2.IMREAD_GRAYSCALE)

if image is not None:
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])

    plt.hist(image.ravel(), 256, [0, 256])
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Piksel Sayisi')
    plt.title('Gri Resim Histogrami')
    plt.show()
else:
    print("Resim yüklenemedi veya bulunamadi.")
