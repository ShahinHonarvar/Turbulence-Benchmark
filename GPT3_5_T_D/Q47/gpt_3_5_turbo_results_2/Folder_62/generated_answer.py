
def palindromes_of_specific_lengths(string):
    substring = string[26:88]
    palindromes = set()
    for i in range(len(substring) - 51):
        substring_lower = substring[i:i+52].lower()
        if substring_lower == substring_lower[::-1] and substring_lower.isalpha():
            palindromes.add(substring_lower)
    return palindromes
