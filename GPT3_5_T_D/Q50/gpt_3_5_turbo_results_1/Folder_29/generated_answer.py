
def if_contains_anagrams(string_list):
    def get_anagrams(string):
        anagrams = []
        for i in range(len(string_list)):
            if i != string_list.index(string):
                if sorted(string.lower()) == sorted(string_list[i].lower()):
                    anagrams.append(string_list[i])
        return anagrams
    
    count = 0
    for string in string_list:
        if len(string) >= 3:
            anagrams = get_anagrams(string)
            if len(anagrams) >= 1:
                count += len(anagrams)
    
    if count >= 35:
        return True
    else:
        return False
