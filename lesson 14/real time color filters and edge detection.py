import cv2
#imprt numpy as np

def apply_color_filter(image, filter_type):
    """Apply the specified 
    color filter to the image"""

    #create a copy of the image to avoid modifying the original
    filtered_image = image.copy()

    if filter_type == "red tint":
        #remove blue and green channels for red tint
        filtered_image[:, :, 1]=0 #Green channel to 0
        filtered_image[:, :, 0]=0 # Blue channel to 0

    elif filter_type == "blue_tint":
        #remove green and red channels for blue tint
        filtered_image[:, :, 1]=0 #Green channel to 0
        filtered_image[:, :, 2]=0 # Red channel to 0
    
    elif filter_type == "green_tint":
        #remove blue and red channels for green tint
        filtered_image[:, :, 0]=0 #Blue channel to 0
        filtered_image[:, :, 2]=0 # Red channel to 0
    
    elif filter_type == "increase red":
        #Increase the intensity of the red channel
        filtered_image[:, :, 2] = cv2.add(filtered_image[:, :, 2], 50)#increase red channel by 50
    
    elif filter_type == "decrease blue":
        #Decrease the intensity of the blue channel
        filtered_image[:, :, 0] = cv2.subtract(filtered_image[:, :, 2], 50)# decrease blue channel by 50
    
    elif filter_type == "sobel":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        sobelx = cv2.sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
        sobely = cv2.sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

        combined_sobel = cv2.bitwise_or(sobelx.astype('uintB'), sobely.astype('uint8'))
        filtered_image = cv2.cvtColor(combined_sobel, cv2.COLOR_GRAY2BGR)

    elif filter_type == "canny":
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray_image, 100, 200)
    
    return filtered_image


#Load the image
image_path = "lesson 14/ example.jpg" #Provide your image path
image = cv2.imread(image_path)

if image is None :
    print("Error: Not found!")
else:
    filter_type = "original" #default filter type

print("Press the following keys to apply filters:")
print("r - Red Tint")
print("b - Blue Tint")
print("g - Green Tint")
print("i - Increase Red Intensity")
print("d - Decrease Blue Intensity")
print("s - sobel edge detection")
print("c - canny edge detection")
print("q - Quit")

while True:
    #Apply the selected filter
    filtered_image = apply_color_filter(image, filter_type)

    #Display the filtered image
    cv2.imshow("Filtered image", filtered_image)

    #Wait for key press
    key = cv2.waitkey(0)

    #Map key presses to filters
    if key == ord("r"):
        filter_type = "red_tint"
    elif key == ord ('b'):
        filter_type = "blue_tint"
    elif key == ord ('g'):
        filter_type = "green_tint"
    elif key == ord ('i'):
        filter_type = "increase_red"
    elif key == ord ('d'):
        filter_type = "decrease_blue"
    elif key == ord ('s'):
        filter_type = "sobel"
    elif key == ord ('c'):
        filter_type = "canny"
    elif key == ord ('q'):
        print("Exiting...")
        break
    else:
        print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', 's', 'c', or 'q'.")

    
    cv2.destroyAllWindows()
    