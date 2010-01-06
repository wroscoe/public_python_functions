'''
Created on Sep 5, 2009

@author: wroscoe
'''
import math
from statlib import stats


if __name__ == '__main__':
    pass

def count_characters(string):
    string = str(string)
    if len(string) > 5000:     string = string[:5000]
    
    chars = len(string)
    charlist = map(chr, range(32, 126))
    # count the characters in the string and create a dictionary of char:count pairs
    charCount = {}
    for char in string.lower():
        if char in charlist:
            charCount[char] = charCount.get(char, 0) + 1
    
    charRatio = {}
    for k, v in charCount.iteritems():
        charRatio[k] = v / math.sqrt(v**2 + 10)
    
    return charRatio 

def letters_between_spaces(str):
    #count the average word size
    words = str.split()
    wordCount = len(words)
    ch = []
    for word in words:
        ch.append(len(word)) 
    letterCountAverage =  stats.mean(ch)
    letterCountStdDev = stats.stdev(ch)
    return None, {'letterAve/StdDev':letterCountAverage / letterCountStdDev}