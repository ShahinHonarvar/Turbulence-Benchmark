 def palindromes_of_specific_lengths(string):
    # Find all palindromes in the specified index range
    palindromes = []
    for i in range(29, 97):
        substr = string[i:i+18]
        if len(substr) < 12 or len(substr) > 18:
            continue

        if substr == substr[::-1]:
            palindromes.append(substr)

    # Filter out palindromes of invalid lengths

    palindromes = [p for p in palindromes if len(p) >= 12 and len(p) <= 18]

    # Filter out palindromes that do not consist only of English letters

    palindromes = [p for p in palindromes if all(c.isalpha() for c in p)]

    return set(palindromes)
