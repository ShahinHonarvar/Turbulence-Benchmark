
def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    palindrome_set = set()
    for i in range(len(input_string)):
        for j in range(i + 21, len(input_string) + 1):
            possible_palindrome = input_string[i:j]
            if possible_palindrome == possible_palindrome[::-1] and possible_palindrome.isalpha():
                palindrome_set.add(possible_palindrome)
    return palindrome_set
