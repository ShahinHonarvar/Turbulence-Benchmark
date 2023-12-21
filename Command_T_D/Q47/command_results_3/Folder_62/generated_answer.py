def palindromes_of_specific_lengths(s):
    return {i for i in range(26, 87) if i - 26 in s[::-1].lower() and len(i - 26) in range(52, 56)}
