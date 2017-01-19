from scipy.misc import imread
import numpy as np
import matplotlib.pyplot as plt

class Image:
	img = None
	def __init__(self, path):
		self.img = imread(path)
	def read(self, path):
		self.img = imread(path)
	def show(self):
		plt.imshow(img)
		plt.show()
	def showColor(self, i):
		clr = np.empty_like(img)
		clr[:,:,i] = img[:,:,i]
		plt.imshow(clr)
		plt.show()
	def showRed(self):
		showColor(self, 0)
	def showGreen(self):
		showColor(self, 1)
	def showBlue(self):
		showColor(self, 2)
	def getGrayscale(self):
		gr = np.empty_like(img)
		gr = np.sum(img, axes=2)
		gr /= 3
		return gr
	def showGrayscale(self):
		gr = getGrayscale(self)
		plt.imshow(gr)
		plt.show(gr)
	def showNegative(self):
		neg = 255-img
		plt.imshow(neg)
		plt.show()
	def showGrayscaleNegative(self):
		gr = getGrayscale(self)
		gr = 255-gr
		plt.imshow(gr)
		plt.show()
		
image = None
s = 100
while s!=0:
	s = raw_input("Choose:\n\t1. Read\n\t2. Display\n\t3. Display Red\n\t4. Display Green\n\t5. Display Blue\n\t6. Display Negative\n\t7. Display Grayscale\n\t8. Display Grascale Negative\n\t0. Exit\n")
	s = int(s)
	if s==1:
		path = raw_input("Enter path: ")
		image = Image(path)
	elif s!=0 and image==None:
		print("No image loaded!")
		continue
	elif s==2:
		image.show()
	elif s==3:
		image.showRed()
	elif s==4:
		image.showGreen()
	elif s==5:
		image.showBlue()
	elif s==6:
		image.showNegative()
	elif s==7:
		image.showGrayscale()
	elif s==8:
		image.showGrayscaleNegative()
	elif s!=0:
		print("Invalid input")
