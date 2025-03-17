import cv2
import numpy as np
import matplotlib as plot

def biggestContour(contours):
    bigContour = np.array({})
    maxArea = 0

    for contour in contours:
        area = cv2.contourArea(contour)
        perimeter = cv2.arcLength(contour, True)
        epsilon = .1*perimeter
        approx = cv2.approxPolyDP(contour, epsilon, True)
        if area > maxArea and len(approx) == 4:
            bigContour = approx
            maxArea = area
    return bigContour, maxArea

def contourCoordinateReordering(points):
    # reorder points to top-left, top-right, bottom-right, bottom-left
    points = points.reshape(4, 2)

    orderedPoints = np.zeros((4, 2), dtype=np.float32)
    sum = points.sum(axis=1)
    diff = np.diff(points, axis=1)

    orderedPoints[0] = points[np.argmin(sum)]
    orderedPoints[1] = points[np.argmin(diff)]
    orderedPoints[2] = points[np.argmax(sum)]
    orderedPoints[3] = points[np.argmax(diff)]
    orderedPoints = orderedPoints.reshape((4, 1, 2))
    return orderedPoints

