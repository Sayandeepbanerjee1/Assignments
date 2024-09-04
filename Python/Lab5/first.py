ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_sorted = sorted(ages)
min_age = ages_sorted[0]
max_age = ages_sorted[-1]

ages_extended = ages_sorted + [min_age, max_age]

n = len(ages_extended)
if n % 2 == 0:
    median_age = (ages_extended[n//2 - 1] + ages_extended[n//2]) / 2
else:
    median_age = ages_extended[n//2]

average_age = sum(ages_extended) / n

age_range = max_age - min_age

min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)

print("Sorted list:", ages_sorted)
print("Min age:", min_age)
print("Max age:", max_age)
print("List after adding min and max age:", ages_extended)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
print("Difference between Min and Average:", min_average_diff)
print("Difference between Max and Average:", max_average_diff)
