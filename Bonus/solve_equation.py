import math

def msqrt(y):
    
    i = 1
    while 1:
        i += 1
        if i * i >= y:
            break

    x = (i + y / i) / 2
    return x

def checkDelta(res,cst):
    
    delta = res
    for i in res.keys():
        if i == 0:
            cst+=res[i]
            del res[i]
    if res.get(1):
        b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    else:
        a = 0
    delta = (b*b  - (4 * a * cst))
    return delta


def twoSolution(res,delta):
    a=b=0
    if res.get(1):
      b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    return x1, x2

def oneSolution(res,bigC):
    a = b = 0
    if res.get(1):
      b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
        x = -b/(2*a)
    else:
        x= bigC/b
    return x

def complexSolution(res,delta):
    if res.get(1):
     b = res[1]
    else:
        b = 0
    if res.get(2):
        a = res[2]
    alpha = str(round(-b/(2*a),6))
    betha = str(- round(msqrt(abs(delta))/(2*a),6))
    gamma = str(round(msqrt(abs(delta))/(2*a),6))
    if betha[0] == '-':
        x1 = alpha + " - " + betha[1:] + "i"
    else:
        x1 = alpha  + " + " + betha + "i"
    if gamma[0] == '-':
        x2 = alpha + " - " + gamma[1:] + "i"
    else:
        x2 = alpha + " + " + gamma + "i"

    return x1, x2

def firstDegre(res, bigC):

    x = - (bigC / res[1])
    return x
