

def collatz_conjecture(num):
    initnum = num
    step = 0
    while num >1:
        step = step + 1
        if (num%2 == 0):
            num = num/2
        else:
            num = (num*3)+1

    return "The collatz steps for {} is {}".format(initnum, step)

