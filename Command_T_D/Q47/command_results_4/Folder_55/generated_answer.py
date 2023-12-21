def palindromes_of_specific_lengths(s):
    return {i[10:-10] for i in s[10:-75].lower() if len(i) in range(10, 21)}
