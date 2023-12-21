
def palindrome_of_length_at_least_n(input_string):
    str_set = set()
    input_string = ''.join(character for character in input_string if character.isalpha()).lower()
    start_index = 0
    while start_index < len(input_string):
        for end_index in range(start_index + 13, len(input_string)):
            sub_string = input_string[start_index:end_index+1]
            if sub_string == sub_string[::-1]:
                str_set.add(sub_string)
        start_index += 1
    return str_set
