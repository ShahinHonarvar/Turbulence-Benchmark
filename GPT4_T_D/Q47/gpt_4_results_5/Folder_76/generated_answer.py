
def palindromes_of_specific_lengths(string):
    string = string[101:292+1]
    palindromes = set()
    
    for length in range(154, 182+1):
        for i in range(len(string) - length + 1):
            substring = string[i: i + length]
            if substring == substring[::-1] and substring.lower().isalpha():
                palindromes.add(substring)
                
    return palindromes
