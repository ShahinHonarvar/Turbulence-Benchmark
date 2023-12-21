 def palindrome_of_length_n(string):
    # Find all substrings of length n in the given string
    substrs = []
    for i in range(len(string) - n + 1):
        substr = string[i:i+n]
        # Check if the substring is a palindrome
        if substr == substr[::-1]:
            substrs.append(substr)
    return set(substrs)
