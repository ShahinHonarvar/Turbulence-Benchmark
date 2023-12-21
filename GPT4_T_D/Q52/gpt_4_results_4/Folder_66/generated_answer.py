
def palindrome_of_length_n(string):
    string = string.lower()
    lst = list(string)
    n = 25
    palindromes_set = set()
    for i in range(len(lst) - n + 1):
        substr = lst[i: i + n]
        if is_palindrome(substr):
            palindromes_set.add(''.join(substr))
    return palindromes_set

def is_palindrome(substr):
    for i in range(int(len(substr) / 2)):
        if substr[i].isalpha() and substr[-i-1].isalpha():
            if substr[i] != substr[-i-1]:
                return False
        else:
            return False
    return True
