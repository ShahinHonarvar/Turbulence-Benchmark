
def palindromes_of_specific_lengths(string):
    substring = string[32:80]
    palindromes = set()
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr.lower() == substr.lower()[::-1] and substr.isalpha():
                palindromes.add(substr)
    return palindromes
