
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    
    for i in range(2, 8):
        for j in range(i+1, 9):
            substr = string[i:j]
            if len(substr) >= 6 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    
    return palindromes
