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
    
def _string_to_file_obj(data):
    """accept a string and return a file object witen with StringIO()"""
    S = StringIO.StringIO()
    S.write(data)
    return S


def get_xml_from_00(data):
    """return the data from an OpenOffice file in xml format"""
    file = _string_to_file_obj(data)
    oo = ReadOO(file)
    return oo.getXML(), None


def get_text_from_OO(data):
    """return the data from an OpenOffice file as text"""
    file = _string_to_file_obj(data)
    oo = ReadOO(file)
    return oo.getData(), None

