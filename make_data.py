import csv
import random

random.seed(42)          # 固定随机种子，保证每次生成的数据一样

categories = ["电子", "食品", "服饰"]
rows = []
for i in range(1, 21):
    rows.append([
        f"商品{i:02d}",
        random.choice(categories),
        round(random.uniform(10, 500), 2),
        random.randint(1, 100),
    ])

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "category", "price", "sales"])
    writer.writerows(rows)

print(f"已生成 data.csv，共 {len(rows)} 行数据")