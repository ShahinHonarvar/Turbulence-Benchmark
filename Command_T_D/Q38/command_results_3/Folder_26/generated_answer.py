import sys
def find_subset_of_length_n(s):
    #Your code here
    #First find all the subsets of size 25
    num_subsets = 1
    for i in range(25):
        num_subsets *= (len(s) - i)
    #Then return the number of unique subsets
    return len(s) * num_subsets
