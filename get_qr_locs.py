import cv2
import zbar
import time
import os
import plotly.express as px
UNKNOWN_Y_LOC = -9999



def read_and_process():
    vidcap = cv2.VideoCapture('qr_scroll2.mp4')
    success,image = vidcap.read()
    count = 0
    ret = {'x': [], 'diff': [], 'y_loc': []}
    prev_y_loc = UNKNOWN_Y_LOC
    while success:
        # cv2.imwrite("frames/frame%d.jpg" % count, image[100:image.shape[0] - 30][0:])     # save frame as JPEG file      
        fpath = "frames/frame%d.jpg" % count
        cv2.imwrite(fpath, image)
        success,image = vidcap.read()
        (prev_y_loc, diff) = get_qr_locs(fpath, prev_y_loc)
        bounded_y_loc = 0 if prev_y_loc == UNKNOWN_Y_LOC else prev_y_loc
        print("{}\t{}\t{}".format(fpath, bounded_y_loc, diff))
        ret['x'].append(count)
        ret['diff'].append(diff)
        ret['y_loc'].append(bounded_y_loc)
        count += 1
    return ret

def get_qr_locs(fpath, prev_y_loc):
    image = cv2.imread(fpath)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    scanner = zbar.Scanner()
    start = time.time()
    results = scanner.scan(grayImage)
    if len(results) > 0:
        y_loc = results[0].position[0][1]
        diff = 0
        if prev_y_loc != UNKNOWN_Y_LOC:
            diff = prev_y_loc - y_loc
        # print("{}\t{}\t{}".format(fpath, y_loc, diff))
        return (y_loc, diff)
    else:
        # print("{}\t{}\t{}".format(fpath, 0, 0))
        return (UNKNOWN_Y_LOC, 0)

# files = os.listdir('frames')
# def compare_key(a):
    # return int(a.split('.')[0].split('frame')[1])

# files.sort(key = compare_key)
# for fpath in files:
    # get_qr_locs('frames/' + fpath)

data = read_and_process()
fig = px.line(x=data['x'], y=data['y_loc'], title='y_loc')
fig.show()
fig = px.line(x=data['x'], y=data['diff'], title='y_loc diff')
fig.show()
