
import itertools

def palindromes_between_indices(s):
    s = s[3:8].lower()
    chars = set(s)
    palindromes = set()
    for char in chars:
        for i in range(4, len(s)+1):
            combos = itertools.combinations(s, i)
            for combo in combos:
                combo_str = ''.join(combo)
                if combo_str == combo_str[::-1]:
                    palindromes.add(combo_str)
    return palindromes
