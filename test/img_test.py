import sys
import cv2
sys.path.append('./Lib/')
from make_contour_image import make_contour_image

def main():
	img = make_contour_image("input.jpg")
	cv2.imshow("gray",img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=='__main__':
	main()