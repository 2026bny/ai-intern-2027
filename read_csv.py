import csv

with open("data.csv", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)

    header = next(reader)          # 第一行是表头，单独取出来
    print("表头:", header)

    total = 0
    for i, row in enumerate(reader, start=1):
        total = i
        if i <= 5:                 # 只看前 5 行
            print(f"第 {i} 行:", row)

print(f"共 {total} 行数据")