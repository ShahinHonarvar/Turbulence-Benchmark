
def palindromes_of_specific_lengths(string):
    substring = string[106:281].lower()
    palindromes = set()
    for length in range(136, 152):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
