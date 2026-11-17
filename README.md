# AR-Gallery

体育館の壁に貼ったQRコードを読むと、小学生の3D作品がARで見られる展示サイト。

## 公開URL

https://superyossy.github.io/ar-gallery/

- 作品一覧: `index.html`
- AR表示: `viewer.html?id=w01` のようにIDを指定

## 作品を追加する手順

1. BlenderからGLB形式で書き出す（Draco圧縮オン、5MB以内目安）
2. `models/` に `w03.glb` のようなID名で入れる
3. `works.json` に1行追加する
4. コミットしてpushする（反映まで1〜2分）
5. `python tools/make_qr.py` でQRコードを再生成する
   - 出力先は `../AR-Gallery-Works/qr/`

## ルール

- IDは `w01`〜 のゼロ埋め半角英数字・小文字
- GLBファイル名と works.json のキーを一致させる
- 元の .blend ファイルはこのリポジトリに入れない（AR-Gallery-Works で管理）
