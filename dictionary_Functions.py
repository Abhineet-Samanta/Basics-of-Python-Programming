d={'name':'Python', 'first Language':'Java' }
f=d.get('name')
print(f)
print(d['name'])
for a in d.keys():print(a)
for a in d.values():print(a)
del d['first Language']
print(d)
print(d.pop('name'))
print(d)
d=dict(name='Python',Language= 'JAVA')
d.update({'Language':'Java'})
print(d)
d.clear()
print(d)
#to add in dictionary
d['desc']="This is Python"
print(d)
