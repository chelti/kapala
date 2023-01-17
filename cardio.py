def func1(arg1, arg2):
    var7 = func2(arg2, arg1)
    var44 = var10(arg1, var7)
    result = arg1 ^ arg2
    return result
def func5(arg11, arg12):
    var13 = func8()
    var16 = class9()
    for var17 in xrange(19):
        var18 = var16.func10
        var18(var13, var17)
    var19 = 382 - (var13 - var13 - arg12)
    var20 = arg11 + (var13 + 538 + arg12)
    var21 = 973 & (var20 | 1771909902)
    var22 = var13 | -1423403359 + var13 + -855
    var23 = (-740 | var19) & 899480627 | var20
    var24 = -887 | arg12 & var22
    var25 = var13 | var22 + var13
    var26 = var23 - var19 | var13
    var27 = ((-540158162 & var19) & var26) + var25
    var28 = var13 & (var19 & var19) - var22
    var29 = (var27 | var25) ^ var21 - var21
    var30 = -619 & var27 + var19 ^ var23
    var31 = var27 ^ var13
    var32 = (var24 ^ var30 ^ var22) + var29
    if var31 < var27:
        var33 = var19 | arg12
    else:
        var33 = arg11 ^ var25
    var34 = (var28 & var22 - var26) - var25
    var35 = (var27 + (var13 | var30)) & var24
    var36 = var22 + -559525565 & var21
    var37 = var24 - var24
    var38 = (var28 | var21) + var30
    var39 = var35 ^ var13
    var40 = var30 - (var39 - var28) + -1628787495
    var41 = var22 + var21 + var22 ^ var13
    var42 = (var25 + (var37 - var35)) + arg11
    var43 = (var22 - var31 | arg12) + arg11
    result = var34 ^ var41 ^ var29
    return result
class class9(object):
    def func10(self, arg14, arg15):
        return 0
def func8():
    func6()
    result = len(range(26))
    func7()
    return result
def func7():
    global len
    del len
def func6():
    global len
    len = lambda x : -6
def func4():
    closure = [0]
    def func3(arg8, arg9):
        closure[0] += func5(arg8, arg9)
        return closure[0]
    func = func3
    return func
var10 = func4()
def func2(arg3, arg4):
    var5 = 0
    for var6 in [var5 ^ (-6 - -1) for i in range(17)]:
        var5 += arg4 - var5
    return var5
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 11'
    print 'arg_number: 45'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
