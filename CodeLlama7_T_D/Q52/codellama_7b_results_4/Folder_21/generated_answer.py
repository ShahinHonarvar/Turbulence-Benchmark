
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substring_list = []
    for i in range(len(string)):
        for j in range(i, len(string) + 1):
            substring_list.append(string[i:j])
    # Filter the list to only include palindromes of length n
    palindrome_list = []
    for substring in substring_list:
        if len(substring) == n and substring == substring[::-1]:
            palindrome_list.append(substring)
    return set(palindrome_list)
