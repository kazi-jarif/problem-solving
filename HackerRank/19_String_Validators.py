if __name__ == '__main__':
    s = input()
    alnum=False
    alba=False
    dig=False
    low=False
    up=False
    for i in s:
        alphanumaric=i.isalnum()
        alphabatical=i.isalpha()
        digit=i.isdigit()
        lower=i.islower()
        upper=i.isupper()
        if alphanumaric==True:
            alnum=True
        if alphabatical==True:
            alba=True
        if digit==True:
            dig=True
        if lower==True:
            low=True
        if upper==True:
            up=True
    if alnum==True:
        print("True")
    else:
        print("False")
    if alba==True:
        print("True")
    else:
        print("False")
    if dig==True:
        print("True")
    else:
        print("False")
    if low==True:
        print("True")
    else:
        print("False")
    if up==True:
        print("True")
    else:
        print("False")
    