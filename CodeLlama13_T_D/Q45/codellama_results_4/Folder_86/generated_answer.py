
def palindromes_between_indices(string):
    indices = range(6, 10)
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    
    for i in indices:
        for j in range(i+1, len(string)):
            substr = string[i:j]
            if len(substr) >= 4 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    
    return palindromes
