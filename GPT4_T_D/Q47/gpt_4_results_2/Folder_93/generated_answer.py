
def palindromes_of_specific_lengths(string):
    import re
    palindromes = set()
    substring = string[17:96]
    for i in range(13, 50):
        for j in range(len(substring) - i + 1):
            substring_temp = substring[j:j + i]
            if re.fullmatch("^[A-Za-z]*$", substring_temp):
                if substring_temp.lower() == substring_temp[::-1].lower():
                    palindromes.add(substring_temp)
    return palindromes
