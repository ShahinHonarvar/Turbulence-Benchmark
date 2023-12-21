
def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    length = 416
    palindrome_set = set()
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i+length]
        if substring == substring[::-1] and substring.isalpha():
            palindrome_set.add(substring)
    return palindrome_set
