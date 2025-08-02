course={'PHP':{'duration':'1 Months','fees':10},
        'JAVA':{'duration':'8 Months','fees':1000},
        'Python':{'duration':'3 Months','fees':100}}
print(course)
print(course['PHP'])
course['JAVA']['duration']='11 months'
print(course['PHP']['fees'])
for k,v in course.items():
    print(k,v['duration'],v['fees'])