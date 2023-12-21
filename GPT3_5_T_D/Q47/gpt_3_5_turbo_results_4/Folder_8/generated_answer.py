
def palindromes_of_specific_lengths(string):
    palindromes = set()
    substring = string[17:73].lower()
    
    for i in range(len(substring) - 49):
        if substring[i:i+52] == substring[i:i+52][::-1]:
            palindromes.add(substring[i:i+52])
    
    return palindromes
