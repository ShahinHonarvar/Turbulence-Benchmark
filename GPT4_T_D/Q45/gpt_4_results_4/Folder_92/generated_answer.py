
import itertools

def palindromes_between_indices(text):
    text = text[4:8].lower()
    palindromes = set()
    for i in range(4, len(text) + 1):
        for combination in itertools.combinations(text, i):
            combo_str = ''.join(combination)
            if combo_str == combo_str[::-1]:
                palindromes.add(combo_str)
    return palindromes
