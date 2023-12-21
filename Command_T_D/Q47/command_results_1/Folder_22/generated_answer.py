def palindromes_of_specific_lengths(s):
    return set(i[i[0] <= 100 < i[1] <= 200] for i in map(str.lower, range(len(s) - 1, -1, -1)))
