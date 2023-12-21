
def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    len_str = len(input_string)
    palindrome_set = set()
    for length in range(93, len_str + 1):
        for i in range(len_str - length + 1):
            snippet = input_string[i : i + length]
            if snippet == snippet[::-1] and snippet.isalpha():
                palindrome_set.add(snippet)
    return palindrome_set
