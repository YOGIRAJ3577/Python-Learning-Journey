#List are mutable, ordered sequence of elements. It can hold any type of data. It is defined by using square brackets [].
Marks = [96, 94,85,90,99]

print(Marks[0]) # 96

print(Marks, type(Marks)) # [96, 94, 85, 90, 99] <class 'list'>
print(Marks[1:3])

Marks.append(100)
print(Marks)

Marks.insert(2, 98)
print(Marks)

print(98 in Marks)