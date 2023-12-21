def palindromes_between_indices(text):
    letters = set(text[1:-1])
    if len(letters) < 7:
        return set()
    return set((''.join(sorted( letters[i:i+7]))) for i in range(1,len(letters)-6))
