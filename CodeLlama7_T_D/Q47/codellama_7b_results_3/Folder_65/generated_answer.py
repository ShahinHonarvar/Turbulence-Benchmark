
def palindromes_of_specific_lengths(string):
    # Find all palindromes in the substring from index 15 to index 95, both inclusive
    palindromes = []
    for i in range(15, 96):
        substr = string[i:i+20]
        if len(substr) < 20 or len(substr) > 66:
            continue

        if substr == substr[::-1]:
            palindromes.append(substr)

    # Find all palindromes of lengths between 20 to 66 (both inclusive)
    filtered_palindromes = []

    for palindrome in palindromes:
        if len(palindrome) < 20 or len(palindrome) > 66:
            continue

        filtered_palindromes.append(palindrome)

    # Return the set of all palindromes with the specified requirements
    return set(filtered_palindromes)
