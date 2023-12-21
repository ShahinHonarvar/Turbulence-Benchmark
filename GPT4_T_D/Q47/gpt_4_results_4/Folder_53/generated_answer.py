
def palindromes_of_specific_lengths(s):
    palindromes = set()
    s = s[1:300]

    for length in range(3, 11):
        for i in range(len(s)):
            substr = s[i:i+length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())

    return palindromes
