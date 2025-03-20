import cv2
import numpy as np
import matplotlib as plot
from CPY_ImageScan import *
import unittest

if __name__ == "__main__":
    testImagePath = "ImageProcessing/testJPG/looseLeafExample.JPG"
    testImage = ScanDocument(testImagePath,option=2)
    ShowImage(testImage)


        

