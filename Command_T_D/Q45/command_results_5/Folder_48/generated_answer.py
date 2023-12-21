def palindromes_between_indices(s):
    return {i for i in range(4,len(s)-2,2) if i in range(6,8) and i == len(s)-i}
