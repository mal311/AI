import cv2
import mediapipe as mp
import pyautogui
import time
from math import hypot

# ==============================

# Configuration Parameters

# ==============================

# Scroll speed can be adjusted as per requirement
SCROLL_SPEED = 300 # Positive value for scroll up, negative for scroll down

# Delay between consecutive scroll actions to prevent rapid scrolling
SCROLL_DELAY = 1 # in seconds

# Camera settings
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

# ==============================

# Initialize MediaPipe Hands

# ==============================

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, # Maximum number of hands to detect
        min_detection_confidence=0.7,min_tracking_confidence=0.7)

mp_draw = mp.solutions.drawing_utils

# ==============================

# Gesture Detection Function

# ==============================

def detect_gesture(hand_landmarks, handedness):
    """

    Detects whether the hand gesture is an open palm or a closed fist.


    Args:

    hand_landmarks: The landmarks of the detected hand.

    handedness: 'Left' or 'Right' hand.



    Returns:

    A string indicating the gesture: "scroll_up", "scroll_down", or "none".

    """

    # List to hold the status of each finger (1: up, 0: down)
    fingers = []

    # Define finger tip landmarks
    finger_tips_ids = [mp_hands.HandLandmark.INDEX_FINGER_TIP,
                       mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
                       mp_hands.HandLandmark.RING_FINGER_TIP,
                       mp_hands.HandLandmark.PINKY_TIP
                        ]

    # Retrieve necessary landmarks
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    thumb_ip  = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP]
    wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]

    # Check each finger (except thumb) to see if it's up
    for tip_id in finger_tips_ids:
        finger_tip = hand_landmarks.landmark[tip_id]
        finger_pip = hand_landmarks.landmark[tip_id - 2]# PIP joint

        if finger_tip.y < finger_pip.y:
            fingers.append(1) #Finger is up
        else:
            fingers.append(0) # Finger is down

    # Check if thumb is open
    if handedness == 'Right':
         # Thumb is open
         # Thumb is closed

    else:
         # Thumb is open
        else:
             # Thumb is closed

    # Total number of fingers up
    

    # Determine gesture based on number of fingers up
    if total_fingers == 5:
        
    elif total_fingers == 0:
        
    else:
        



# ==============================

# Main Function

# ==============================

def main():
    # Initialize webcam
    

    if not cap.isOpened():
        
        return

     # Previous time for FPS calculation
     # Timestamp of the last scroll action

    

    while True:
        

         # Flip the image for a mirror effect
        

        gesture = "none"
        handedness = "Unknown"



        if results.multi_hand_landmarks and results.multi_handedness:

            for hand_landmarks, hand_info in zip(results.multi_hand_landmarks, results.multi_handedness):

                # Get hand label (Left/Right)
                

                # Draw hand landmarks on the image
                mp_draw.draw_landmarks(
                                        )



                # Detect the gesture
                gesture = detect_gesture(hand_landmarks, handedness)

                # Get current time
                current_time = time.time()

                # Perform scrolling action based on gesture with delay
                if gesture == "scroll_up" and (current_time - last_scroll_time) > SCROLL_DELAY:
                     # Scroll up
                    last_scroll_time = 

                elif gesture == "scroll_down" and (current_time - last_scroll_time) > SCROLL_DELAY:
                     # Scroll down
                    last_scroll_time = 



        # Calculate Frames Per Second (FPS)
        cTime = time.time()
        fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
        pTime = cTime



        # Display gesture and FPS on the image
        

        # Show the image
        cv2.imshow("Hand Gesture Scroll Control", img)



        # Exit the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

