
def palindrome_of_length_n(string):
    # find all substrings of length n in the string
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        if substring == substring[::-1]:
            substrings.append(substring)

    # return the set of all palindromes of length n as substrings of the given string
    return set(substrings)
