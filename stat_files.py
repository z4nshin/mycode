import os
import sys
import stat
import time

def test(path):
    print path

def recurse_dir(root=".", callback=test, atime="14-01-1973"):
    day,month,year = atime.split("-")
    compareTime = list(time.gmtime())
    compareTime[0] = int(year)
    compareTime[1] = int(month)
    compareTime[2] = int(day)

    try:
        curDir = os.listdir(root)
    except:
        print "Error in accessing path:", root
        return
    for f in curDir:
        path = os.path.join(root, f)
        try:
            st = os.lstat(path)
        except:
            return
        mode = st[stat.ST_MODE]
        if stat.S_ISDIR(mode):
            recurse_dir(path, callback, atime)
        elif stat.S_ISREG(mode):
            if st[stat.ST_ATIME] < time.mktime(compareTime):
                callback(path)

if __name__ == "__main__":
    try:   
        if sys.argv[2]:
            recurse_dir(sys.argv[1], test, sys.argv[2])
    
    except:
        recurse_dir(sys.argv[1], test)

