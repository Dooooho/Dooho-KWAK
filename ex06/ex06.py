#-*-coding:cp949
x = "There are %d types of people." %10 # 10���� ������� �ִ�.
binary  = "binary" # ����
do_not = "don't" # ���� �ʴ´�.
y = "Those who know %s and those who %s" %(binary, do_not) # ������ �ƴ� ������ �𸣴� ������� �ִ�.

print x # x ���� ���
print y # y ���� ���

print "I said: %r." %x
print "I also said: '%s." %y

hilarious = False # ����� = �׸���
joke_evaluation  = "Isn't that joke so funny?! %r" # �� ����� ������� �ʴ�?

print joke_evaluation % hilarious

w = "This is the left side of..." # w = ����
e = "a string with a right side." # e = ������ ���ڿ�

print w + e