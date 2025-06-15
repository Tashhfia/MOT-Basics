import numpy as np
from pathlib import Path
import cv2



def iou(a, b):
    
    """ Takes in boxes(x1, y1, x2, y2) and returns IOU score"""

    x1_a, y1_a, x2_a, y2_a = a
    x1_b, y1_b, x2_b, y2_b = b
    
    # left point of intersection
    xl_inter = max(x1_a, x1_b)
    yl_inter = max(y1_a, y1_b)

    # right point of intersection
    xr_inter = min(x2_a,x2_b) 
    yr_inter = min(y2_a, y2_b)

    inter_w = max(0, xr_inter - xl_inter)
    inter_h = max(0, yr_inter - yl_inter)

    a_w = x2_a - x1_a
    b_w = x2_b - x1_b
    a_h = y2_a - y1_a
    b_h = y2_b - y1_b

    inter = inter_h * inter_w

    union = (a_w * a_h) + (b_h * b_w) - inter

    if union == 0:
        return 0 

    return inter / union


