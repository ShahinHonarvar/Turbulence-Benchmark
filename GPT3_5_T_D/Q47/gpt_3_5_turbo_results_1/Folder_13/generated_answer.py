
def palindromes_of_specific_lengths(string):
    substring = string[13:96]
    palindromes = set()
    for length in range(57, 61):
        for i in range(len(substring)):
            substr = substring[i:i+length]
            if substr.lower() == substr.lower()[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
