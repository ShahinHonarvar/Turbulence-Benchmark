
def palindromes_of_specific_lengths(string):
    result = set()
    for i in range(1, 8):
        for j in range(i+2, min(len(string), 8)):
            substr = string[i:j]
            if substr == substr[::-1]:
                result.add(substr)
    return result
