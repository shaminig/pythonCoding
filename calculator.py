def main():
    print(__name__)
    while True:
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        choice=input("enter the operation to perform")
        if((choice=='q') or (choice=='Q')):
            break
        n1=int(input("Enter 1st num"))
        n2=int(input("enter 2nd num"))
        if(choice=='1'):
            add(n1, n2)
        elif(choice=='2'):
            subt(n1, n2)
        elif(choice=='3'):
            mul(n1, n2)
        elif(choice=='4'):
            div(n1, n2)
def add(n1, n2):
    result = n1 + n2
    print(result)
def subt(n1, n2):
    result = n1-n2
    print(result)
def mul(n1, n2):
    result = n1 *n2
    print(result)
def div(n1, n2):
    result = n1 / n2
    print(result)

if __name__ == "__main__":
    main()
