
import itertools

def palindromes_between_indices(string):
    letters = []
    for i in range(2, 4):
        if i < len(string):
            if string[i].isalpha():
                letters.append(string[i].lower())
    letters = set(letters)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            palindrome = ''.join(combination)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes
