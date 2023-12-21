
def palindromes_of_specific_lengths(string):
    substring = string[127:289].lower()
    palindromes = set()
    
    for length in range(119, 142):
        for start in range(len(substring) - length + 1):
            substring_length = substring[start:start+length]
            if substring_length == substring_length[::-1] and substring_length.isalpha():
                palindromes.add(substring_length)
    
    return palindromes
