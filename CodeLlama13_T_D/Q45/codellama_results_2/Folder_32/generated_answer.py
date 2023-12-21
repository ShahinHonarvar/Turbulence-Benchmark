
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    
    for i in range(1, 7):
        for j in range(i + 5, len(string)):
            substr = string[i:j]
            if all(letter in letters for letter in substr) and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
