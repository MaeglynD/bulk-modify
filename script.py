import datetime
import os
import time

def set_file_last_modified(file_path, dt):
    dt_epoch = dt.timestamp()
    os.utime(file_path, (dt_epoch, dt_epoch))

dirPath = list(map(lambda x: [x, os.listdir(x)], [
    # list of file paths e.g. 'C:/some/path/'
]))

for i in range(max(list(map(lambda x: len(x[1]), dirPath)))):
    stack = []    

    now = datetime.datetime.now()
    time.sleep(2)

    for baseDir, files in dirPath:
        if len(files) > i:
            stack.append(baseDir + files[i])

    print(f'Current iteration {i}, current stack is: ')
    print(stack)

    for item in stack:
        set_file_last_modified(item, now)