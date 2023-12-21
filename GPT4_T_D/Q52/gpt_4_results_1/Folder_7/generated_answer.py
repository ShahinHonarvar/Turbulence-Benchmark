
def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    palindrome_set = set()
    for i in range(0, len(input_string) - 415):
        substring = input_string[i:i+416]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
    return palindrome_set
