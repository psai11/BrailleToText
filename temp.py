from PIL import Image, ImageChops
# import numpy as np
# from skimage import img_as_float
# from sewar.full_ref import mse
# from image_similarity_measures.quality_metrics import rmse, ssim, sre

def equal(im1, im2):
    diff = ImageChops.difference(im1, im2).getbbox()
    print(diff)

im1 = Image.open("images/a.png")
im2 = Image.open("images/test3.png")
# im1.show()
print(equal(im1, im2))