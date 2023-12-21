
def palindromes_of_specific_lengths(s):
    s = s[0:10].lower()
    palindromes = set()
    for substr_len in range(3, 6):
        for index in range(len(s)-substr_len+1):
            substr = s[index:index+substr_len]
            if substr.isalpha() and substr == substr[::-1]:
                palindromes.add(substr)
    return palindromes
