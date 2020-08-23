import csv
import json

from django.core.files.uploadedfile import InMemoryUploadedFile

'''
input csv
question,answer
q1,a1
q2,a2
out json 
[{
question:'', 
answer: ''
}]
'''
def csvToJson(fileObj: InMemoryUploadedFile):
    res = []
    for line in fileObj.readlines():
        ques, ans = str(line.decode('utf-8')).split(',')
        res.append({'question': ques.strip(),'answer': ans.strip()})
    return res