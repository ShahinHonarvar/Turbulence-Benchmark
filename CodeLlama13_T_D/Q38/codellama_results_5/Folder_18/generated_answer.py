
def find_subset_of_length_n(myset):
    return sum(1 for i in range(len(myset)+1) for j in itertools.combinations(myset,i))
