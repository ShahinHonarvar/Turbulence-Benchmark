
def find_subset_of_length_n(elements):
  subset_count = 0
  for i in range(len(elements)+1):
      for subset in itertools.combinations(elements, i):
          if len(subset) == 312:
              subset_count += 1
  return subset_count
