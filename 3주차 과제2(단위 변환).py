def get_number(message1):
    ### do not edit here ###
    num = input(message1)
    while not num.isdigit():
        num = input(message1)
    return int(num) 


def centi2inch():
    
    print('-centimeter to inch')
    a=int(input("input number(centimeter) : "))

    return print("%dcm -> %.2finch"%(a,a/2.54)) 

def inch2centi():

    print('-inch to centimeter')
    a=int(input("input number(inch) : "))

    return print("%dinch -> %.2fcm"%(a,a*2.54))


def choose_scale(): 
    # get 1 or 2 as input (centi to inch or inch to centi)

    print('# centimeter to inch = 1')
    print('# inch to centimeter = 2')
    
    sc=input("choose 1 or 2 : ")

    while not (sc=="1" or sc=="2"):
        sc=input("choose 1 or 2 : ")

    return sc


def continues():
    
    cont=input("Wanna continue? (y/n)")
    while not(cont=="y" or cont=="n"):
        cont=input("Wanna continue? (y/n)")

    return cont=='y'


def changeScale():
    ### do not edit here ###
    sc = choose_scale()
    if sc == '1':
        centi2inch()
    elif sc == '2': 
        inch2centi()


# make sure changeScale() iterate until user wants to stop
def main():
    On = True
    while On:
        changeScale()

        if continues():
            continue
        else:
            break

main()
