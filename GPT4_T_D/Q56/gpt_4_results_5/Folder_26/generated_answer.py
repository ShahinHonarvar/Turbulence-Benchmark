
def all_substring_of_size_n(S):
    lst = set(S[i: i + 33] for i in range(len(S) - 32))
    return [i for i in lst if len(set(i)) == 33]
