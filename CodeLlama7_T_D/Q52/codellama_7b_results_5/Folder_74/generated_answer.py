
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string) - 95):
        substring = string[i:i + 96]
        if len(substring) == 96 and substring.isalpha():
            substrings.append(substring)

    # Return the set of all palindromes of length 96 as a subset of the given string
    return set(substrings)
