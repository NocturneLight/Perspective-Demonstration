import sys
import cv2
import numpy as np

def main(args):
    # Create variables here.
    imageName = args[1]
    f = float(args[2]) if float(args[2]) < -255 or float(args[2]) > 255 else 1
    u0 = float(args[3])
    v0 = float(args[4])
    a = float(args[5])
    b = float(args[6])
    c = float(args[7])
    

    # Load in the image.
    image = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)

    # Get our width and height.
    height, width = image.shape[:2]

    # Get our offset for centering the image.
    offsetX = width / 2
    offsetY = height / 2

    # Get the four corner values.
    tl = calculateXY(f, 0, 0, u0 + offsetX, v0 + offsetY, a, b, c)
    tr = calculateXY(f, width, 0, u0 + offsetX, v0 + offsetY, a, b, c)
    br = calculateXY(f, width, height, u0 + offsetX, v0 + offsetY, a, b, c)
    bl = calculateXY(f, 0, height, u0 + offsetX, v0 + offsetY, a, b, c)

    # Create an array with the corner values.
    corners = np.float32([tl, tr, br, bl])

    # Create an array containing the dimensions of the image. The image will
    # warp with respect to the image dimensions. 
    pixelCorners = np.float32([[0, 0], [width, 0], [width, height], [0, height]])

    # Use the getPerspective() function to get a matrix for
    # applying the warp to the image. 
    matrix = cv2.getPerspectiveTransform(pixelCorners, corners)

    # Apply the warp to the image.
    warpImage = cv2.warpPerspective(image, matrix, (width, height))

    # Show the original image and the warped image for comparison.
    cv2.imshow("Original", image)
    cv2.imshow("Warped", warpImage)

    # Press any key to exit.
    cv2.waitKey(0)


# Our functions go here.
def calculateXY(f, u, v, u0, v0, a, b, c):
    # Calculate X.
    _x = (c * (u - u0)) / (f - a * (u - u0) - b * (v - v0))

    # Calculate Y.
    _y = (c * (v - v0)) / (f - a * (u - u0) - b * (v - v0))

    # Return the newly calculated values. u0 and v0 added to x and y respectively to 
    # move the image along the x axis and y axis according to the user's choices.
    return (_x + u0, _y + v0)



# Run the main function if in the main file.
if __name__ == "__main__":
    main(sys.argv)
