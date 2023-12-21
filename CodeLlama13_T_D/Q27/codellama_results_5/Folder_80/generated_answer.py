
def insert_after_index(mylist):
    if 95 < len(mylist):
        mylist = mylist[:96]+[43]+mylist[96:]
    return mylist
