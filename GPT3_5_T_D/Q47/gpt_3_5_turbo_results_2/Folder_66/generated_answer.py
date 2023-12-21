
def palindromes_of_specific_lengths(string):
    substring = string[32:80]
    palindromes = set()
    
    for length in range(35, 42):
        for i in range(len(substring) - length + 1):
            substring_lower = substring[i:i+length].lower()
            if substring_lower == substring_lower[::-1] and substring_lower.isalpha():
                palindromes.add(substring_lower)

    return palindromes
