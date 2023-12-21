
def palindromes_between_indices(string):
    letters = ''.join(sorted(set(string)))
    return {''.join(letters[i:j]) for i in range(1, 4) for j in range(i + 3, len(letters) + 1) if letters[i] == letters[j - 1]}
