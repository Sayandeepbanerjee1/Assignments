it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

length_it_companies = len(it_companies)

it_companies.add('Twitter')

# III. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Snapchat', 'LinkedIn', 'Tesla'])

# IV. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')  # You can choose any company to remove

# V. Difference between remove and discard
# 'remove' will raise a KeyError if the item is not found in the set
# 'discard' will not raise any error if the item is not found

# it_companies.remove('NonExistentCompany')  # This will raise a KeyError
it_companies.discard('NonExistentCompany')  # This will do nothing

# Output the results
print("Length of it_companies:", length_it_companies)
print("Updated it_companies:", it_companies)
