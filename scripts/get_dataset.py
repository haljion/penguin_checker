import sys
import os
from urllib import request
from PIL import Image

def download(url, decode=False):
    response = request.urlopen(url)
    if response.geturl() == "https://s.yimg.com/pw/images/en-us/photo_unavailable.png":
        # Flickr :This photo is no longer available image.
        raise Exception("This photo is no longer available image.")

    body = response.read()
    if decode == True:
        body = body.decode()
    return body

def write(path, img):
    file = open(path, 'wb')
    file.write(img)
    file.close()

# 参照 
# http://image-net.org/archive/words.txt
# http://www.image-net.org/explore?wnid=n01503061
classes = {"king":"n02056570", "adelie":"n02056228", "jackass":"n02057035", "rockhopper":"n02057330", "emperor":"n02056728"}

# 続きからダウンロードしたい場合はoffsetの値を変更する
offset = 0
# ダウンロード枚数上限
max = 2000

for dir, id in classes.items():
    print(dir)
    dir = os.path.join("C:\\workspace_app\\penguin_checker\\img", dir)

    os.makedirs(dir, exist_ok=True)
    urls = download("http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=" + id, decode=True).split()
    print("オフセット:", offset)
    print("枚数:", len(urls))
    i = 0
    for url in urls:
        if i < offset:
            i = i + 1
            continue
        if i > max:
            break

        try:
            file = os.path.split(url)[1]
            path = dir + "/" + file
            write(path, download(url))
            print("done:" + str(i) + ":" + file)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            print("error:" + str(i) + ":" + file)
        i = i + 1

print("end")