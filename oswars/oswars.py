import Image
import sys

with open(sys.argv[1]) as f:
    im = Image.open(f)
    im.show()