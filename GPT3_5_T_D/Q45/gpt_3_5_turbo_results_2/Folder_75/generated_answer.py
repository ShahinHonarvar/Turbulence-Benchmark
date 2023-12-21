
def palindromes_between_indices(string):
    result = set()
    for i in range(2, 5):
        for j in range(i+2, 5):
            substring = string[i:j+1].lower()
            if substring == substring[::-1] and len(substring) >= 3:
                result.add(substring)
    return result
