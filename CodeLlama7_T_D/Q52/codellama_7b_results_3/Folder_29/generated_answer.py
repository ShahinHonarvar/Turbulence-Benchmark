
def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substring_list = []
    for i in range(len(string) - n + 1):
        substring_list.append(string[i:i+n])
    # Create a set to store palindromes
    palindrome_set = set()
    # Check if each substring is a palindrome and add it to the set if it is
    for substring in substring_list:
        if substring == substring[::-1]:
            palindrome_set.add(substring)
    return palindrome_set
