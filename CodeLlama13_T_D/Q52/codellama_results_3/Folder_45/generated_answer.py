
def palindrome_of_length_n(string):
    return {p for p in find_all_palindromes(string) if len(p) == 21}

def find_all_palindromes(string):
    for i in range(len(string)):
        for j in range(i + 1, len(string) - i + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                yield substring

def is_palindrome(string):
    return string == string[::-1]
