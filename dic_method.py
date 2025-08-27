d1= {'name': 'prachi', 'age': '21', 'subject': 'python', 'add': 'js', 'ch': (1, 2), 'ch_name': ['intro', 'history']}
d2= {'name': 'nency', 'age': '21', 'subject': 'cyber security'}
d2.clear()
print(d1)
print(d2)
d2=d1.copy()
print("d2 copy of d1",d2)
print("d1.get('ch')",d1.get('ch',0))
print('d1.get("add")',d1.get('add','did not exist'))
print(d1.items()) 
print(d1.keys())
print(d1.values())
print(d1.fromkeys('subject',[147852,'hello']))
print(d2.pop('subject'))
print('d2',d2)
print(d2.popitem())
print(d2)
d2.update({'age':'20'})
print(d2)


