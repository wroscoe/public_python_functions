'''
Created on Oct 25, 2009

'''

# -*- coding: Latin-1 -*-

"""
Convert OpenOffice documents to XML and text

USAGE:
ooconvert [filename]
"""

import zipfile
import re
import random
import os
import StringIO


#Extract XML or text from an Open Office Document
rx_stripxml = re.compile("<[^>]*?>", re.DOTALL|re.MULTILINE)
class ReadOO:

    def __init__(self, file_name):
        zf = zipfile.ZipFile(file_name)
        self.data = zf.read("content.xml")
        zf.close()

    def getXML(self):
        return self.data

    def getData(self, collapse=1):
        return " ".join(rx_stripxml.sub(" ", self.data).split())
    
#make a string a file object
def _string_to_file_obj(data):
    S = StringIO.StringIO()
    S.write(data)
    return S


#Callable Functions
def get_xml_from_00(data):
    file = _string_to_file_obj(data)
    oo = ReadOO(file)
    return oo.getXML(), None


def get_text_from_OO(data):
    file = _string_to_file_obj(data)
    oo = ReadOO(file)
    return oo.getData(), None

    
if __name__ == "__main__":
    filepath = '/var/www/daduce/sample_data/Rent_Calculations.ods'
    fileObj = open(filepath, 'r')
    data = fileObj.read()
    print get_text_from_OO(data)

