#!/usr/bin/env python
# coding: utf-8

# In[60]:


##练习一

def printtable(number):
    b = 0
    while(b<number):
        b += 1
        a = 1
        while ( a<=b ):
            c = a * b
            print('%d ×%2d =%2d' % (a,b,c),end='  ')
            a += 1 
        print("\n")

number = int(input("请输入1~9中任一数字"))
if (0<number<10):
    print("打印",number,"x",number,"乘法表")
    printtable(number)
else:print("Error!")
    
    


# In[ ]:





# In[ ]:




