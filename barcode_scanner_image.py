import cv2
import zbar
import time
import os

def get_qr_locs(fpath):
    image = cv2.imread(fpath)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scanner = zbar.Scanner()
    start = time.time()
    results = scanner.scan(grayImage)
    if len(results) > 0:
        print(fpath, results[0].position[0][1])
    else:
        print(fpath, 'No qr code')

files = os.listdir('frames')
def compare_key(a):
    return int(a.split('.')[0].split('frame')[1])

files.sort(key = compare_key)
for fpath in files:
    get_qr_locs('frames/' + fpath)

