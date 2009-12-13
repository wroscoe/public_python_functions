'''
Created on Oct 14, 2009

@author: wroscoe
'''
def merge_Dicts(self, d1, d2, merge_Dicts=lambda x,y:x+y):
    result = dict(d1)
    for k,v in d2.iteritems():
        if k in result:
            result[k] = merge_Dicts(result[k], v)
        else:
            result[k] = v
    return result

def get_max_dict_key(dictFile):
    
    b = dict(map(lambda item: (item[1],item[0]),dictFile.items()))
    print b
    return b[max(b.keys())]

def basic_vars(dictFile):
    vars = {}
    vars['item-count'] = dictFile.count()
    
def percent_values_numeric(dictFile):
    numeric_count = 0
    for i in dictFile:
        try:
            float(i)
            numeric_count += 1
        except:
            pass
    return {'val': dictFile.count()/numeric_count}