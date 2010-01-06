'''
Created on Oct 25, 2009

@author: wroscoe
'''
#programs to zip and unzip file

def get_data_type(data):
    """get the data type of a variable"""
    t = type(data).__name__
    return 0, {'_data_type*'+t:1}

def get_shebang_info(data, vars={}):
    """get the shebang info from a file"""
    first_line = data.split()[0]
    if first_line[0] != '#' or first_line[1] != '!':
        return None, False #not a shebang line
    
    path_start_index = first_line.find('/')
    path_end_index = first_line.find(' ',path_start_index)
    shebang_path = first_line[path_start_index : path_end_index]
    vars['_shebang_path*'+shebang_path] = 1
    
    shebang_program = first_line[path_end_index:].split()[0] #get the next word from the shebang line
    vars['_shebang_program*'+shebang_program] = 1
    return None, vars