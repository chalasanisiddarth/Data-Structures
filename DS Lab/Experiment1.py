#linear search
def linear(list,element):

    flag=0
    for i in range(0,len(list)):
        if list[i]==element:
            return i
            flag+=1
            break
    if flag==0:
        return 0

list=[2,5,34,179,41,59,57,10]
element=int(input())
result=linear(list,element)
if result==0:
    print("element not found")
else:
    print("element found at",result)