
def palindromes_of_specific_lengths(string):
    substring = string[22:96]
    palindromes = set()
    
    for i in range(len(substring) - 51):
        substring_section = substring[i:i+52]
        substring_section = substring_section.lower()
        if substring_section.isalpha() and substring_section == substring_section[::-1]:
            palindromes.add(substring_section)
    
    return palindromes
