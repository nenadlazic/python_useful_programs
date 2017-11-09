import io
import sys
import re

def compareDownloadedUrls(download_urls, fill_urls):
    
    pattern_list_fill = re.compile(r'(\d+\-\d+ \d+\:\d+\:\d+\.\d+).*(PLAYLIST URL: )(.*\.m4s)(.*\n)',re.M)
    pattern_download_urls = re.compile(r'(\d+\-\d+ \d+\:\d+\:\d+\.\d+)(.*)(subtitle.*\.m4s)(.*\n)',re.M)
    
    downloads = []
    fill_url = []
    prevTime = ""
    prevUrl = ""

    track1 = "725_152"
    track2 = "725_888" 
    track3 = "725_889"
    count_t1 = 0
    count_t2 = 0
    count_t3 = 0

    with io.open(download_urls, 'r') as reader1:
        for line in reader1:
            #print(line)
            strUrl = ""
            match_object = pattern_download_urls.match(line)
            if match_object:
                time = match_object.group(1)
                urls = match_object.group(3)
                strUrl = 'TIME: '+time+' URL: '+urls+'\n'
          
                if urls.find(track1) != -1:
                    count_t1 = count_t1 + 1
                elif urls.find(track2):
                    count_t2 = count_t2 + 1
                elif urls.find(track3):
                    count_t3 = count_t3 + 1

                #print(strUrl)
                if prevUrl != urls:
                    downloads.append(strUrl)
                    prevUrl = urls


    print("items in downloads list: ",len(downloads))
    print("Count t1: ", count_t1)
    print("Count t2: ", count_t2)
    print("Count t3: ", count_t3)

    count_t1 = 0
    count_t2 = 0
    count_t3 = 0


    prevTime = ""
    prevUrl = ""
    with io.open(fill_urls, 'r') as reader2:
        count = 0
        for line in reader2:
            #print(line)
            strUrl = ""
            match_object = pattern_list_fill.match(line)
            if match_object:
                time = match_object.group(1)
                urlf = match_object.group(3)
                
                if urlf.find(track1) != -1:
                    count_t1 = count_t1 + 1
                elif urlf.find(track2):
                    count_t2 = count_t2 + 1
                elif urlf.find(track3):
                    count_t3 = count_t3 + 1

               
                if prevUrl != urlf:
                    prevUrl = urlf

                    flag = 0
                    strUrl = "" 
                    for i in downloads:
                       if i.find(urlf) != -1: #not found
                          strUrl = 'FILL TIME: '+time+' URL: '+urlf+' downloaded\n'
                          #print(strUrl+" downloaded")
                          count = count + 1
                          prevTime = time
                          flag = 1
                          break

                    if flag == 1:
                        fill_url.append(strUrl)
                        flag = 0
                    else:
                        strUrl = 'FILL TIME: '+time+' URL: '+urlf+'\n'
                        fill_url.append(strUrl)

    print("Count downloaded: ", count)
    print("Count t1: ", count_t1)
    print("Count t2: ", count_t2)
    print("Count t3: ", count_t3)


    print("items in fill list: ", len(fill_url))

    with open("download_urls", 'w') as file_handler:
        for item in downloads:
            file_handler.write(item)	
    with open("fill_urls", 'w') as file_handler:
        for item in fill_url:
            file_handler.write(item)	
    print("items realy downloaded: ",count)

if __name__ == '__main__':

	file_name_download = sys.argv[1]
	file_name_fill = sys.argv[2]

	print(file_name_download)
	print(file_name_fill)
               
	compareDownloadedUrls(file_name_download, file_name_fill)
