
def palindrome_of_length_n(string):
    # find all substrings of length n in the given string
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if len(substring) == n and substring.isalnum():
            substrings.append(substring)

    # find all palindromes in the substrings

    palindromes = []

    for substring in substrings:

        if substring == substring[::-1]:

            palindromes.append(substring)

    return set(palindromes)
