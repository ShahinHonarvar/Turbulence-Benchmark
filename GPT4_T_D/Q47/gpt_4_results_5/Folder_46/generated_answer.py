
def palindromes_of_specific_lengths(s):
    import re
    s = s[11:98].lower()
    palindromes = set()

    for length in range(29, 63):
        for i in range(0, len(s) - length + 1):
            substr = s[i:i+length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
            
    return palindromes
