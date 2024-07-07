import os

def is_valid_json(content):
    result = False
    if content[0] == "{" and content[-1] == "}":
        result = True
    return result

def create_dict(contentArr):
    index = 0
    arrSize = len(contentArr)
    result = {}
    while index < arrSize:
        key = contentArr[index].strip('"')
        value = contentArr[index+1].strip('"')
        result[key] = value
        index = + 2
    return result


        
# read file
# determine if json is valid 
# go through json  key after key and look up keys of keys
def parse(path):
    fd = os.open(path,os.O_RDONLY)
    content = os.read(fd,50)
    content_str = content.decode("utf-8")
    if is_valid_json(content_str):
        print("valid json")
        keys = content_str[1:-1]
        keyArr = keys.split(":")
        res = create_dict(keyArr)
        print(res)
    os.close(fd)
    