import os.path
import cv2
from torch import cuda
from torch import nn
from os import path
import  albumentations as A
from albumentations.pytorch import ToTensorV2
IMAGE_SIZE = 80
scale = 1

DATASET_TRAIN_PATH = os.path.join("..", "..", "dataset", "train", "data_img")

DATASET_TEST_PATH = os.path.join("..", "..", "dataset", "dev", "data_img")

TRANSFORMS_TRAIN = A.Compose([
    #A.LongestMaxSize(max_size=int(IMAGE_SIZE * scale)),
    A.PadIfNeeded(
        min_height=int(IMAGE_SIZE * scale),
        min_width=int(IMAGE_SIZE * scale),
        border_mode=cv2.BORDER_CONSTANT,
    ),
    #A.RandomCrop(width=IMAGE_SIZE, height=IMAGE_SIZE),
    A.ColorJitter(brightness=0.6, contrast=0.6, saturation=0.6, hue=0.6, p=0.3),

    A.ShiftScaleRotate(rotate_limit=19, p=0.2, border_mode=cv2.BORDER_CONSTANT),


    A.HorizontalFlip(p=0.4),
    A.CLAHE(p=0.4),
    A.Posterize(p=0.4),
    A.ToGray(p=0.4),
    A.ChannelShuffle(p=0.05),
    A.Normalize(mean=[0, 0, 0], std=[1, 1, 1], max_pixel_value=255, ),
    ToTensorV2(),
])


TRANSFORMS_TEST =  A.Compose([
    #A.RandomBrightnessContrast(brightness_limit=0.3, contrast_limit=0.3, p=0.3),
    A.Normalize(
                std=[1,1,1],),
    ToTensorV2(),
])

DATASET_NUM_WORKERS = 2
NUM_EPOCHS = 1000
DEVICE = 'cuda' if cuda.is_available() else 'cpu'
BATCH_SIZE = 1
LOAD_CHECK_POINT = False
SAVE_CHECK_POINT = False
CHECK_POINT_PATH = path.join("..", "..", "models")
CHECK_POINT_NAME = "model_img.pth"
LEARNING_RATE = 1e-5
LOSS_FUNCTION = nn.MSELoss()