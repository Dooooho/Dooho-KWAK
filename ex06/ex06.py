#-*-coding:cp949
x = "There are %d types of people." %10 # 10명의 사람들이 있다.
binary  = "binary" # 진수
do_not = "don't" # 하지 않는다.
y = "Those who know %s and those who %s" %(binary, do_not) # 진수를 아는 사람들과 모르는 사람들이 있다.

print x # x 값을 출력
print y # y 값을 출력

print "I said: %r." %x
print "I also said: '%s." %y

hilarious = False # 들썩들썩 = 그릇된
joke_evaluation  = "Isn't that joke so funny?! %r" # 그 농담이 재미있지 않니?

print joke_evaluation % hilarious

w = "This is the left side of..." # w = 왼쪽
e = "a string with a right side." # e = 우측의 문자열

print w + e