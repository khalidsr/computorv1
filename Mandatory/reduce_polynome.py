def big_c(const, res):
    big_c = 0
    for i in const:
        big_c += float (i)
    keys = list(res)

    for i in keys:
        if i == 0:
            big_c+=res[i]
            del res[i]

    return big_c

def ReduceEquation(coefficients, exponents):
    res = {}

    for i in range(len(exponents)): 
        key = int(exponents[i])
        value = coefficients[i]
        
        if key in res:
            res[key] += value 
        else:
            res[key] = value 
    
    return res