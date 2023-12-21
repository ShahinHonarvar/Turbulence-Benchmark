 def palindrome_of_length_at_least_n(string, n=89):
    # Find all substrings of length greater than or equal to 89 in the given string
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) < n:
            continue

        substrings.append(substring)

    # Find palindromes by comparing each substring with its reverse

    palindromes = []

    for substring in substrings:

        if substring == substring[::-1]:

            palindromes.append(substring)

    # Return the set of all palindromes found in the given string

    return set(palindromes)
