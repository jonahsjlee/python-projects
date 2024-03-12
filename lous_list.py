'''
Name: Jonah Lee
Computing ID: wkx9ff
'''

import urllib.request
url = "http://arcanum.cs.virginia.edu/cs1110/files/louslist/"

def instructor_lectures(department, instructor):
    classes = []
    link = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + department)
    data_list = link.readlines()
    for data in data_list:
        data = str(data)
        list_2 = data.split("|")
        if list_2[4].split('+')[0] == instructor and list_2[5] == "Lecture" and list_2[3] not in classes:
            classes.append(list_2[3])
    return classes

def compatible_classes(first_class, second_class, needs_open_space=False):
    first_data = []
    second_data = []

    #Differentiates departments
    class1 = first_class.split(" ")
    dept1 = class1[0]
    code1 = class1[1].split("-")[0]
    section1 = class1[1].split("-")[1]

    class2 = second_class.split(" ")
    dept2 = class2[0]
    code2 = class2[1].split("-")[0]
    section2 = class2[1].split("-")[1]

    link1 = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + dept1)
    link2 = urllib.request.urlopen("http://arcanum.cs.virginia.edu/cs1110/files/louslist/" + dept2)


    #Makes lists of each field
    data1_list = link1.readlines()
    for data in data1_list:
        list = data.decode('utf-8').strip().split("|")
        if list[0] == dept1 and list[1] == code1 and list[2] == section1:
            first_data = list

    data2_list = link2.readlines()
    for data in data2_list:
        list = data.decode('utf-8').strip().split("|")

        if list[0] == dept2 and list[1] == code2 and list[2] == section2:
            second_data = list

    if needs_open_space == True:
        if int(first_data[15]) >= int(first_data[16]) or int(second_data[15]) >= int(second_data[16]):
            return False

    days1 = [first_data[7], first_data[8], first_data[9], first_data[10], first_data[11]]
    days2 = [second_data[7], second_data[8], second_data[9], second_data[10], second_data[11]]

    for i in range(0, len(days1)):
        if days1[i] == "true" and days2[i] == "true":
            if int(first_data[12]) <= int(second_data[12]) <= int(first_data[13]):
                return False
            elif int(first_data[12]) <= int(second_data[13]) <= int(first_data[13]):
                return False
            elif int(second_data[12]) <= int(first_data[12]) <= int(second_data[13]):
                return False
            elif int(second_data[12]) <= int(first_data[13]) <= int(second_data[13]):
                return False
    return True





