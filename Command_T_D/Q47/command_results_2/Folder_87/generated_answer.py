def palindromes_of_specific_lengths(text):
    return {i for i in range(11, 93) if all(a == b for a, b in zip(text[i:j], text[i:j][::-1])) for j in range(i+34, min(len(text)-1, i+54)+1)}
