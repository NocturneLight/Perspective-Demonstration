import sys
import cv2
import numpy as np

def main(args):
    # Create variables for image 1 here.
    imageName = args[1]
    f = 1
    u0 = 0
    v0 = 0
    a = -0.0008
    b = 0 
    c = float(args[2])


    # Load in the image.
    image1 = cv2.imread(imageName, cv2.IMREAD_UNCHANGED)

    # Get our width and height.
    height, width = image1.shape[:2]

    # Draw a vertical line on the image.
    cv2.line(image1, (round(width / 2), 0), (round(width / 2), height), (255, 255, 255), 2)

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
    warpImage = cv2.warpPerspective(image1, matrix, (width, height))

    # Show the original image and the warped image for comparison.
    cv2.imshow("Image 1", warpImage)



    # Adjust variables for image 2 here.
    a = 0
    b = 0.0008 # 0.001 Solution to image 2, this is.

    # Load in a new image.
    image2 = cv2.imread(imageName, cv2.IMREAD_UNCHANGED) 

    # Draw a horizontal line on the image.
    cv2.line(image2, (0, round(height / 2)), (width, round(height / 2)), (255, 255, 255), 2)

    # Get the four corner values.
    tl = calculateXY(f, 0, 0, u0 + offsetX, v0 + offsetY, a, b, c)
    tr = calculateXY(f, width, 0, u0 + offsetX, v0 + offsetY, a, b, c)
    br = calculateXY(f, width, height, u0 + offsetX, v0 + offsetY, a, b, c)
    bl = calculateXY(f, 0, height, u0 + offsetX, v0 + offsetY, a, b, c)

    # Create an array with the corner values.
    corners = np.float32([tl, tr, br, bl])

    # Use the getPerspective() function to get a matrix for
    # applying the warp to the image. 
    matrix = cv2.getPerspectiveTransform(pixelCorners, corners)

    # Apply the warp to the image.
    warpImage = cv2.warpPerspective(image2, matrix, (width, height))

    # Show the original image and the warped image for comparison.
    cv2.imshow("Image 2", warpImage)


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



# Run the program if this is the main file.
if __name__ == "__main__":
    main(sys.argv)