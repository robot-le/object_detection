# Object Detection

Django REST framework API for object detection. Model trained on [COCO dataset](https://cocodataset.org/).

## How to use

1. Clone the repository:
~~~
git clone https://github.com/robot-le/object_detection.git
~~~
2. Build a docker image:
~~~
docker build . --tag object_detection
~~~
3. Run the container:
~~~
docker run -p 8084:8000 object_detection
~~~
4. Send a request with such tools as Postman or Insomnia, or send it from a terminal with curl:
~~~
curl --location 'http://localhost:8084/api/detect-objects/' --form 'image=@"<path_to_your_image>"'
~~~

## Example:

![dog](https://github.com/robot-le/object_detection/assets/86671798/87d63414-5b40-4fff-8194-9e49f3c48747)

In Postman send POST request with this photo in body as form-data:

![Screenshot from 2024-05-14 20-12-13](https://github.com/robot-le/object_detection/assets/86671798/bbbb7814-88ab-47bc-9976-917ff9b06951)

In response you'll get an object with a list of detected objects with label, confidence, and bounding box coordinates:
~~~
{
    "detected_objects": [
        {
            "label": "dog",
            "confidence": 0.9979016780853271,
            "box": {
                "a": 122,
                "b": 223,
                "c": 320,
                "d": 543
            }
        },
        {
            "label": "bicycle",
            "confidence": 0.9900935292243958,
            "box": {
                "a": 117,
                "b": 124,
                "c": 569,
                "d": 432
            }
        },
        {
            "label": "truck",
            "confidence": 0.9370242357254028,
            "box": {
                "a": 472,
                "b": 86,
                "c": 692,
                "d": 166
            }
        }
    ]
}
~~~
