
def palindromes_of_specific_lengths(string):
    string = string[40:95]
    palindromes = set()
    
    for length in range(45, 52):
        for i in range(len(string) - length + 1):
            substring = string[i:i+length]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    
    return palindromes
