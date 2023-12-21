
def palindromes_of_specific_lengths(string):
    string = string.lower()
    substring = string[124:284]
    palindromes = set()
    
    for length in range(115, 135):
        for i in range(len(substring) - length + 1):
            if substring[i:i+length].isalpha() and substring[i:i+length] == substring[i:i+length][::-1]:
                palindromes.add(substring[i:i+length])
    
    return palindromes
