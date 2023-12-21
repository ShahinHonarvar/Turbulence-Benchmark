
def return_binary_or_hexa(test_tup):
    res = test_tup[45] + 1
    while res < test_tup[48]:
        if res not in test_tup[45:48]:
            break
        res += 1
    return ("{:b}".format(res), '{:x}'.format(res))
