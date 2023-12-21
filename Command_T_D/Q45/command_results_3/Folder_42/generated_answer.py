def palindromes_between_indices(str1):
    str1 = str(str1)
    str1 = str1.lower()
    str1 = str1[6:9]
    str1 = str1 + str1[::-1]
    return set(str1)
