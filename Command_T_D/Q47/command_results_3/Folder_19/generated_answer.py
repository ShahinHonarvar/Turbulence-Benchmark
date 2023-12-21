def palindromes_of_specific_lengths(text):
    return set(pal for i in range(10, 56) for j in range(10, 56) for pal in text[i:j+1].lower() if len(pal) in (3, 4, 5, 6, 7))
