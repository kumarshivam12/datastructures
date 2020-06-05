string = "ABCDCDCabgvfrCDC"
substring = "CDC"

def count_substring(string,sub_string):
    len1 = len(string)
    len2 = len(sub_string)
    counter = 0
    for i in range(len1):
        if(string[i] == sub_string[0]):
            if(string[i:i+len2] == sub_string):
                counter += 1
    return counter
print(count_substring(string,substring))
