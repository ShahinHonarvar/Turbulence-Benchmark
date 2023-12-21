
def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    set_of_palindrome = set()
    for i in range(len(input_string)):
        for j in range(i, len(input_string)):
            sub_string = input_string[i:j+1]
            if (len(sub_string) == 80) and (sub_string == sub_string[::-1]) and sub_string.isalpha():
                set_of_palindrome.add(sub_string)
    return set_of_palindrome
