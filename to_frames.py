import cv2
# vidcap = cv2.VideoCapture('big_buck_bunny_720p_5mb.mp4')
vidcap = cv2.VideoCapture('qr_scroll2.mp4')
success,image = vidcap.read()
count = 0
print(image.shape[0] - 300)
while success:
  cv2.imwrite("frames/frame%d.jpg" % count, image[100:image.shape[0] - 30][0:])     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
