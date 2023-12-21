
def if_contains_anagrams(string_list):
    anagrams = []
    for string in string_list:
        if len(string) >= 3:
            anagrams.append(''.join(sorted(string.lower())))
    counter = 0
    for i in range(len(anagrams) - 1):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j]:
                counter += 1
                if counter >= 11:
                    return True
    return False
