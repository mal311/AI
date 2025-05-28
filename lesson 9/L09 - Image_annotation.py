import cv2
import matplotlib.pyplot as plt

# Step 1: Load the Image
image_path ="lesson 9/example.jpg"  # User-provided image path
image = cv2.imread(image_path)

# Convert BGR to RGB for correct color display with matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Get image dimensions
height, width, _ = image_rgb.shape

# Step 2: Draw Two Rectangles Around Interesting Regions
# Rectangle 1: Top-left corner
rect1_width, rect1_height = 150, 150
top_left1 = (20,20)  # Fixed 20 pixels padding from top-left
bottom_right1 = (top_left1[0] +rect1_width , top_left1[1] + rect1_height)
cv2.rectangle(image_rgb, top_left1, bottom_right1, (0, 0, 0), 3) # black rectangle

# Rectangle 2: Bottom-right corner
rect2_width, rect2_height = 200, 150
top_left2 = (width - rect2_width - 20, height - rect1_height - 20) # 20 pixels padding
bottom_right2 = (top_left2[0] + rect2_width, top_left2[1] + rect1_height)
cv2.rectangle(image_rgb, top_left2, bottom_right2, (255, 0, 255)3)  # Magenta rectangle

# Step 3: Draw Circles at the Centers of Both Rectangles
center1_x = top_left1[0] + rect1_width // 2
center1_y = top_left1[1] + rect1_height // 2

center2_x = top_left2[0] + rect2_width // 2
center2_y = top_left2[1] + rect2_height // 2

cv2.circle(image_rgb (center1_x, center1_y), 15, (0, 255, 0), -1)   # Filled green circle
cv2.circle(image_rgb (center2_x, center2_y),15, (0, 0, 255) -1)  # Filled blue circle

# Step 4: Draw Connecting Lines Between Centers of Rectangles
cv2.line(image_rgb, (center1_x, center1_y), (center2_x, center2_y), (0, 255, 0), 3)

# Step 5: Add Text Labels for Regions and Centers
font = cv2.FONT_HERSHEY_COMPLEX
cv2.putText(image_rgb, 'Region1', (top_left1[0], top_left1[1] - 10), font , 0.7, (0, 255, 255), 2, cv2.LINE_AA)
cv2.putText(image_rgb, 'Region2', (top_left2[0], top_left2[1] - 10), font , 0.7, (0, 255, 255), 2, cv2.LINE_AA)

cv2.putText(image_rgb, 'Center 1')
# Step 6: Add Bi-Directional Arrow Representing Height
  # Start near the top-right
  # End near the bottom-right

# Draw arrows in both directions
  # Downward arrow
 # Upward arrow

# Annotate the height value


# Step 7: Display the Annotated Image
