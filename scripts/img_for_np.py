import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
import os

images_dir = "C:\\workspace_app\\penguin_checker\\img\\gray_dataset"
labels = os.listdir(images_dir)
X = []
y = []

for i, label in enumerate(labels):
    dir_name = os.path.join(images_dir, label)
    for curDir, dirs, files in os.walk(dir_name):
        for f in files:
            image = Image.open(os.path.join(curDir, f))
            # 画像データを配列に変換
            image = np.asarray(image)
            X.append(image)
            y.append(i)

# numpy配列に変換
X = np.array(X)
y = np.array(y)
print(X.shape)
# 3次元配列→2次元配列への変換
X = X.reshape(len(X), -1).astype(np.float64)
print(X.shape)
# 学習データとテストデータに分ける
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# 圧縮してファイルに出力
np.savez_compressed(
    "penguins.npz", 
    X_train=X_train, 
    X_test=X_test, 
    y_train=y_train, 
    y_test=y_test
    )
