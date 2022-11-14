import cv2 
import matplotlib.pyplot as plt

img = cv2.imread('z.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10,6))
# plt.title('Image display example')
plt.imshow('Window for Zebra image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()