
import itertools

def palindromes_between_indices(string):
    letters = [c.lower() for c in string if c.isalpha()]
    letter_counts = {letter: letters.count(letter) for letter in letters}
    possible_letters = ''.join([letter * count for letter, count in letter_counts.items()])

    palindromes = set()
    for letters_combination in itertools.combinations(possible_letters, 4):
        for permutation in itertools.permutations(letters_combination, 4):
            palindrome = ''.join(permutation)
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)

    return palindromes
