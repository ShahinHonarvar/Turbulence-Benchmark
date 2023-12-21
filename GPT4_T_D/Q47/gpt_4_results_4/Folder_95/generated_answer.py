
def palindromes_of_specific_lengths(string):
    import re
    string = string[12:57]
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(20,22):
            temp_string = string[i:i+j]
            if re.search('[a-zA-Z]', temp_string) and temp_string.lower() == temp_string.lower()[::-1]:
                palindrome_set.add(temp_string)
    return palindrome_set
