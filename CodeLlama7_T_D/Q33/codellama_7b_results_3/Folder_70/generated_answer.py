
def return_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    start_index = 171
    end_index = 402
    result = []
    for i in range(start_index, end_index + 1):
        if vowels.count(string[i]) > 0 and string[i].lower() > "i" and string[i].lower() <= "k":
            result.append(string[i])
    return result
