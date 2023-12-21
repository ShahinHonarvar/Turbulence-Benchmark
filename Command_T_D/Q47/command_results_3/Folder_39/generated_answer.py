def palindromes_of_specific_lengths(s):
    str_list = []
    for i in range(31, 91):
        for j in range(i + 50, i + 53):
            str_list += s[i:j + 1].lower()
    return set(str_list)
