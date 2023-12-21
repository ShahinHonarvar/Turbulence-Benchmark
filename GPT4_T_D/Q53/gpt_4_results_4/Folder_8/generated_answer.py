
def palindrome_of_length_at_least_n(my_str):
    my_str = my_str.lower()
    palindromes = set()
    for i in range(len(my_str)):
        for j in range(i + 1, len(my_str) + 1):
            sub_str = my_str[i:j]
            if len(sub_str) >= 45 and sub_str == sub_str[::-1] and sub_str.isalpha():
                palindromes.add(sub_str)
    return palindromes
