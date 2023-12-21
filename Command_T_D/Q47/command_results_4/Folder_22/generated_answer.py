def palindromes_of_specific_lengths(text):
    return set(text[i:j] for i in range(100, 200) for j in range(i, i + 5, -1))
