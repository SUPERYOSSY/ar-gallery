# -*- coding: utf-8 -*-
# works.json を読んで、全作品分のQRコードPNGを一括生成する
# 使い方:
#   pip install "qrcode[pil]"
#   python tools/make_qr.py
# 出力先: ../AR-Gallery-Works/qr/
import json, os, qrcode

# ★公開後、自分のGitHub PagesのURLに書き換える
BASE = "https://USERNAME.github.io/REPONAME/viewer.html?id="

HERE = os.path.dirname(os.path.abspath(__file__))
WORKS = os.path.join(HERE, "..", "works.json")
OUT = os.path.join(HERE, "..", "..", "AR-Gallery-Works", "qr")
os.makedirs(OUT, exist_ok=True)

with open(WORKS, encoding="utf-8") as f:
    works = json.load(f)

for wid in works:
    img = qrcode.make(BASE + wid, box_size=12, border=4)
    path = os.path.join(OUT, f"qr_{wid}.png")
    img.save(path)
    print("done:", path)

print(f"\n{len(works)} 件のQRコードを生成しました")
