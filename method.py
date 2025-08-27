s1 = ["am","is","are","was",147,"were","had","python",147,147]
s2 = [159,147,158,123,148]
s3 = [159,147,158,123,148]
print(s1)
s1.append('we')
print(s1)  
s1.extend('hello')
print(s1)
s1.insert(3,159)
print(s1)
s1.pop(6)
print(s1)
s2.clear()
print(s1.index('are'))
print(s1.count(147))
s3.sort()
print(s3)
s3.reverse()
print(s3)
s4 = s1.copy()
print(s4)


