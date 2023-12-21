
def palindromes_between_indices(string):
    english_letters = set("abcdefghijklmnopqrstuvwxyz")
    palindromes = set()
    
    for i in range(3, 6):
        for j in range(i + 1, len(string) - i + 2):
            substr = string[i:j]
            if all(letter in english_letters for letter in substr):
                palindromes.add(substr)
    
    return palindromes
