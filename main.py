def f10(n, l, a, x):
    if n > 0:
        a.append(n%x)
        f10(n // x, l + 1, a, x)
    else:
        print('Base= '+str(x))
        print('Level= ' + str(l))
        for i in reversed(a):
            print(i, end='')
    return a
def main():
    n = int(input('n='))
    a = []
    l=1
    f10(n, l, a,2)
    print('')
    a.clear()
    f10(n, l, a,8)
    print('')
    a.clear()
    f10(n,l,a,5)

if __name__=='__main__':
    main()