
def palindromes_between_indices(string):
    # Find the indices of the first and last occurrences of each letter in the string
    indices = {}
    for i, c in enumerate(string):
        if c not in indices:
            indices[c] = [i, i]
        else:
            indices[c][1] = i
    # Find all palindromes of length at least 6 between the specified indices
    palindromes = []
    for i in range(len(string) - 5):
        if string[i] == string[i + 5]:
            palindrome = ""
            for j in range(6):
                palindrome += string[i + j]
            palindromes.append(palindrome)
    return palindromes
