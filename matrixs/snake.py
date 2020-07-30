import numpy as np

def get_last_direction(ar):
    last_dir = ""
    dir = ["R","D","L","U"]
    rows, cols = len(ar), len(ar[0])
    r, c, index_dir = 0, -1, -1
    nextturn = stepsx = cols
    stepsy = rows-1
    inc_c, inc_r = 1, 0
    turns = 0
    for i in range(rows*cols):
        c += inc_c
        r += inc_r

        if i == nextturn-1:
            turns += 1
            index_dir += 1
            dir.append(dir[index_dir])
            last_dir = dir[index_dir]
            if turns%2==0:
                nextturn += stepsx
                stepsy -= 1
            else:
                nextturn += stepsy
                stepsx -= 1
            inc_c, inc_r = -inc_r, inc_c  
    return last_dir

results = []
tests = int(input("Input the number of matrixs: "))
for t in range(0, tests):
    rows = int(input("Input the number of rows for the matrix number {0}: ".format(str(t))))
    cols = int(input("Input the number of columns for the matrix number {0}: ".format(str(t))))
    ar = np.ones((rows,cols))
    results.append(get_last_direction(ar))

for r in results:
    print(r)