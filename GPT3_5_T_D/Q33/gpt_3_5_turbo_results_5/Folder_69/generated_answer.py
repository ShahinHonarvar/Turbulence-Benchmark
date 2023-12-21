
def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_list = []
  
    for i in range(641, 872):
        if string[i] > '>' and string[i] <= 'q' and string[i] in vowels:
            vowels_list.append(string[i])

    return vowels_list
