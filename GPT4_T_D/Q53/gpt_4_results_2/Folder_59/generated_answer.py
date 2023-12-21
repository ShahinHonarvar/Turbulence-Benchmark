
def palindrome_of_length_at_least_n(string):
    palindrome_set = set()
    string = ''.join(ch for ch in string if ch.isalpha()).lower()
    for i in range(len(string)):
        for j in range(i + 19, len(string)):
            possible_palindrome = string[i:j + 1]
            if possible_palindrome == possible_palindrome[::-1]:
                palindrome_set.add(possible_palindrome)
    return palindrome_set
