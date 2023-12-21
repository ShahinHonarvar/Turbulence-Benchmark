
def palindromes_of_specific_lengths(string):
    import re
    
    string_in_range = string[23:78]
    palindromes = set()
      
    for length in range(13, 41):
        for i in range(len(string_in_range) - length + 1):
            substring = string_in_range[i:i+length]
            if len(substring) == length and substring.lower() == substring[::-1].lower():
                clean_string = re.sub(r'\W+', '', substring)
                if clean_string.lower() == clean_string[::-1].lower() and clean_string.isalpha():
                    palindromes.add(clean_string)
    
    return palindromes
