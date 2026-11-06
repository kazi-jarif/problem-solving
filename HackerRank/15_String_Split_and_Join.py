def split_and_join(line):
    li=line.split(" ")
    li_st="-".join(li)
    return li_st

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)