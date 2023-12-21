
import itertools

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:8] if char.isalpha()]
    palindromes = set()
    
    if len(letters) < 5:
        return palindromes
        
    for length in range(5, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)

    return palindromes
