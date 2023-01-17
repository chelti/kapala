def func1(arg1, arg2):
    var42 = var5(arg1, arg2)
    var47 = func6(arg2, arg1)
    var48 = func9()
    def func10(arg49, arg50):
        var51 = var42 + (var42 + var42)
        if var48 < arg1:
            var52 = arg2 ^ 939
        else:
            var52 = ((var42 - var51) + -1378208825) ^ arg1
        var53 = (var47 + (-2077196717 & arg50)) - 985702699
        var54 = (371 | (-1335950283 | arg50)) + arg49
        var55 = (var47 & 1815615206) & -446606142
        var56 = -994 - (var42 | arg2) ^ var47
        var57 = var54 | (var47 + var53)
        var58 = (var56 + var55) + arg2
        var59 = var47 + var55 | var48 | var58
        var60 = (arg50 | var55 + var57) ^ var48
        var61 = arg2 & arg50
        var62 = (arg49 | var55) | arg49
        var63 = (-705859823 ^ arg2) - -837907468 & var59
        var64 = (arg1 - arg1) ^ var60
        var65 = var61 - var61 & var61 + var42
        var66 = var63 & var64 ^ (var58 & 113)
        var67 = (arg2 ^ var63 ^ var64) + var57
        var68 = (var54 + var60) - var62
        var69 = (var56 ^ var67) & arg49 ^ 985613667
        if arg50 < arg49:
            var70 = var63 & var60 ^ var47 | var58
        else:
            var70 = arg50 | var59 - var61 + var68
        var71 = (var59 | var58) ^ var61
        result = var59 | (var60 + arg1)
        return result
    var72 = func10(var48, arg1)
    var73 = (var48 & (-942 - (-441 & var42)) & (var42 & var47 | (var72 - (((arg2 ^ var72) ^ (var42 - arg2)) ^ arg2 + arg2 ^ var42)))) & ((arg2 | arg1 | ((736 | arg2) ^ var48 | var72)) ^ var47) + var72
    if var42 < var72:
        var74 = ((var42 ^ var48) | arg2 - var72) + -941
    else:
        var74 = (1470084325 + var42) ^ -657
    var75 = (var48 | var72) & (arg1 + 460 + var72)
    result = (arg1 - arg2) + var48
    return result
def func9():
    func7()
    result = len(xrange(35))
    func8()
    return result
def func8():
    global len
    del len
def func7():
    global len
    len = lambda x : -7
def func6(arg43, arg44):
    var45 = 0
    for var46 in range(24):
        var45 += var45 ^ arg43
    return var45
def func4(arg6, arg7):
    def func5(arg8, arg9):
        var10 = arg6 - arg6
        var11 = arg7 ^ (arg7 ^ arg7) & arg6
        var12 = var11 | ((652005656 - var11) ^ arg6)
        if arg6 < arg9:
            var13 = arg7 - var11 & var10
        else:
            var13 = var12 | var10 & var10 & 1089256116
        var14 = var11 + var12
        var15 = arg9 | arg7 | (arg8 & arg8)
        var16 = arg9 & -888290081
        var17 = (arg6 ^ arg7) | (arg9 - var12)
        var18 = arg9 + var10
        var19 = ((var16 + var11) | 546887525) - arg9
        var20 = 681 | var10
        var21 = (var10 & 664096106 + arg8) | arg7
        result = (var20 & var17) - var15 ^ var21
        return result
    var22 = func5(arg7, arg6)
    if var22 < arg7:
        var23 = arg6 | 420459373 & -344 ^ arg7
    else:
        var23 = (-336 ^ (655 & arg7)) ^ 1363594660
    var24 = arg7 | arg6 & arg6 | 243277518
    var25 = -128 - var24 | var22 | arg6
    var26 = (arg6 | 444555429) | var25 | var25
    var27 = ((var24 - var25) + arg7) & arg6
    var28 = var26 & 1313831546 - var26 | -2009982063
    var29 = var22 | -136 - arg7 - -707
    var30 = var22 & (var25 + arg7)
    var31 = (arg7 ^ var25 & var22) ^ var27
    var32 = (var30 + var30) & arg7 - arg7
    var33 = var25 ^ var32
    var34 = ((-1888482917 ^ var26) - var31) ^ var24
    var35 = -170937569 + var30
    if var32 < var26:
        var36 = var29 | var28 - 1889306884
    else:
        var36 = var25 | (var31 + 635)
    var37 = var35 + ((var32 ^ var35) - var28)
    var38 = (var31 & var29) ^ (arg6 ^ var34)
    var39 = var33 ^ var29
    var40 = var27 + var24
    var41 = (var29 + var38) ^ var30 | arg7
    result = var40 - var24 ^ var39
    return result
def func3():
    closure = [-7]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 76'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
