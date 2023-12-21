
from collections import deque

def lists_with_product_equal_n(circ_list):
    # convert the list into a circular queue
    circ_queue = deque(circ_list)
  
    # resulting list of sublists
    result = []
  
    # slide a window over the queue (rotate)
    # - repeat as many times as the length of the list 
    # - to cover all possible starting points
    for _ in range(len(circ_queue)):
        for i in range(1, len(circ_queue)+1):  # sublists of every possible length
            sublist = list(circ_queue)[:i]  # take a slice from the queue
            mult = 1
            for n in sublist:
                mult *= n
            if mult == 247:  # if the sublist's product equals to 247, append it to the result
                result.append(sublist)
        circ_queue.rotate(-1)  # rotate the queue to the left
    return result
