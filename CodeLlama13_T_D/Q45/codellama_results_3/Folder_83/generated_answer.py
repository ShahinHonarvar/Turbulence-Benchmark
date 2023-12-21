
def palindromes_between_indices(string):
    letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    
    for i in range(2, 9 + 1):
        for j in range(i, 9 + 1):
            substr = string[i:j]
            if len(substr) >= 7 and all(letter in letters for letter in substr):
                palindromes.add(substr)
    
    return palindromes
