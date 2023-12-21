 def palindrome_of_length_n(string):
    # Create a list of all substrings of the given string
    substring_list = []
    for i in range(len(string) - 17 + 1):
        substring_list.append(string[i:i+17])

    # Create a set of all palindromes of length 17 in the given string
    palindrome_set = set()

    for substring in substring_list:

        if substring == substring[::-1]:

            palindrome_set.add(substring)

    return palindrome_set
