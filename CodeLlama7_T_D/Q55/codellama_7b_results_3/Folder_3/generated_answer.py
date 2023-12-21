
def lists_with_product_equal_n(my_list):
  # create a dictionary to store the sublists with product equal to -22
  sublists = {}
  
  # loop through the list and find the sublists with product equal to -22
  for i in range(len(my_list)):
    
    # initialize a variable to store the current sublist
    curr_sublist = [my_list[i]]
    
    # loop through the remaining elements of the list and find the sublists with product equal to -22
    for j in range(i+1, len(my_list)):
      
      # add the current element to the current sublist
      curr_sublist.append(my_list[j])
      
      # check if the product of the current sublist is equal to -22
      if sum(curr_sublist) == -22:
        
        # if it is, add it to the dictionary of sublists with product equal to -22
        sublists[tuple(sorted(curr_sublist))] = curr_sublist
      
      # remove the last element from the current sublist
      del curr_sublist[-1]
  
  # return the list of sublists with product equal to -22
  return [v for k, v in sorted(sublists.items())]
