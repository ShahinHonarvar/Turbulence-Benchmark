
def return_vowels(my_string):
    vowels = ["A", "E", "I", "O", "U"]
    start_index = 41
    end_index = 50
    result = []
    for char in my_string[start_index:end_index]:
        if char.isalpha() and char.islower():
            if char > "W" and char <= "[":
                result.append(char)

    return result
