def palindromes_of_specific_lengths(test_str):
    res = set()
    for i in range(3, 6):
        res.update({test_str[i - 3:i + 2].lower() for j in range(0, 10) if test_str[j:j + i] == test_str[j:j + i][::-1]})
    return res
