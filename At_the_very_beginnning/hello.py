# coding:utf-8
# Working with strings
character_name = 'ZHu'
uni = 'SUFE'
is_male = True
print('This is a story about an economics student')
print('He wants to get PHD in ' + uni + ',')
print('But ' + character_name + ' never works hard to get what he want')
print( character_name + ' was born to fail')
print(uni.lower().islower()) # turn all characters in uni into lower and judge whether they are all lower letter
print(len(uni)) # the lenghth of variable uni
print(character_name[0]) #index the 1st letter of variable
print(uni.index('SUFE')) #index the word or letter, from which letter it starts
print(uni.replace('SUFE','Tsinghua_U')) # replace A with B for variable uni

# Working with numbers
my_num = 5
print(4+5.5-9*2/2+2*(2+2)+my_num)
print(100%3) #mod, print the reminder