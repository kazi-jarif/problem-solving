def swap_case(s):
    li=[]
    for i in s:
        j=i.isupper()
        if j ==True:
            k=i.lower()
            li.append(k)
        elif j == False
            k=i.upper()
            li.append(k)
        else:
            li.append(i)
    return li

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)