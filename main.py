from transformer import transform

# Image parameters
file_path = 'images/test_1.jpg' # Input image
output_path = 'output.jpg' # Output image
to_ratio = 16/9 # The desired aspect ratio: width = height * to_ratio
                # If to_ratio > 1: the output image will be horizontal: the height is kept
                # If to_ratio < 1: the output image will be vertical: the width is kept

# Advanced parameters
blur = 30 # How much to blur the background
shadow_blur = 50 # How much to blur the shadow
shadow_opacity = 0.75

transform(
    file_path=file_path, output_path=output_path, to_ratio=to_ratio,
    blur=blur, shadow_blur=shadow_blur, shadow_opacity=shadow_opacity
)
