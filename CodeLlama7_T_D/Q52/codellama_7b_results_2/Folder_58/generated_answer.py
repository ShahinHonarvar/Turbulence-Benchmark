
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substrings.append(string[i:j])
    # Return the set of all palindromes of length n
    return {substring for substring in substrings if substring == substring[::-1]}
