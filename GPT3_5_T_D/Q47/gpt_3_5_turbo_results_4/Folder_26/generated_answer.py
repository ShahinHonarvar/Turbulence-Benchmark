
def palindromes_of_specific_lengths(string):
    substring = string[24:85]
    substring = substring.lower()
    palindromes = set()
    for length in range(21, 32):
        for start in range(len(substring) - length + 1):
            end = start + length
            substring_to_check = substring[start:end]
            if substring_to_check == substring_to_check[::-1] and substring_to_check.isalpha():
                palindromes.add(substring_to_check)
    return palindromes
