import torch
import torchvision

print(torch.__version__, torch.cuda.is_available(), torch.version.cuda)
print(float(torchvision.__version__[:3]))
import numpy
import scipy
import PIL
import cv2
import matplotlib
import easydict
