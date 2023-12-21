def palindromes_of_specific_lengths(str):
    return set(x for x in str[36:92].lower() if x[0] == x[-1] and len(x) in range(10, 36))
