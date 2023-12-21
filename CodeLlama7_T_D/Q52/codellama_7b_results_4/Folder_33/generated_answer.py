 def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substring_list = []
    for i in range(len(string) - n + 1):
        substring_list.append(string[i:i+n])
    # Remove any substrings that are not palindromes
    palindrome_list = []
    for substring in substring_list:
        if substring == substring[::-1]:
            palindrome_list.append(substring)
    return set(palindrome_list)
