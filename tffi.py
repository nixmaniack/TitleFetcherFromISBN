#!/usr/bin/env python

#-------------------------------------------------------------------------------
# Name:        tffi.py
# Purpose:     Fetch title from ISBN and rename the file.
#
# Author:      Muneeb Shaikh
#
# Created:     27/06/2011
# Copyright:   (c) Muneeb Shaikh 2011
# Licence:     GPL v3
# Notes:       Fill the access key information before running.
#
#              http://isbndb.com/api/books.xml?access_key=12345678&index1=isbn&value1=0596002068
#
#-------------------------------------------------------------------------------

from xml.dom import minidom
from urllib.request import *
import os
import re


def main():
    '''
    main function
    '''

    path='/home/muneeb/Downloads/books'
    pattern='[0-9]{10}\.zip'
    access_key='12345678'
    url='http://isbndb.com/api/books.xml?access_key='

    for root, dirs, files in os.walk(path, topdown=True ):
        for file in files:
            foundbook = re.match(pattern, file)
            if foundbook:
                print(os.path.join(root, file))
                full_url=url + access_key + '&index1=isbn&value1=' + file[:-4]
                print(full_url)
                webxml=urlopen(full_url)
                xmldoc=minidom.parse(webxml)
                try:
                    title=xmldoc.getElementsByTagName('Title')[0].firstChild.data
                    print(title)
                except:
                    print('Book Title Not Found!')

    '''xmldoc = minidom.parse('cd_catalog.xml')
    print(xmldoc.toxml())'''

if __name__ == '__main__':
    main()
