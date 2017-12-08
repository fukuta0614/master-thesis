# 東京大学 大学院情報理工学系研究科 創造情報専攻 修士論文テンプレート

[創造情報学専攻が配布しているテンプレート][template]を整理したものです

## 使い方

### ファイルを変更する度に自動でビルドする

```sh
$ make
```

- Preview.appだとpdfに変更があっても更新してくれないのでSkim.appがおすすめ
- 句読点。や半角カンマ、ピリオドは自動で全角カンマ、ピリオド．になります

### ビルドするだけ

```sh
$ make build
```

### ゴミファイルを消す

```sh
$ make clean
```

[template]: http://www.ci.i.u-tokyo.ac.jp/2016/mtstyle/index.html