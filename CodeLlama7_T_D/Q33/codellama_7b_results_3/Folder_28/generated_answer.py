 def return_vowels(string):
    vowels = []
    for i in range(41, 50):
        if string[i].lower() in ["a", "e", "i", "o", "u"] and string[i] > "W" and string[i] <= "[":
            vowels.append(string[i])
    return vowels
