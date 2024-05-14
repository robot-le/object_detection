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

![8](https://github.com/robot-le/object_detection/assets/86671798/10055560-5d10-4880-892b-6e19d21b8d61)


In Postman send POST request with this photo in body as form-data:

![image](https://github.com/robot-le/object_detection/assets/86671798/4cac6771-536c-4f71-99bf-872d6ee221ec)


In response you'll get an object with a list of detected objects with label, confidence, and bounding box coordinates:
~~~
{
    "detected_objects": [
        {
            "label": "car",
            "confidence": 0.9929202198982239,
            "box": {
                "a": 70,
                "b": 344,
                "c": 266,
                "d": 394
            }
        },
        {
            "label": "person",
            "confidence": 0.9896812438964844,
            "box": {
                "a": 266,
                "b": 330,
                "c": 288,
                "d": 376
            }
        },
        {
            "label": "person",
            "confidence": 0.9634418487548828,
            "box": {
                "a": 295,
                "b": 332,
                "c": 311,
                "d": 376
            }
        },
        {
            "label": "person",
            "confidence": 0.9565578699111938,
            "box": {
                "a": 416,
                "b": 328,
                "c": 440,
                "d": 378
            }
        },
        {
            "label": "person",
            "confidence": 0.9295955300331116,
            "box": {
                "a": 588,
                "b": 326,
                "c": 620,
                "d": 380
            }
        },
        {
            "label": "person",
            "confidence": 0.9230886101722717,
            "box": {
                "a": 306,
                "b": 331,
                "c": 320,
                "d": 375
            }
        },
        {
            "label": "person",
            "confidence": 0.9230819344520569,
            "box": {
                "a": 625,
                "b": 326,
                "c": 639,
                "d": 368
            }
        },
        {
            "label": "traffic light",
            "confidence": 0.9148918390274048,
            "box": {
                "a": 20,
                "b": 163,
                "c": 44,
                "d": 201
            }
        },
        {
            "label": "person",
            "confidence": 0.9024598598480225,
            "box": {
                "a": 356,
                "b": 333,
                "c": 372,
                "d": 375
            }
        },
        {
            "label": "car",
            "confidence": 0.8786023855209351,
            "box": {
                "a": 371,
                "b": 334,
                "c": 401,
                "d": 354
            }
        },
        {
            "label": "person",
            "confidence": 0.8716214299201965,
            "box": {
                "a": 402,
                "b": 327,
                "c": 416,
                "d": 367
            }
        },
        {
            "label": "traffic light",
            "confidence": 0.8687766194343567,
            "box": {
                "a": 440,
                "b": 230,
                "c": 462,
                "d": 252
            }
        },
        {
            "label": "person",
            "confidence": 0.8665909171104431,
            "box": {
                "a": 473,
                "b": 330,
                "c": 495,
                "d": 374
            }
        },
        {
            "label": "traffic light",
            "confidence": 0.7571566700935364,
            "box": {
                "a": 454,
                "b": 232,
                "c": 466,
                "d": 250
            }
        },
        {
            "label": "traffic light",
            "confidence": 0.700567901134491,
            "box": {
                "a": 0,
                "b": 164,
                "c": 14,
                "d": 202
            }
        },
        {
            "label": "traffic light",
            "confidence": 0.558958888053894,
            "box": {
                "a": 248,
                "b": 300,
                "c": 254,
                "d": 308
            }
        },
        {
            "label": "person",
            "confidence": 0.5131950378417969,
            "box": {
                "a": 120,
                "b": 333,
                "c": 130,
                "d": 357
            }
        }
    ]
}
~~~
