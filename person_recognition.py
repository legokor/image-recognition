from ultralytics import YOLO
import cv2
import math 
# start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# load pretrained YOLO modell weights (general purpose)
model = YOLO("yolo-Weights/yolov8n.pt")

# object classes (reduced to people detection only)
classNames = ["person"]

def check_confidence(box):
    # confidence
    confidence = math.ceil((box.conf[0]*100))/100
    print("Confidence --->",confidence)

while True:
    success, img = cap.read()
    results = model(img, stream=True)

    # coordinates
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # class name
            cls = int(box.cls[0])
            if cls == 0:  # Only process if the class is "person"
                # bounding box
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2) # convert to int values

                # put box in cam
                cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

                #check_confidence(box)

                # object details
                org = [x1, y1]
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 1
                color = (255, 0, 0)
                thickness = 2

                cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    # display webcam image
    cv2.imshow('Webcam', img)
    
    # exit
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()