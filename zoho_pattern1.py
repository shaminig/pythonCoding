    bjykiqkdef zohoPattern1():
    a = [10, 36, 54, 89, 12]
    print(str(a))
    a = orderElements(a)
    n = len(a)
    sum = 0
    for i in range(0, n):
        if a[i] % 4 == 0 and a[i] % 6 == 0:
            print("<" + str(a[i]) + ", 3>")
            sum += a[i]
        elif a[i] % 2 == 0:
            print("<" + str(a[i]) + ", 4>")
            sum += a[i]
        elif checksquare(n):
            print("<" + str(a[i]) + ", 5>")
            sum += a[i]
    print("Total sum is : " + str(sum))


def checksquare(n):
    for j in range(1, n):
        if j * j == n:
            return True
    return False


def orderElements(a):
    int
    temp = 0
    for (int i = 0; i < a.length; i++):
        for (int j = i + 1; j < a.length; j++):
            if (a[i] > a[j]):
                temp = a[i]
                a[i] = a[j]
                a[j] = temp
    return a


zohoPattern1()
