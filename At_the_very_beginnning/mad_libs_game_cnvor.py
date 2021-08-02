#coding=utf-8

import sys

print("MAD LIB GAME")
print("请根据提示输入以下问题的答案\n")

guy = input("一个男名人的名字: ")
girl = input("一个女名人的名字: ")
food = input("你最喜欢的食物: ")
ship = input("一架宇宙飞船的名字: ")
job = input("一个职业名称: ")
planet = input("一个星球名称: ")
drink = input("你最喜欢的饮料: ")
number = input("一个从1到10的数字: ")

story = "\n一对著名的已婚夫妇, GUY和GIRL, 前往PLANET这颗星球去度假. 他们乘坐SHIP飞船花费了NUMBER星期才来到了那里. 他们一边吃着FOOD, 一边喝着DRINK, 一边享受着豪华的烛光晚餐. 他们为了JOB的工作>，所以不得不缩短假期. "

story = story.replace("GUY", guy)
story = story.replace("GIRL", girl)
story = story.replace("FOOD", food)
story = story.replace("SHIP", ship)
story = story.replace("NUMBER", number)
story = story.replace("DRINK", drink)
story = story.replace("PLANET", planet)
story = story.replace("JOB", job)

print(story)