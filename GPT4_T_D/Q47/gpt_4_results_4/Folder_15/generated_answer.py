
def palindromes_of_specific_lengths(string):
    palindromes = set()
    for i in range(7):
        for j in range(i+3, min(7, i+7)):
            substr = string[i:j]
            if substr == substr[::-1] and substr.isalpha():
                palindromes.add(substr.lower())
    return palindromes
