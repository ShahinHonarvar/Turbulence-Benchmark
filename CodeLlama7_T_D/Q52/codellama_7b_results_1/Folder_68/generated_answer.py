
def palindrome_of_length_n(string):
    # Create a list of all substrings of length n
    substrings = []
    for i in range(len(string) - n + 1):
        substring = string[i:i+n]
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            substrings.append(substring)

    return set(substrings)
