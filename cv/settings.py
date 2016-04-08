# Camera parameters
AWB_MODE = 'auto' # auto white balance
AWB_GAINS = (1.65, 1.45)
SATURATION = -35 # If too yellow/green adjust this
EXPOSURE_MODE = 'sports'
EXPOSURE_COMPENSATION = 10
SHUTTER = 35000 # 0.035 seconds (measured in microseconds)
VIDEO_STABALIZATION = True
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

# Thresholding parameters
BLUE_HSV_RANGE = [([20, 140, 220], [50, 190, 255])] #[([30, 30, 60], [80, 80, 90])]
YELLOW_HSV_RANGE = [([20, 140, 220], [50, 190, 255])]  #[([25, 230, 230], [50, 255, 255])]
HEIGHT_PADDING = int(CAMERA_HEIGHT/2.5)
WIDTH_PADDING = 0#int(CAMERA_WIDTH/4)

REGIONS_KEYS = ['middle'] # ['top', 'middle', 'bottom']