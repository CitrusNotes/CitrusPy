import cv2
import numpy as np
import matplotlib as plot
from CPY_ImageScan import *
import unittest

if __name__ == "__main__":
    testImagePath = "ImageProcessing/testJPG/looseLeafExample.JPG"
    testImage = cv2.imread(testImagePath)

    # Image Path check
    if testImage is None:
        print("Invalid Path")
    else:
        # Print Test Image
        cv2.imshow('Test Image', testImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
        # Gray Image Conversion and Printing
        # Grey Image Conversion because intensity values are better for edge detection and transformation
        testImageGray = cv2.cvtColor(testImage,cv2.COLOR_RGB2GRAY)
        cv2.imshow('Test Image Gray', testImageGray)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Gaussian Blur on Gray Image
        # Gaussian Blur on Gray Image reduces the general noise
        # GaussianBlur third param is sigmax; 0 - automatic blur, 1 - small bluring, 1> - more blurring
        testImageGrayBlur = cv2.GaussianBlur(testImageGray, (5,5), 0)
        cv2.imshow('Test Image Gaussian Blur', testImageGrayBlur)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Should have something here to apply different Thresholding
        # Canny Edge Detection
        
        # add threshold bar
        thres1 = 45
        thres2 = 125
        testImgGrayEdges = cv2.Canny(testImageGrayBlur,thres1,thres2)
        cv2.imshow(f'Test Image Edges {thres1} {thres2}', testImgGrayEdges)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        

        # Image Closing - Perserves Larger Shapes
        kernel = np.ones((5,5))
        testImgGEClosing = cv2.dilate(testImgGrayEdges, kernel, iterations=3)
        testImgGEClosing = cv2.erode(testImgGEClosing, kernel, iterations=2)
        cv2.imshow('Test Image Closing', testImgGEClosing)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Contour - Our main document is in the shape of rectangle
        testImgContours = testImage.copy()
        contours, hierarchy = cv2.findContours(testImgGEClosing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        
        # draw contour on our image copy; -1 represent all contours; 4th param is color of the contour; 
        cv2.drawContours(testImgContours, contours, -1, (255, 150, 150), 5) 
        cv2.imshow('Test Image Contours', testImgContours)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Get Biggest Contour
        # FIXME
        

