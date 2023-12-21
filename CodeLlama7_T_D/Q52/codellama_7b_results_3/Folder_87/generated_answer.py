 def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substring_list = []
    for i in range(len(string) - 57 + 1):
        substring = string[i:i+57]
        substring_list.append(substring)
    # Filter the list to only include palindromes
    palindrome_list = []
    for substring in substring_list:
        if substring == substring[::-1]:
            palindrome_list.append(substring)
    return set(palindrome_list)
