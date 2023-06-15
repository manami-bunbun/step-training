
How to run visualizer

```
python -m http.server
```
ans access to [http://localhost:8000/visualizer/build/default/](http://localhost:8000/visualizer/build/default/).


## New files

- output_generator.py

- solver_kruskal.py
  
  -[参考にした記事](https://qiita.com/flowerrr__lily/items/6679f9496d0079fa0dd2#%E3%82%AF%E3%83%A9%E3%82%B9%E3%82%AB%E3%83%AB%E6%B3%95)
 
## モチベーション

調べてみたところの理解では、

1. 初期経路探索 : **greedy** or **kruskal** or **prim**　
2. 最適化の組み合わせ : 2/3 opt / 焼きなまし法 / 距離重みづけ

のステップで行うと良いのかなと思いました。

先週体調不良で欠席した関係上、あまり実装の時間を取れなかったことと、MSTを見つけるアルゴリズムのコードに興味があったので今回kruskal法を用いました。
 　

