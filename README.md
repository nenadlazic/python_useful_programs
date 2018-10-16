This repository contains useful functions written in python

# compare_segment_list_and_download.py - compare segment list and downloaded list urls #
The program receives two arguments:
1. First file containing a log with urls that is really used to download data with the get method over HTTP

2. The second file contains the urls that should be used to download the data

The program is executed in the following manner:
python3 compare_segment_list_and_download.py download_urls.txt fill_segment_list.txt

# read_all_files.py - search for the specified binary sequence in all binary files within the specified directory
python3 read_all_files.py "/home/myusername/test" "hello"


# download_segments.py - download file from urls in file.txt
python3 download_segments.py downloadr_segments.py file.txt

