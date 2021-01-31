import cv2
import imageio
import numpy as np

def transform(file_path, output_path, to_ratio=16/9, blur=0, shadow_blur=0, shadow_opacity=1.0):
    # Open image
    input = imageio.imread(file_path)
    orig_height, orig_width, _ = input.shape

    # Initialize usefull variables
    if to_ratio < 1: # Vertical orientation
        horizontal = False
        width = orig_width
        height = width / to_ratio
        scaling = height / orig_height
    else: # Horizontal orientation
        horizontal = True
        height = orig_height
        width = height * to_ratio
        scaling = width / orig_width
    # Round width and height
    width = round(width)
    height = round(height)
    # Image position on the output
    x = (width - orig_width) // 2
    y = (height - orig_height) // 2

    # Apply background
    output = cv2.resize(input, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
    output = cv2.GaussianBlur(output, (0, 0), blur)

    # Create shadow
    shadow_mask = np.zeros(output.shape)
    shadow_mask[y:y+orig_height, x:x+orig_width, :] = shadow_opacity
    shadow_mask = cv2.GaussianBlur(shadow_mask, (0, 0), shadow_blur)

    # Apply shadow
    output = shadow_mask.astype(np.uint8) + np.multiply(output, (1 - shadow_mask)).astype(np.uint8)

    # Put image back in the center
    output[y:y+orig_height, x:x+orig_width, :] = input[:, :, :]

    # Export image
    imageio.imwrite(output_path, output)
