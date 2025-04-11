import cv2
import numpy as np
import matplotlib as plot
from CPY_ImageScan import *
from ImageProcessing.PDFGenerator import jpgs_to_pdf

if __name__ == "__main__":
    # --- Document Scan Test ---
    testImagePath = "ImageProcessing/testJPG/gridPaperExample.JPG"
    testImage = ScanDocument(testImagePath, option=2)
    ShowImage(testImage)

    # --- JPG to PDF Test ---
    image_list = [
        "ImageProcessing/testJPG/gridPaperExample.JPG",
        "ImageProcessing/testJPG/bookExample.JPG"  # Add more as needed
    ]
    output_pdf_path = "ImageProcessing/output.pdf"
    jpgs_to_pdf(image_list, output_pdf_path)
    print(f"PDF created at: {output_pdf_path}")
