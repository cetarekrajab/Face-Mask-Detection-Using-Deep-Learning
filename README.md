# Face Mask Detection Using Deep Learning

## Overview

This project is a real-time Face Mask Detection System developed using Deep Learning, TensorFlow, OpenCV, and MobileNetV2. The system detects human faces through a webcam and classifies them as wearing a mask or not wearing a mask.

Initially, a CNN model was built from scratch, but the project was later improved using transfer learning with MobileNetV2, resulting in significantly better accuracy and real-time performance.

The final model achieved an accuracy of 98.9% after improving the training data with more real-world variations.

---

## Features

* Real-time face mask detection
* Webcam integration using OpenCV
* Deep learning image classification
* Transfer learning using MobileNetV2
* Mask / No Mask classification
* Real-time prediction display
* Improved real-world detection performance

---

## Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* MobileNetV2

---

## Model Performance

| Model            | Accuracy |
| ---------------- | -------- |
| CNN From Scratch | 95%      |
| MobileNetV2      | 98%      |
| Improved Model   | 98.9%    |

---

## Training Data Sources

```text id="m5q2vl"
https://www.kaggle.com/datasets/omkargurav/face-mask-dataset
```

```text id="u8r1xp"
https://www.kaggle.com/datasets/adsawe/face-data-for-mask-classification/data
```

---

## Project Structure

```bash id="k4v9tm"
Face-Mask-Detection-Using-Deep-Learning/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── app.py
├── train1.py
├── train2.py
├── train3.py
│
├── models/
│   ├── cnn_model.h5
│   ├── mobilenetv2_model.h5
│   └── improved_model.h5
│
└── screenshots/
```

---

## How to Run the Project

1. Install Python

2. Install required libraries:

```bash id="r2m7qw"
pip install tensorflow opencv-python numpy matplotlib
```

3. Put all project files in the same folder.

4. Run the camera detection system:

```bash id="v6x1kp"
python app.py
```

5. The webcam will open and start detecting:

* Mask
* No Mask

in real time.

---

## Methodology

### Data Preprocessing

* Image rescaling
* Train-validation split (80/20)

### CNN Model

* Conv2D
* MaxPooling
* Dense layers
* Dropout

### Transfer Learning

* MobileNetV2 pretrained model
* ImageNet weights
* Custom classification layers

### Final Improvements

Additional real-world images were added for:

* Incorrect mask usage
* Hands covering faces
* Different lighting conditions
* Real-world edge cases

This improved prediction reliability and real-time performance.

---

## Challenges

* Face detection accuracy
* Real-world lighting variations
* Hand/object misclassification
* Real-time optimization

---

## Future Improvements

* Cloud deployment
* Mobile application integration
* Better UI/UX
* Multi-face tracking
* Performance optimization

---

## Author

Tarek Rajab

---

## License

This project is licensed under the MIT License.
