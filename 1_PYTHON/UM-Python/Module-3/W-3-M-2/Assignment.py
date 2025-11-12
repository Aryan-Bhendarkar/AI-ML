import re

handle_data = open('data.txt')
all_numbers = []

for line in handle_data:
    numbers = re.findall('[0-9]+', line)
    all_numbers.extend(numbers)

sum_all = 0
for num in all_numbers:
    sum_all = sum_all + int(num)

print(sum_all)


