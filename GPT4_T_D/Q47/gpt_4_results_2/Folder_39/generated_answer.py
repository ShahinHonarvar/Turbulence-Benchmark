
def palindromes_of_specific_lengths(s):
    s = s[31:92]
    palindromes = set()
    for length in range(50, 54):
        for i in range(len(s)-length+1):
            substr = s[i: i+length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes
