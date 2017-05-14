#coding:utf8
#author:Rock.Wang
age_of_oldboy=56
guess_age=int(input('guess_age:'))
if guess_age==age_of_oldboy:
    print('恭喜你答对了')
elif guess_age>age_of_oldboy:
    print('抱歉你猜大了')
else :
    print('抱歉你猜小了')