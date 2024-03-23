import cv2
import pandas as pd
from ultralytics import YOLO
from tracker import *

model = YOLO('yolov8s.pt')
def process_image(input_image_path):
    frame = cv2.imread(input_image_path)

    my_file = open("coco.txt", "r")
    data = my_file.read()
    class_list = data.split("\n")

    tracker1 = Tracker()
    tracker2 = Tracker()
    tracker4 = Tracker()
    tracker3 = Tracker()

    counter1 = []
    counter2 = []
    counter3 = []
    counter4 = []
    offset = 6

    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")

    # Get the count of results
    result_count = len(results[0].boxes.data)

    # Get the width of the image
    image_width = frame.shape[1]

    # Display the count on the image covering the entire width
    cv2.rectangle(frame, (10, 10), (image_width - 10, 50), (255, 255, 255), -1)
    cv2.putText(frame, f'TOTAL VEHICLES: {result_count}', (15, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Save the output image temporarily
    input_image_path=input_image_path
    output_image_path = 'static/uploads/' + 'processed_' + input_image_path.split("/")[-1]
    cv2.imwrite(output_image_path, frame)



    return input_image_path, output_image_path, result_count


