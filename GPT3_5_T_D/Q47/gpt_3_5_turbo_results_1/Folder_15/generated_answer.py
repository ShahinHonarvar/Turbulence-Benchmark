
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[:7].lower()
    
    for i in range(3, 7):
        for j in range(len(substring) - i + 1):
            if substring[j:j+i] == substring[j:j+i][::-1]:
                palindromes.add(substring[j:j+i].capitalize())
    
    return palindromes.intersection(set(string[:7]))
