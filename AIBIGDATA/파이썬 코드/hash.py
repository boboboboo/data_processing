import os


path = "./"

file_list = os.listdir(path)
#file_name = os.path.basename(file_list)

data = []


for i in file_list:
    data.append(os.path.basename(i))
    data.append(os.popen('certutil -hashfile {} MD5'.format(i)).read().strip().split('\n'))
    data.append(os.popen('certutil -hashfile {} SHA256'.format(i)).read().strip().split('\n'))
    data.append(os.path.getsize(i))


for i in range(len(data)):
    try:
        if i > 0:
            i = i * 4
        print("Name : ", data[i])
        i = i + 1
        print("MD5 : {}".format(data[i][1]))
        i = i + 1
        print("SHA256 : {}".format(data[i][1]))
        i = i + 1
        print("SIZE : ", data[i])
    except:
        pass
