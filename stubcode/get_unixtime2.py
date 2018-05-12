#!/usr/bin/env python3

import time
import os
import sys

print("[*] Current working directory: ", os.getcwd())
print("[*] Current scriptname: ", sys.argv[0])
current_time=int(time.time())


with open('/tmp/junk','a') as fh:
    fh.write("[*] current time: ")
    fh.write(str(current_time))
    fh.write("\n")

print('[*] Output 5 timestamps: ')
i=0
while i < 5:
    print(current_time)
    current_time += 10

    i += 1
