
def if_contains_anagrams(string_list):
    def sortWord(word):
        return ''.join(sorted(word.lower()))

    counter = 0
    for i in range(len(string_list)):
        for j in range(i+1, len(string_list)):
            if len(string_list[i]) >= 3 and len(string_list[j]) >= 3:
                if sortWord(string_list[i]) == sortWord(string_list[j]):
                    counter += 1
                    if counter > 61:
                        return False
    return True
