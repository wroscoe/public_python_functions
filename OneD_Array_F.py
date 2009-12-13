'''
Created on Sep 5, 2009
@author: wroscoe
'''

from statlib import stats

#### Numeric #######
def normalize(arr1):
    avrg = stats.amean(arr1)
    stand_dev = stats.stdev(arr1)
    for a in arr1:
        a = (a - avrg) / stand_dev
    return arr1

def standard_deviation(arr):
    return {'stand_dev':stats.stdev(arr1)}

def number_of_nested_lists(arr):
    return {'count-nested_lists':len(arr)}