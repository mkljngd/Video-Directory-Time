import os, sys
import moviepy.editor


def splitall(path):
    allparts = []
    while 1:
        parts = os.path.split(path)
        if parts[0] == path:  # sentinel for absolute paths
            allparts.insert(0, parts[0])
            break
        elif parts[1] == path: # sentinel for relative paths
            allparts.insert(0, parts[1])
            break
        else:
            path = parts[0]
            allparts.insert(0, parts[1])
    return allparts
path = os.getcwd()
l = os.listdir(path)
folder = []
d = {}
#l.remove('.DS_Store')
for i in l:
    temp_path = os.path.join(path, i)
    if os.path.isdir(temp_path):
        folder.append(i)

paths = []
parent = []


def formats(seconds):
    h = seconds // 3600
    m = (seconds - h * 3600) // 60
    s = seconds % 60
    s = round(s, 1)
    return str(int(h)) + ' h ' + str(int(m)) + ' m ' + str(s) + ' s'


def folder_open(fpath, i, flag):
    if flag == 0:
        parent.append(i)
    npath = os.path.join(fpath, i)
    if os.path.isdir(npath):
        l = os.listdir(npath)
        for j in l:
            folder_open(npath, j, flag + 1)
    else:
        if(npath.find('.mp4') > 0 or npath.find('.mkv') > 0):
            paths.append(npath)


for i in folder:
    d[i] = 0
    folder_open(path, i, 0)

folder_dict = dict()
for i in paths:
    folder_dirs = splitall(i)
    for j in folder_dirs:
        if (j in parent and j not in folder_dict.keys()):
            print('Opened Folder:', j)
            folder_dict[j] = False
    try:
        video = moviepy.editor.VideoFileClip(i)
    except:
        continue
    for j in parent:
        if j in i:
            d[j]+= int(video.duration)
            # d[j]+=audio.info.length
sum=0
with open('lol.txt','w') as f:
    for k, v in d.items():
        print(k, formats(v),file = f)
        sum+=v
    print('Total Duration:',formats(sum),file = f)
