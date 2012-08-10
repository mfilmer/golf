from __future__ import print_function
import itertools
import random
import string

random.seed(440)
count = int(''.join([random.choice(string.digits) for x in range(2)]))
map(print,itertools.repeat('Print this line',count))