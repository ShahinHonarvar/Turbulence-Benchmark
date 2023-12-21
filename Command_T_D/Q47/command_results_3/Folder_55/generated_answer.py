def palindromes_of_specific_lengths(s):
    return {i[::-1] for i in s[10:-5:-1] if len(i) in range(10, 21)}
