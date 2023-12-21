
import itertools

def palindromes_between_indices(string):
    english_letters = [char for char in string if char.isalpha()]
    english_letters = list(set([char.lower() for char in english_letters]))

    palindromes = set()
    for i in range(len(english_letters)):
        for combination in itertools.combinations(english_letters, i + 1):
            for permutation in itertools.permutations(combination):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 7 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)

    return palindromes
