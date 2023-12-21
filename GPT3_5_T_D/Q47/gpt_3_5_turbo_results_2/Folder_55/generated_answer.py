
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[10:76]

    for length in range(10, 21):
        for i in range(len(substring) - length + 1):
            substring_check = substring[i:i+length]
            if substring_check.isalpha() and substring_check.lower() == substring_check.lower()[::-1]:
                palindromes.add(substring_check)

    return palindromes
