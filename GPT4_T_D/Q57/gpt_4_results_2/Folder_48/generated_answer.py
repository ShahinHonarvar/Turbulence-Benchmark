
import numpy as np

def submatrix_with_particular_sum(array_2d):
   rows, cols = array_2d.shape
   result = []
   
   for row in range(rows):
       for col in range(cols):
           for submatrix_width in range(1, cols-col+1):
               for submatrix_height in range(1, rows-row+1):
                   submatrix = array_2d[row:row+submatrix_height, col:col+submatrix_width]
                   
                   if submatrix.sum() == -261:
                       result.append(submatrix)
   
   return result
