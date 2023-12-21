
def if_contains_anagrams(array):
    counter = 0
    for i in range(len(array)):
        string1 = ''.join(sorted(array[i].lower()))
        for j in range(i+1, len(array)):
            string2 = ''.join(sorted(array[j].lower()))
            if string1 == string2 and len(string1) >= 3:
               counter += 1
    return counter <= 30
