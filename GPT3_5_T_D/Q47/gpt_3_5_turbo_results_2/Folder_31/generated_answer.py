
def palindromes_of_specific_lengths(string):
    lowercase_string = string.lower()
    substring = lowercase_string[10:83]
    palindromes = set()

    for length in range(37, 61):
        for i in range(len(substring) - length + 1):
            substr = substring[i:i+length]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr)

    return palindromes
