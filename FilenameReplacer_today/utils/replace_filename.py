# 目的：任意のフォルダ内にあるファイル名に含まれる「日付部分」を一括で「TODAY」に置き換えたい。
# target_files フォルダ内の全ファイルを対象に、正規表現で日付部分を検出し、「TODAY」に置換してリネームを実行するバッチ処理。
# ファイルパスはループ処理で取得し、os.rename による更新を行う。重複や衝突発生時は例外処理でハンドリング。
import os, re
from pathlib import Path
from datetime import datetime


# target_filesフォルダ内のファイル名一覧を取得する
current_folder = Path(__file__).parent
target_folder = os.path.join(current_folder.parent, 'target_files')
files = os.listdir(target_folder)


# 各ファイル名から日付部分を抽出し、フォーマットを維持したまま今日の日付へ変更
# 日付フォーマット全パターンをコンパイル(それぞれグループ名を付ける)
date_pattern = re.compile(
    r"(?P<dash4>\d{4}-\d{2}-\d{2})|"      # yyyy-mm-dd
    r"(?P<underscore4>\d{4}_\d{2}_\d{2})|"# yyyy_mm_dd
    r"(?P<plain4>\d{8})|"                 # yyyymmdd
    r"(?P<dash2>\d{2}-\d{2}-\d{2})|"      # yy-mm-dd
    r"(?P<underscore2>\d{2}_\d{2}_\d{2})|"# yy_mm_dd
    r"(?P<plain2>\d{6})"                  # yymmdd
)
# todayの各フォーマット版を用意(nameをフォーマット名で一致させる)
today = datetime.today()
today_str = {
    "dash4": today.strftime("%Y-%m-%d"),        # yyyy-mm-dd
    "underscore4": today.strftime("%Y_%m_%d"),  # yyyy_mm_dd
    "plain4": today.strftime("%Y%m%d"),         # yyyymmdd
    "dash2": today.strftime("%y-%m-%d"),        # yy-mm-dd
    "underscore2": today.strftime("%y_%m_%d"),  # yy_mm_dd
    "plain2": today.strftime("%y%m%d"),         # yymmdd
}

def replace_with_today(match):
    for name, value in match.groupdict().items():
            if value:
                return today_str[name]
    return match.group()

for file in files:
    new = date_pattern.sub(replace_with_today, file)
    new_filename = ''

    old_filename = os.path.join(target_folder, file)
    new_filename = os.path.join(target_folder, new)

    print(f"{old_filename} → {new_filename}")
    os.rename(old_filename, new_filename)