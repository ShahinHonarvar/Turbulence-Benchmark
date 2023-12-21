
def palindromes_of_specific_lengths(string):
    substring = string[21:63]
    palindromes = set()
    
    for i in range(len(substring) - 21):
        for j in range(22, 34):
            current = substring[i:i+j].lower()
            if current == current[::-1] and current.isalpha():
                palindromes.add(current)
    
    return palindromes
