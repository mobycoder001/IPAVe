#!/usr/bin/env python3

import time
current_time=int(time.time())

print('[*] Output 5 timestamps: ')
i=0
while i < 5:
    current_time += 10
    print(current_time)

    i += 1
