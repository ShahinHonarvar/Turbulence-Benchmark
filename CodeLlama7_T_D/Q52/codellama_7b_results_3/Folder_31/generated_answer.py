 def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == n and substring.isalnum():
            substrings.append(substring)

    # Create a list of all palindromes of length n in the given string

    palindromes = []

    for substring in substrings:

        if substring == substring[::-1]:

            palindromes.append(substring)


    return set(palindromes)
