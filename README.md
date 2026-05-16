# Face Mask Detection Using Deep Learning

## Overview

This project is a real-time Face Mask Detection System developed using Deep Learning, TensorFlow, OpenCV, and MobileNetV2. The system detects human faces through a webcam and classifies them as wearing a mask or not wearing a mask.

Initially, a CNN model was built from scratch, but the project was later improved using transfer learning with MobileNetV2, resulting in significantly better accuracy and real-time performance.

The final model achieved an accuracy of 98.9% after improving the dataset with more real-world variations.

---

## Features

* Real-time face mask detection
* Webcam integration using OpenCV
* Face detection using Haar Cascade
* Deep learning image classification
* Transfer learning using MobileNetV2
* Mask / No Mask classification
* Real-time prediction display
* Improved dataset handling for real-world scenarios

---

## Technologies Used

* Python
* TensorFlow
* Keras
* OpenCV
* NumPy
* MobileNetV2
* Haar Cascade Classifier

---

## Model Performance

| Model                  | Accuracy |
| ---------------------- | -------- |
| CNN From Scratch       | 95%      |
| MobileNetV2            | 98%      |
| Improved Dataset Model | 98.9%    |

---

## Dataset

Two Kaggle datasets were used for training and testing the model.

### Dataset 1 — Face Mask Dataset

* Total images: 7553
* With mask: 3725
* Without mask: 3828

Dataset Link:

```text id="u8m3pl"
https://www.kaggle.com/datasets/omkargurav/face-mask-dataset
```

### Dataset 2 — Face Data for Mask Classification

Includes:

* Correct mask
* Incorrect mask
* No mask
* Real-world variations
* Different lighting conditions
* Hands or objects covering faces

Dataset Link:

```text id="r5x1qw"
https://www.kaggle.com/datasets/adsawe/face-data-for-mask-classification/data
```

---

## Project Structure

```bash id="t9n4vk"
Face-Mask-Detection-Using-Deep-Learning/
│
├── README.md
├── LICENSE
├── .gitignore
│
├── app.py
├── train_model.py
├── detect_mask.py
├── mask_detector.model
├── haarcascade_frontalface_default.xml
├── requirements.txt
│
├── dataset/
│   ├── with_mask/
│   ├── without_mask/
│   └── additional_data/
│
├── static/
│
├── screenshots/
│
└── models/
```

---

## How to Run the Project

1. Install Python

2. Install required libraries:

```bash id="c2v7mn"
pip install tensorflow opencv-python numpy matplotlib
```

3. Put all project files in the same folder.

4. Run the detection system:

```bash id="k8r1ql"
python detect_mask.py
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

Additional images were added for:

* Incorrect mask usage
* Hands covering faces
* Real-world edge cases

This improved real-time prediction reliability.

---

## Challenges

* Face detection accuracy
* Real-world lighting variations
* Hand/object misclassification
* Dataset diversity limitations
* Real-time optimization

---

## Future Improvements

* Cloud deployment
* Mobile application integration
* Better UI/UX
* Multi-face tracking
* Medical safety analytics
* Performance optimization

---

## Author

Tarek Rajab

---

## License

This project is licensed under the MIT License.
