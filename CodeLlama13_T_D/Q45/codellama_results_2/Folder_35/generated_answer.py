
def palindromes_between_indices(string):
    palindromes = set()
    for i in range(2, len(string) - 3):
        for j in range(i + 1, len(string) - 2):
            if string[i] == string[j]:
                substring = string[i:j+1]
                if substring not in palindromes and is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes

def is_palindrome(string):
    return string == string[::-1]
