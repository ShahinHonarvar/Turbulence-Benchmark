
def palindromes_between_indices(string):
    english_letters = [char.lower() for char in string if char.isalpha()]
    if len(english_letters) < 5:
        return set()
    
    palindromes = set()
    for i in range(3, 5):
        for j in range(3, 5):
            if i != j:
                palindrome = english_letters[i] + english_letters[j] + english_letters[i]
                palindromes.add(palindrome)
    
    return palindromes
