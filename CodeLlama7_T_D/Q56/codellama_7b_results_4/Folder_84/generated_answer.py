
def all_substring_of_size_n(s):
    # Initialize an empty list to store the substrings
    substrings = []

    # Iterate over the characters in the string
    for i in range(len(s)):
        # For each character, generate all possible substrings of size n starting from that character
        for j in range(i, len(s) - n + 1):
            substring = s[j:j+n]
            if not any(substring == s[k:k+n] for k in range(len(s)))):
                substrings.append(substring)

    # Return the list of all distinct substrings of size n with no duplicate characters, or an empty list if no such substrings exist in the given string
    return substrings
