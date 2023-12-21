
def palindromes_between_indices(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    palindromes = set()
    
    for i in range(2, 6):
        for j in range(i + 3, len(string)):
            substring = string[i:j]
            if substring == substring[::-1] and all(letter in letters for letter in substring):
                palindromes.add(substring)
    
    return palindromes
