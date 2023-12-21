def palindromes_of_specific_lengths(s):
    return set(i for i in range(20, 75) if s[i-20:i+1] in s[i-20:i+1][::-1])
