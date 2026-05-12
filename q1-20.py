'''
#WAP to sum all the items in a given list
def listsum(lst):
    sum_list = 0
    for i in lst:
        sum_list += i
    return sum_list


def main():
    lista = []
    a = int(input("Enter total elements you want = "))
    for i in range(0,a,1):
        new = int(input(f"Enter {i+1} numbers"))
        lista.append(new)
    print(f"Your list formed is : {lista}")
    sum_new = listsum(lista)
    print(f"Sum of all elements in your list is : {sum_new}")

if __name__ == "__main__":
    main()

'''    
#WAP to count all strings in a list of strings
def str_count(lst):
    counter = 0
    for i in lst:
        #if isinstance(i,str):''''''
            counter += 1
    return counter

def main():
    a = int(input("Enter how many string you want in list : "))
    str_lst=[]
    for i in range(0,a,1):
        strs= input("Enter a string: ")
        str_lst.append(strs)
    print(f"Your list of strings is:{str_lst}")

    count_str = str_count(str_lst)
    print(f"Total number of strings in the list is {count_str}")

main()