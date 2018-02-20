import os
import sys
import base64


def processingDirectory(dir_path, required_content):
    location = os.getcwd()
    counter = 0
    m4s_files = []
    files_with_required_content = []

    if dir_path[0] == '/':
        location = dir_path
    else:
        location = location+'/'+dir_path

    print(location)

    for file in os.listdir(location):
        try:
            if file.endswith(".m4s"):
                #print("m4s file found:\t", file)
                m4s_files.append(str(file))
                counter = counter+1

                #open and read file
                fileName = location+'/'+file 
                with open(fileName, mode='rb') as fileOpened: # b is important -> binary
                    fileContent = fileOpened.read()
                    #print(''.join(format(x, ' 02x') for x in fileContent))

                    count_1 = 0
                    for i in range(0, len(fileContent)):
                        if fileContent[i] == required_content[count_1]:
                            count_1 = count_1 + 1 
                            if count_1 == len(required_content):
                                #print("SEQUENCE FOUND IN FILE "+file)
                                files_with_required_content.append(str(file))
                                count_1 = 0
                        else:
                            count_1 = 0
                        
        except Exception as e:
            raise e
            print("No files found here!")

    print("\n###########################################")
    print("# Requested sequence was found in %s files #" % (len(files_with_required_content)))
    print("###########################################\n")

    for i in range(0,len(files_with_required_content)):
        print(files_with_required_content[i])

if __name__ == '__main__':

	if len(sys.argv) < 3:
            print("Enter path to the directory and required content!")
            sys.exit()

	dir_name = sys.argv[1]
	print(dir_name)
	reqCont = sys.argv[2].encode('utf-8')
	#print(reqCont.hex())
	processingDirectory(dir_name,reqCont)
