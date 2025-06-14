
def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string)):
        if string[i].isalpha():
            for j in range(i, len(string)):
                if (j - i) >= 99:
                    break
                if string[j] == string[i]:
                    palindromes.add((string[i:j]))
    return palindromes
