#!/usr/bin/python

import sys
import threading
import urllib
from queue import Queue
import logging
import urllib
import os
import re
import io

if __name__ == '__main__':

    download_urls = []
    
    file_name_download = sys.argv[2]
 
    pattern_download_urls = re.compile(r'(.*)(DOWNLOAD CHECK\]\[Segment full url: )(http:/.+m4s)',re.M)


    with io.open(file_name_download, 'r') as reader:
        for line in reader:
            print(line)
            match_object = pattern_download_urls.match(line)
            if match_object:
                url = match_object.group(3)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
                print(url)
                os.system("wget "+url)
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
