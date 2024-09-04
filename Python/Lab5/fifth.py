# Given sets
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

# I. Join A and B (Union)
A_union_B = A.union(B)

# II. Find A intersection B
A_intersection_B = A.intersection(B)

# III. Is A subset of B
A_is_subset_of_B = A.issubset(B)

# IV. Are A and B disjoint sets
A_and_B_are_disjoint = A.isdisjoint(B)

# V. Join A with B and B with A (Union in both ways, which gives the same result)
A_join_B = A.union(B)
B_join_A = B.union(A)

# VI. What is the symmetric difference between A and B
A_symmetric_difference_B = A.symmetric_difference(B)

# VII. Delete the sets completely
del A
del B

# Output the results
print("Union of A and B:", A_union_B)
print("Intersection of A and B:", A_intersection_B)
print("Is A subset of B:", A_is_subset_of_B)
print("Are A and B disjoint:", A_and_B_are_disjoint)
print("Union of A with B:", A_join_B)
print("Union of B with A:", B_join_A)
print("Symmetric difference between A and B:", A_symmetric_difference_B)

# Trying to print A or B now will raise an error since they are deleted
