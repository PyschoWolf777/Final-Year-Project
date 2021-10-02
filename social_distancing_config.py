# base path to YOLO directory
MODEL_PATH = "yolo-coco"

'''
Non Maximum Suppression (NMS) is a technique used in numerous computer vision tasks. 
It is a class of algorithms to select one entity (e.g., bounding boxes) out of many overlapping entities. 
We can choose the selection criteria to arrive at the desired results. The criteria are most commonly some 
form of probability number and some form of overlap measure (e.g. Intersection over Union).
'''

# initialize minimum probability to filter weak detections along with
# the threshold when applying non-maxima suppression
MIN_CONF = 0.3
NMS_THRESH = 0.3

# boolean indicating if NVIDIA CUDA GPU should be used
USE_GPU = False

# define the minimum safe distance (in pixels) that two people can be
# from each other
MIN_DISTANCE = 25