import os


sample_directory_path = './target_files'
sample_files_name = (
    'Report_2025-09-25.txt', 'Report_20250925.txt', 'Report_2025_09_25.txt', '2025-09-25_Report.docx',
    'Backup20250925.log', 'Data-250925.csv', 'Export_25-09-2025.xlsx', 'Report_25-09-25.txt',
    'Report_250925.txt', 'Report_25_09_25.txt', '25-09-25_Report.docx', 'Backup250925.log','Export_25-09-25.xlsx'
)

# ディレクトリ存在確認
if os.path.isdir(sample_directory_path):
    pass
else:
    # ディレクトリ作成
    os.makedirs(sample_directory_path)

# ファイル作成
for sample_file in sample_files_name:
    f = open(os.path.join(sample_directory_path,sample_file), 'w')
    f.close