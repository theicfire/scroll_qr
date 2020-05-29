The point of this code is to measure scroll smoothness.

# Running
I have forgotten a bit about how all this works but here's a brain dump:

To get `get_qr_locs.py` working:
- `pip3 install opencv-python`
- `pip3 install zbar-py`
- `pip3 install plotly`
	- Maybe: `pip install plotly==4.2.1`
- `pip3 install pandas`
- `python3 get_qr_locs.py`

To add some qr codes to a webpage and make the page bounce up and down:
- Place the contents of `place_image.js` in the developers tools console
- Run `bounce_scroll()`

# Graphing
I'm not sure how to generate the graphs, but they look something like this: https://www.dropbox.com/s/ut6zy7set1d20p3/Screenshot%202020-05-29%2010.34.00.png?dl=0

