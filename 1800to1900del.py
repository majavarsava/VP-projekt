import csv

file_path = "vizualizacija/national_names.csv"

# Read all rows except those from 1880 to 1899
with open(file_path, "r", newline="", encoding="utf-8") as csvfile:
    reader = list(csv.reader(csvfile))
    header = reader[0]
    rows = [row for row in reader[1:] if not (1880 <= int(row[3]) <= 1899)]

# Overwrite the original file with filtered rows
with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)