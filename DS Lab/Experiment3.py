#bubble sort
def bubble(list):

    for i in range(0,len(list)):
        for j in range(0, len(list)-i-1):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    return list

list=[3,6,1,7,8,99,14,5]
print("Sorted List : ", bubble(list))