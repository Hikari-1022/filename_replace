Pythonの基礎を学ぶためのリポジトリ
業務委託依頼で依頼のあるやつを参考にスクリプト作成して学ぶ


◆FilenameReplacer_today
・概要
指定したフォルダ内にあるファイル名の「日付部分」を自動的に検出し、「TODAY」に一括置換するスクリプト

・目的
言語の理解とフォルダ・ファイル操作の基礎を学べる

・フォルダ構成
FilenameReplacer_today/
    ├── target_files/               # 対象ファイルを配置するフォルダ
    └── utils/
        ├── replace_filename.py     # ファイル名を置換するメインスクリプト
        └── create_sample_file.py   # サンプルファイルを自動生成するスクリプト

・実行フロー
1.サンプルファイル作成
テスト用に target_files にファイルを作る。
> python Python_practice/FilenameReplacer_today/utils/create_sample_file.py

2.ファイル名の日付部分を今日の日付へ置換
> python Python_practice/FilenameReplacer_today/utils/replace_filename.py

3.ファイル名が変わっていることを確認
以下フォルダ内を確認して完了!!
\GitHub\Python_practice\FilenameReplacer_today\target_files