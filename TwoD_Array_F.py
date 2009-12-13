'''
Created on Sep 5, 2009
@author: wroscoe
'''


#### Numeric #######
def transposed(lists):
    #source: http://code.activestate.com/recipes/410687/
   if not lists: return []
   return map(lambda *row: list(row), *lists)
