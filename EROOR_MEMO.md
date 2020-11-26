# Numpyのimport部分でランタイムエラー

## エラーログ
    RuntimeError: The current Numpy installation ('C:\\envs\\bird-env\\lib\\site-packages\\numpy\\__init__.py') fails to pass a sanity check due to a bug in the windows runtime. See this issue for more information: https://tinyurl.com/y3d

## 原因
Numpyバージョン 1.19.4の問題らしい

## 解決法
- バージョンを1.19.3に下げる
- https://qiita.com/bear_montblanc/items/b4b75dfd77da98076da5