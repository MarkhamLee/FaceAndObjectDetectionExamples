from PIL import Image, ImageDraw
import numpy as np
import PIL
import PIL.Image 
from facenet_pytorch import MTCNN, InceptionResnetV1
import cv2
import torch


class ImageProcessing:

    def __init__(self):
        # this enables this class to run on GPU when available without having to update the code 
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')
        print('Running on device: {}'.format(self.device))

    # basic face detection and image cropping 
    # wrote this for photo comparison implementations based on TensorFlow or PyTorch 
    # to do: fine tune the parameters, these were just sample ones given in a tutorial
    def mtcnn_face_detection(self, image):
        self.image = image
        self.type = type 
        self.image_size = 160
        self.margin = 35
        self.min_face_size = 20
        self.thresholds = [0.6, 0.7, 0.7]
        self.factor = 0.709
        self.post_process = "True"
        self.type = type

        # instantiate MTCNN 
        mtcnn = MTCNN(
            self.image_size, self.margin, self.min_face_size,
            self. thresholds, self.factor, self.post_process,
            self.device)

        # read in image 
        img = Image.open(self.image) # uses PIL to readin the image 
        cropped_image = mtcnn(img)
        return cropped_image


    # face detection, image cropping and writing the processed image to a file 
    # wrote this for use batch processing or anything that will require an input file 
    # rather than a tensor 
    def mtcnn_processing(self, image, file_path):
        self.image = image
        self.type = type 
        self.image_size = 224
        self.margin = 35
        self.min_face_size = 20
        self.thresholds = [0.6, 0.7, 0.7]
        self.factor = 0.709
        self.post_process = "True"
        self.type = type
        self.file_path = file_path

        # instantiate MTCNN 
        mtcnn = MTCNN(
            self.image_size, self.margin, self.min_face_size,
            self. thresholds, self.factor, self.post_process,
            self.device)

        # read in image 
        img = Image.open(self.image)
        mtcnn(img, save_path = self.file_path)
        return self.file_path


    # this generates the embeddings, which can use for facial recognition models OR in matching scenarios
    # you can use them to calculate the "distance" between images for similarity calculations 
    def resnet_embeddings(self, cropped_image, type):
        self.cropped_image = cropped_image
        self.type = type

        # instantiate resnet using the pre-traiend vggface2 model 
        resnet = InceptionResnetV1(pretrained='vggface2', classify=True).eval().to(self.device)

        # determine whether to return a numpy array or a tensor 
        # type = 0 for numpy, else defaults to tensors
        if type == 0:
            return resnet(self.cropped_image.unsqueeze(0)).detach().numpy()
        else:
            return resnet(self.cropped_image.unsqueeze(0))


    # add OpenCV - SSD 


    # open CV preprocessing, 
    def openCV(self, image):
        face_cascade = cv2.CascadeClassifier('hcdata/haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('hcdata/haarcascade_eye.xml')
        
        self.image = image
        processed_image = cv2.imread(self.image)
        grey = cv2.cvtColor(processed_image, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(grey, 1.3, 5)
        
        return faces