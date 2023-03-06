# UUM2023 Better Style

## このアプリの目的

簡単マラソン計測システム [K-SOK](http://www.co-runners.co.jp/k-sok/)の[レース結果・計測速報ページ](http://www.k-sok.com/corunners/welcome)の表示内容が

- PC画面でのみの最適化でスマホでは非常に読みにくい
- レース管理側として知りたい情報が不足している
  - チェックポイント（通称：関門）通過状況
  - コース上に選手があと何人残っているか
  - コース上に残っている選手のゼッケン番号（アスリートビブス番号）

という欠点があり、これを解消するために

- スマホ表示対応
- チェックポイント間に存在するランナーの人数を固定表示
- 選手名、ビブス番号、最終通過チェックポイント以外の情報を非表示

することでスマホでのレース管理を行いやすくする。

## 技術情報

- Python Flask使用
- Herokuデプロイ対応
  - GUnicorn使用
- BeautifullSoup4使用
  - 対象レースの計測データサイトをスクレイピングするため

## 利用方法の簡易説明

### スクレイピング機能

スクレイピング対象レースは[app/scrp.py](app/scrp.py)にリテラルで埋め込んでいる。

再利用する場合は適宜URLやチェックポイントの情報を書き換えて利用する。基本的にコアの内容はscrp.pyの修正だけで済むはず。

### レース選択

ウルトラうどんマラニック2023中讃スペシャルは２日間にわたって実施したため、Day1とDay2でルーティングを分けている。
また、2日間参加の部(フル)と1日だけの参加（ハーフ1日目、ハーフ2日目）で計測サイトが別々なので双方の結果を合算している。

## 特記事項

1日目レース終了後に3時間くらいの時間で突貫で作ったため粗が多い。今後も使用する場合はブラッシュアップ必須。

デプロイしたHerokuへのリンク：https://uum2023-better-result.herokuapp.com/ （必要時以外閉鎖中）