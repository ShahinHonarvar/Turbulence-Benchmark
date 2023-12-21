import sys
def find_subset_of_length_n(s):
    return sum(1 for i in range(len(s)) for j in range(i+1, len(s)+1) if s[i:j])
