def big_c(const, res):
    big_c = 0
    for i in const:
        big_c += float (i)
    keys = list(res)
    for i in keys:
        if i == 0:
            big_c+=res[i]
            del res[i]
    # for i in keys:
    #     if res[i] == 0:
    #         del res[i]
    return big_c

def  ReduceEquation(coefficients, exponents):
    
    res = {}
    for  key in exponents:
        for value in coefficients:
            if key in res:
                res[int (key)] += value
            else:
                res[int (key)] = value
            coefficients.remove(value)
            break
    return res