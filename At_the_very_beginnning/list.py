# -*- coding: utf-8 -*-

"""
step 1: Giving a descriptive name to the list
step 2: Storing a bunch of values inside of the lists

"""
friends = ['Hesse','Zhu',2,False]
friends[0] = 'Herman'
print(friends)
print(friends[0])
print(friends[-1])
print(friends[1:])

# list function

luck_num = [4,7,13,34]
friends.extend(luck_num)
print(friends)
friends.append('myself')
print(friends)
friends.insert(1,'Kelly')
print(friends)
friends.remove('Zhu')
print(friends)
friends.pop() # remove the last one
print(friends.index('Herman'))
friends.clear() #clc
print(friends)