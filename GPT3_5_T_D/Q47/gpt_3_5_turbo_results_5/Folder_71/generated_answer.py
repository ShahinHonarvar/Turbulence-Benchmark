
def palindromes_of_specific_lengths(string):
    substring = string[18:66]
    palindromes = set()
    for length in range(23, 37):
        for i in range(len(substring) - length + 1):
            substring_lowercase = substring[i:i+length].lower()
            if substring_lowercase.isalpha() and substring_lowercase == substring_lowercase[::-1]:
                palindromes.add(substring[i:i+length])
    return palindromes
