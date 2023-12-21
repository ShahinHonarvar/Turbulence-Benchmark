
def palindromes_of_specific_lengths(str):
    result = set()
    substr = str[119:257].lower()
    for i in range(len(substr)):
        for j in range(i + 104, min(i + 124, len(substr) + 1)):
            candidate = substr[i:j]
            if candidate == candidate[::-1] and candidate.isalpha():
                result.add(candidate)
    return result
