import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

dirs = os.listdir("C:\\workspace_app\\penguin_checker\\img\\color_dataset")


for dir_p in dirs:
    gray_dir = os.path.join("C:\\workspace_app\\penguin_checker\\img\\gray_dataset", dir_p)


    for curDir, dirs, files in os.walk(gray_dir):
        count = 0
        
        for f in files:
            try:
                # 元画像読み込み
                img_path = os.path.join(curDir, f)
                img_gray = cv2.imread(img_path)
                img_gray = cv2.cvtColor(img_gray, cv2.COLOR_BGR2GRAY)
                # 300*300にリサイズ
                img_gray = cv2.resize(img_gray, dsize=(200, 200))
                # 保存
                cv2.imwrite(os.path.join(gray_dir, str(count).zfill(4) + ".jpg"), img_gray)

                count = count + 1
                print("successes:", dir_p, f)
            except Exception as e:
                print(e)
                print("failed:", f)
                continue
        
        print("successes:", dir, count)