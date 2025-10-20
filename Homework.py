import cv2
import numpy as np

def Colors_Filter(image, Filter_type):
    Filtered_Color = image.copy()
    if Filter_type == "red_tint":
        Filtered_Color[:,:,0]=0
        Filtered_Color[:,:,1]=0
    elif Filter_type == "blue_tint":
        Filtered_Color[:,:,1]=0
        Filtered_Color[:,:,2]=0
    elif Filter_type == "green_tint":
        Filtered_Color[:,:,0]=0
        Filtered_Color[:,:,2]=0
    elif Filter_type == "Increased_red":
        Filtered_Color[:,:,2]=cv2.add(Filtered_Color[:,:,2],50)
    elif Filter_type == "Decreased_blue":
        Filtered_Color[:,:,0]=cv2.subtract(Filtered_Color[:,:,0],50)
    elif Filtered_Color == "sobel":
        gray_image = cv2.cvtColor(filter_image,cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
        sobely = cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype("uint8"),sobely.astype("uint8"))
        filter_image = cv2.cvtColor(combined_sobel,cv2.COLOR_GRAY2BGR)
    elif Filtered_Color == "canny":
        gray_image = cv2.cvtColor(filter_image,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image,100,200)
        filter_image = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    return Filtered_Color
image = cv2.imread("flower.png")
if image is None:
    print("Image is not found.")
else:
    Filter_type = "original"
    while True:
        filter_image = Colors_Filter(image, Filter_type)
        cv2.imshow("Filter Image", filter_image)
        key = cv2.waitKey(0) & 0xFF
        if key == ord("r"):
            Filter_type = "red_tint"
        elif key == ord("b"):
            Filter_type = "blue_tint"
        elif key == ord("g"):
            Filter_type = "green_tint"
        elif key == ord("B"):
            Filter_type = "Decreased_blue"
        elif key == ord("R"):
            Filter_type = "Increased_red"
        elif key == ord("S"):
            Filter_type = "sobel"
        elif key == ord("C"):
            Filter_type = "canny"
        elif key == ord("Q"):
            break
        else:
            print("Invalid input.")
cv2.destroyAllWindows()

