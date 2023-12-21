
import sys

def insert_at_index(a_list):
    res = []
    for i in range(len(a_list)):
        res.append(a_list[i])
    res.insert(38, 45)
    return res
