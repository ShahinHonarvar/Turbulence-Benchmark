
def palindromes_between_indices(string):
    # Get the indices of the English letters in the given string that occur between index 3 and index 7, both inclusive.
    indices = []
    for i in range(3, len(string)):
        if string[i].isalpha():
            indices.append(i)
    # Create a set of all palindromes of the length of at least 5 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 3 to index 7, both inclusive.
    palindromes = set()
    for i in range(len(indices) - 1):
        for j in range(i + 1, len(indices)):
            substring = string[indices[i]:indices[j] + 1]
            if len(substring) >= 5 and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes
