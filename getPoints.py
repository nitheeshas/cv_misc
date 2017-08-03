###########################################
# Run the code as follows:                #
# $ python getPoints.py <image filename>  #
###########################################

import cv2
import sys


def getCoordinate(event, x, y, flags, points):
    if event == cv2.EVENT_LBUTTONUP:
        points.append({'x' : x, 'y': y})    # Add current (x,y) to list


def main(argv):
    numPoints = 3 # Number of points expecting from the user
    points = []   # List for storing the points

    img = cv2.imread(argv[1])
    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', getCoordinate, param = points)

    while(True):
        k = cv2.waitKey(20) & 0xFF

        # Check if $(numPoints) points are clicked by user
        # At any point of time, program will exit if <Esc> is pressed
        if k == 27 or len(points) == numPoints:
            for i, point in enumerate(points):
                print "Point %d : (%d, %d)" % (i + 1, point['x'], point['y'])
            break

    ##################################
    # Add the rest of your code here #
    ##################################

if __name__ == "__main__":
    main(sys.argv)
