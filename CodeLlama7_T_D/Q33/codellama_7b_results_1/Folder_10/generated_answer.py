
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 31
    end_index = 37
    result = []
    for char in my_string[start_index:end_index]:
        if char.lower() in vowels and ord(char) > ord(';') and ord(char) <= ord('t'):
            result.append(char)
    return result
