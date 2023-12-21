
def palindromes_of_specific_lengths(string):
    # Create a list of all palindromes in the string
    palindromes = []
    for i in range(24, 97 + 1):
        for j in range(i, len(string) - (97 - i) + 1):
            substring = string[i:j]
            if len(substring) < 10 or len(substring) > 36:
                continue

            if not all(c.isalpha() for c in substring):
                continue

            if substring == substring[::-1]:
                palindromes.append(substring)

    return set(palindromes)
