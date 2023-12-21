
def return_vowels(input_string):
    vowels_list = []
    for char in input_string[71:81]:
        if char > '>' and char <= 'U' and char.lower() in "aeiou":
            vowels_list.append(char)
    return vowels_list
