
def palindromes_between_indices(string):
    english_letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    
    for i in range(1, 8):
        for j in range(i + 2, 9):
            substr = string[i:j]
            if len(substr) >= 3 and substr == substr[::-1]:
                palindromes.add(substr)
    
    return palindromes
