
def palindrome_of_length_at_least_n(string):
    import re

    string = re.sub(r'[^a-zA-Z]', '', string.lower())

    palindromes = set()
    for i in range(len(string)-37):
        for j in range(i+38, len(string)+1):
            if string[i:j] == string[i:j][::-1]:
                palindromes.add(string[i:j])

    return palindromes
