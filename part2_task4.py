h=int(input('Input hour:'))
m=int(input('Input minute:'))
s=int(input('Inpute sec:'))
h1=int(input('Input 2-hour:'))
m1=int(input('Input 2-minute:'))
s1=int(input('Inpute 2-sec:'))
total=m*60+h*3600+s
total1=m1*60+h1*3600+s1
#if total1>total:
print('Between first time and second time',total-total1,'seconds')
#else:
    #print('First time must be bigger, repeat again')
