
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[11:94]
    substring = substring.lower()
    for length in range(34, 55):
        for i in range(len(substring) - length + 1):
            substring_sub = substring[i:i+length]
            if substring_sub == substring_sub[::-1] and substring_sub.isalpha():
                palindromes.add(substring_sub)
    
    return palindromes
