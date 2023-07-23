#Megre sort
def merge_sort(lst,i,j):
    if i>=j:
        return
    middle=(i+j)//2
    merge_sort(lst,i,middle)
    merge_sort(lst,middle+1,j)
    Merge(lst,i,j,middle)
    
    
def Merge(lst,i,j,middle):
    l_lst=lst[i:middle+1]
    r_lst=lst[middle+1:j+1]
    l_index=0
    r_index=0
    sort_index=i
    while l_index<len(l_lst) and r_index<len(r_lst):
        if l_lst[l_index]<=r_lst[r_index]:
            lst[sort_index]=l_lst[l_index]
            l_index += 1
            sort_index += 1
        else:
            lst[sort_index]=r_lst[r_index]
            r_index += 1
            sort_index += 1
            
        
    while l_index<len(l_lst):
        lst[sort_index]=l_lst[l_index]
        l_index+=1
        sort_index+=1
    while r_index<len(r_lst):
        lst[sort_index]=r_lst[r_index]
        r_index+=1
        sort_index+=1
def main():
    n=int(input("enter the size of the list\n"))
    li=[]
    print("enter the list elements")
    for i in range(n):
        li.append(int(input()))
    merge_sort(li,0,n-1)
    print(li)
main()