import numpy as np
import cv2
from matplotlib import pyplot as plt
import os

# 読み込み
dirs = os.listdir("C:\\workspace_app\\penguin_checker\\img\\color_dataset")


for dir in dirs:
    # 元画像のタグ別フォルダ
    color_dir = os.path.join("C:\\workspace_app\\penguin_checker\\img\\color_dataset", dir)
    # img/gray_dataset配下にタグごとのフォルダを作成
    gray_dir = os.path.join("C:\\workspace_app\\penguin_checker\\img\\gray_dataset", dir)
    os.makedirs(gray_dir)

    # 作成したフォルダ配下にグレースケールした画像を保存
    for curDir, dirs, files in os.walk(color_dir):
        count = 0

        
        for f in files:
            try:
                # 元画像読み込み
                img_bgr_path = os.path.join(curDir, f)
                img_bgr = cv2.imread(img_bgr_path)

                # グレースケール
                img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
                # 300*300にリサイズ
                img_gray = cv2.resize(img_gray, dsize=(300, 300))
                # 上下反転、左右反転、上下左右反転
                img_gray_ud = cv2.flip(img_gray, 0)
                img_gray_lr = cv2.flip(img_gray, 1)
                img_gray_udlr = cv2.flip(img_gray, -1)
                # 保存
                cv2.imwrite(os.path.join(gray_dir, str(count).zfill(4) + ".jpg"), img_gray)
                cv2.imwrite(os.path.join(gray_dir, str(count).zfill(4) + "_ud.jpg"), img_gray_ud)
                cv2.imwrite(os.path.join(gray_dir, str(count).zfill(4) + "_lr.jpg"), img_gray_lr)
                cv2.imwrite(os.path.join(gray_dir, str(count).zfill(4) + "_udlr.jpg"), img_gray_udlr)

                count = count + 1
            except Exception as e:
                print(e)
                print("failed:", f)
                continue
        
        print("successes:", dir, count)


        
    
