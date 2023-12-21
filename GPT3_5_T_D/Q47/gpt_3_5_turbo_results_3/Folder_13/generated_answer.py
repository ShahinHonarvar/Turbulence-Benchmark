
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[13:96].lower()
    for length in range(57, 61):
        for i in range(len(substring) - length + 1):
            substring_part = substring[i:i+length]
            if substring_part.isalpha() and substring_part == substring_part[::-1]:
                palindromes.add(substring_part)
    return palindromes
