a=input("Enter:")

if a=='Hello':
    print('1 -google_kz.txt 2-google_paris.txt 3-google_uar.txt')
    b=int(input())
if  b==1:
    myfile1 = open('google_kz.txt','w')
    print("Name of a file is: ",myfile1.name)
    myfile1.write(input())
    print(myfile1)
    myfile1.close()
elif b==2:
    myfile2=open('google_paris','w')
    print("Name of a file is: ",myfile2.name)
    myfile2.write(input())
    print(myfile2)
    myfile2.close()
elif b==3:
    myfile3=open('google-uar', 'w')
    print("Name of a file is: ",myfile3.name)
    myfile3.write(input())
    print(myfile3)
myfile3.close()