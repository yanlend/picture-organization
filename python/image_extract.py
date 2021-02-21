# coding: utf-8
# Show a frame from the video
# WORK IN PROGRESS, better use FFMPEG directly
# - Paths are hardcoded
# - Image sizes are hardcoded

FFMPEG_BIN = "ffmpeg.exe" # on Windows
import subprocess as sp
command = [
		FFMPEG_BIN,
		'-i', r"C:\Users\Peter\Desktop\20130208020906.MTS",
        '-f', 'image2pipe',
        '-pix_fmt', 'rgb24', '-']
pipe = sp.Popen(command, stdout = sp.PIPE, bufsize=10**8)
import numpy as np
raw_image = pipe.stdout.read(420*360*3)
import numpy
# read 1 frame
raw_image = pipe.stdout.read(1440*1080*3)
image =  numpy.fromstring(raw_image, dtype='uint8')
image = image.reshape((1080,1440,3))
import matplotlib.pyplot as plt
plt.imshow(image)
plt.show()
