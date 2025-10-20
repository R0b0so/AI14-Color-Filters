import cv2

def apply_color(image, color_filter):
    filter_image = image.copy()
    if color_filter == "red_tint":
        filter_image[:,:,0] = 0 
        filter_image[:,:,1] = 0
    elif color_filter == "blue_tint":
        filter_image[:,:,2] = 0
        filter_image[:,:,1] = 0
    elif color_filter == "green_tint":
        filter_image[:,:,0] = 0
        filter_image[:,:,2] = 0
    elif color_filter == "sobel":
        gray_image = cv2.cvtColor(filter_image,cv2.COLOR_BGR2GRAY)
        sobelx = cv2.Sobel(gray_image,cv2.CV_64F,1,0,ksize=3)
        sobely = cv2.Sobel(gray_image,cv2.CV_64F,0,1,ksize=3)
        combined_sobel = cv2.bitwise_or(sobelx.astype("uint8"),sobely.astype("uint8"))
        filter_image = cv2.cvtColor(combined_sobel,cv2.COLOR_GRAY2BGR)
    elif color_filter == "canny":
        gray_image = cv2.cvtColor(filter_image,cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image,100,200)
        filter_image = cv2.cvtColor(edges,cv2.COLOR_GRAY2BGR)
    elif filter_type == "original":
        pass
    return filter_image
capture = cv2.VideoCapture(0)
filter_type = "original"
if not capture.isOpened():
    print("ERROR cannot open camera.")
    exit()
while True:
    ret,frame = capture.read()
    print(ret)
    if not ret:
        break
    filter_image = apply_color(frame,filter_type)
    cv2.imshow(filter_type,filter_image)
    print("Press the key (r) for a red tint. \n Press the key (b) for a blue tint. \n Press the key (g) for a green tint. \n Press the key (q) to quit the program.")
    key = cv2.waitKey(1) & 0xFF 
    if key == ord("r"):
        filter_type = "red_tint"
    elif key == ord("g"):
        filter_type = "green_tint"
    elif key == ord("b"): 
        filter_type = "blue_tint"
    elif key == ord("q"):
        break
    elif key == ord("s"):
        filter_type = "sobel"
    elif key == ord("c"):
        filter_type = "canny"
    else: 
        print("Invalid key press either R,G,B,S,C,Q")
capture.release()
cv2.destroyAllWindows()