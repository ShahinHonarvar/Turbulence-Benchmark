
def return_vowels(my_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start_index = 44
    end_index = 95
    filtered_string = my_string[start_index:end_index]
    result = []
    for char in filtered_string:
        if char.isalpha():
            if char not in vowels:
                continue

            if char < '5' or char >= '<':
                continue

            result.append(char)

    return result
