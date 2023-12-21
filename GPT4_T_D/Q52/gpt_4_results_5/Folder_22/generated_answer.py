
def palindrome_of_length_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string)):
        for j in range(i + 20, len(string) + 1):
            temp_str = string[i:j]
            if temp_str == temp_str[::-1]:
                if all(letter.isalpha() for letter in temp_str):
                    palindromes.add(temp_str)
    return palindromes
