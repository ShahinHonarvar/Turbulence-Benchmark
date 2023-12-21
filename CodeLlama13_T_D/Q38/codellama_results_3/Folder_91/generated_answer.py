
def find_subset_of_length_n(my_set):
    return len([i for i in range(6) if {j for j in my_set}])
