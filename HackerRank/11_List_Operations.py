if __name__ == '__main__':
    N = int(input())
    task=[]
    for i in range(N):
        work=input()
        work_list=work.split()
        if work_list[0]=="insert":
            task.insert(int(work_list[1]),int(work_list[2]))
        elif work_list[0]=="print":
            print(task)
        elif work_list[0]=="remove":
            task.remove(int(work_list[1]))
        elif work_list[0]=="append":
            task.append(int(work_list[1]))
        elif work_list[0]=="sort":
            task.sort()
        elif work_list[0]=="pop":
            task.pop()
        else:
            task.reverse()