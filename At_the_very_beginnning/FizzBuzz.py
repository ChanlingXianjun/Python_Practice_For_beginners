# -*- coding: utf-8 -*-
"""
:author: lihui
:website: withlihui.com
Let computer guess a number
:edition: This one looks like the game I played in junior high school, en lecturer told us to call out number
and replace number which is the multiples of 7 with a clap
"""
numbers = range(1,101)

for i in numbers:
    if i%3==0 and i%5==0:
        print ('FizzBuzz')
    elif i%3==0:
        print ('Fizz')
    elif i%5==0:
        print ('Buzz')
    else:
        print (i)