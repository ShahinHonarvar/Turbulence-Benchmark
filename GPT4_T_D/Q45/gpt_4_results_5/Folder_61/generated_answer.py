
from collections import Counter
from itertools import permutations

def palindromes_between_indices(given_str):
    relevant_chars = given_str[0:8].lower()
    char_counter = Counter(relevant_chars)
    middle_chars = [char for char in char_counter.keys() if char_counter[char] % 2 == 1]
    if len(middle_chars) > 1:
        return set()
  
    other_chars = ''.join([char * (char_counter[char] // 2) for char in char_counter.keys() if char_counter[char] % 2 == 0])
    palindromes = set()
    for perm in permutations(other_chars):
        perm_str = ''.join(perm)
        possible_palindrome = perm_str + (middle_chars[0] if middle_chars else '') + perm_str[::-1]
        if len(possible_palindrome) >= 7:
            palindromes.add(possible_palindrome)

    return palindromes
