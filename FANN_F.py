'''
Created on Sep 5, 2009
@author: wroscoe
'''

def test_predictability_for_all_columns(arr):
    #accept an array with columns stored as 1D arrays inside a larger array
    #will take some time for larger data sets
    pass

def convert_bpnn_array_to_fann_file(arr = [[[1,2], [5]], [[4,4],[3]]] ):
    # accept an array in the training data format of bpnn.py 
    # and return a string in the FANN training data format 
    from cStringIO import StringIO
    file_str = StringIO()

    num_training_sets = str(len(arr))
    num_inputs = str(len(arr[1][0]))
    num_outputs = str(len(arr[1][1]))
    file_str.write(num_training_sets + ' ' + num_inputs + ' ' + num_outputs + '\n')
    
    for set in arr:
        for input in set[0]:
            file_str.write(str(input) + ' ')
        file_str.write('\n')
        
        for output in set[1]:
            file_str.write(str(output) + ' ')
        file_str.write('\n')
        
    return file_str.getvalue()
    
    
def convert_fann_file_to_bpnn_array(str = '2 2 1\n1 2\n5\n4 4\n3\n'):
    # convert a string in the format of the FANN training data
    # to an array formated for bpnn.py to
    arrLines = str.split('\n')
    arrLines.pop(0) # remove the descriptive first line
    arrBpnn = []
    while len(arrLines) > 1:
        inputs = map(lambda x: float(x), arrLines.pop(0).split())
        outputs = map(lambda x: float(x), arrLines.pop(0).split())
        arrBpnn.append([inputs, outputs])
    
    return arrBpnn

if __name__ == '__main__':
    print convert_fann_file_to_bpnn_array()
    