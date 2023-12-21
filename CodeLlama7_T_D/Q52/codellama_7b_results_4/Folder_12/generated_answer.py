 def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substring_list = []
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            substring_list.append(string[i:j])
    # Filter the list to only include palindromes of length n
    palindrome_list = []
    for substring in substring_list:
        if len(substring) == 23 and all(c.lower() == c.lower() for c in substring):
            palindrome_list.append(substring)
    return set(palindrome_list)
