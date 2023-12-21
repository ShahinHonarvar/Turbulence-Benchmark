
def palindromes_between_indices(s):
    # Find the first and last indices where the string can be split
    first_index = s.find('a')
    if first_index == -1:
        return set()

    last_index = s.rfind('z')
    if last_index == -1:
        return set()

    # Create a list of all possible palindromes between the indices
    palindromes = []

    for i in range(first_index + 1, last_index + 1):
        for j in range(i + 1, last_index + 1):
            if s[i] == s[j]:
                palindromes.append((s[i:j+1], i, j))

    # Filter the list of palindromes to only include those that have a length of at least 4 and are case-insensitive
    filtered_palindromes = []

    for p in palindromes:
        if len(p[0]) >= 4 and p[0].lower() == p[0]:
            filtered_palindromes.append(p)

    # Return the set of filtered palindromes
    return set(filtered_palindromes)
