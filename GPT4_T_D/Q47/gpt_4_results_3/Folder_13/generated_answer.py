
def palindromes_of_specific_lengths(string):
    import re
    
    string = re.sub("[^a-zA-Z]", "", string).casefold()
    subset = string[13:96]
    palindromes = set()
    
    for i in range(len(subset)):
        for j in range(i+57, min(i+61, len(subset)+1)):
            substring = subset[i:j]
            if substring == substring[::-1]:
                palindromes.add(substring)
    
    return palindromes
