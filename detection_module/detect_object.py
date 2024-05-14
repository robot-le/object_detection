import os
import cv2
import numpy as np
from dotenv import load_dotenv
load_dotenv()

YOLO_DIR = os.getenv('YOLO_DIR')

with open(f'{YOLO_DIR}/yolov3_classes.txt', 'r') as f:
    classes = [line.strip() for line in f.readlines()]


def detect_objects(uploaded_image):
    image = cv2.imdecode(np.frombuffer(uploaded_image.read(), np.uint8), cv2.IMREAD_COLOR)

    width = image.shape[1]
    height = image.shape[0]
    scale = 0.00392

    net = cv2.dnn.readNet(
        f'{YOLO_DIR}/yolov3.weights',
        f'{YOLO_DIR}/yolov3.cfg',
    )
    blob = cv2.dnn.blobFromImage(image, scale, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)

    layer_names = net.getLayerNames()
    output_layers = [layer_names[i - 1] for i in net.getUnconnectedOutLayers()]
    outs = net.forward(output_layers)

    class_ids = []
    confidences = []
    boxes = []
    conf_threshold = 0.5
    nms_threshold = 0.4

    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
                x = center_x - w / 2
                y = center_y - h / 2
                class_ids.append(class_id)
                confidences.append(float(confidence))
                boxes.append([x, y, w, h])

    indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

    res = []

    for i in indices:
        box = boxes[i]

        res.append({
            'label': classes[class_ids[i]],
            'confidence': confidences[i],
            'box': {
                'a': round(box[0]),
                'b': round(box[1]),
                'c': round(box[0] + box[2]),
                'd': round(box[1] + box[3]),
            }
        })

    return res
