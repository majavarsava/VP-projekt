import csv
from collections import defaultdict


input_file_state = "vizualizacija/state_names_full.csv"
input_file_national = "vizualizacija/national_names.csv"
output_file = "vizualizacija/counts.csv"

# Helper to accumulate counts
def accumulate_state_counts(reader):
    counts = defaultdict(lambda: {'boys': 0, 'girls': 0})
    for row in reader:
        year = int(row['Year'])
        place = row['State']
        gender = row['Gender']
        count = int(row['Count'])
        key = (place, year)
        if gender == 'M':
            counts[key]['boys'] += count
        elif gender == 'F':
            counts[key]['girls'] += count
    return counts

def accumulate_national_counts(reader):
    counts = defaultdict(lambda: {'boys': 0, 'girls': 0})
    for row in reader:
        year = int(row['Year'])
        gender = row['Gender']
        count = int(row['Count'])
        key = ('National', year)
        if gender == 'M':
            counts[key]['boys'] += count
        elif gender == 'F':
            counts[key]['girls'] += count
    return counts

# Read and accumulate state counts
with open(input_file_state, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    state_counts = accumulate_state_counts(reader)

# Read and accumulate national counts
with open(input_file_national, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    national_counts = accumulate_national_counts(reader)

# Write output
with open(output_file, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Place', 'Year', 'Count', 'Boys', 'Girls'])
    # Write national
    for (place, year), data in sorted(national_counts.items()):
        total = data['boys'] + data['girls']
        writer.writerow([place, year, total, data['boys'], data['girls']])
    # Write states
    for (place, year), data in sorted(state_counts.items()):
        total = data['boys'] + data['girls']
        writer.writerow([place, year, total, data['boys'], data['girls']])