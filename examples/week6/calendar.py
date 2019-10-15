
# coding: utf-8

# In[1]:


def Calander1(month,day):
    a=month
    b=day
    m={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    M=['January','February','March','April','May','June','July','August','September','Octobor','November','December']
    print(M[a-1].center(20,' ')+' '*6+M[a].center(20,' ')+' '*6+M[a+1].center(20,' '))
    d="Mo Tu We Th Fr Sa Su"
    s=' '*6
    print(d+s+d+s+d)
    S=[]
    l=' 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31'
    for i in range(3):
        y=(m[a]-7+b)%7
        q=(31-m[a])*3
        L=(b)*'   '+l[:len(l)-q]+'   '*(7-y)
        S.append(L)
        a+=1
        b=y
        #print(b)
        #print(L)
    while S[0] and S[1] and S[2]:
    #while S[0]:
        print(S[0][:20]+s+S[1][:20]+s+S[2][:20])
        S[0]=S[0][21:]
        S[1]=S[1][21:]
        S[2]=S[2][21:]
    if S[0]:
        print(S[0])
    if S[1]:
        print(' '*26+S[1])
    if S[2]:
        print(' '*52+S[2])
        
        
    return b
print(2019)
x=Calander1(1,1)
for i in [4,7,10]:
    x=Calander1(i,x)

