
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[24:98].lower()
    
    for length in range(10, 37):
        for i in range(len(substring) - length + 1):
            substring_check = substring[i:i+length]
            if substring_check.isalpha() and substring_check == substring_check[::-1]:
                palindromes.add(substring_check)

    return palindromes
