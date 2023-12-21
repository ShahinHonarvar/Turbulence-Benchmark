import sys
def find_subset_of_length_n(set):
    num = 0
    for i in range(len(set)):
        if len(set) - i >= 86:
            num += 1
    return num
