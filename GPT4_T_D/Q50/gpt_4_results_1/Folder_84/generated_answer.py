
def if_contains_anagrams(str_list):
    ana_count = 0
    sorted_list = [''.join(sorted(word.lower())) for word in str_list if len(word)>=3]
    for i in range(len(sorted_list)):
        for j in range(i+1, len(sorted_list)):
            if sorted_list[i] == sorted_list[j]:
                ana_count += 1
    return ana_count >= 108
