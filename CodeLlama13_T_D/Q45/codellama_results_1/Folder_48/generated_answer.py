
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    
    for i in range(6, 9):
        for j in range(i, len(string)):
            substr = string[i:j]
            if len(substr) >= 4 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    
    return palindromes
