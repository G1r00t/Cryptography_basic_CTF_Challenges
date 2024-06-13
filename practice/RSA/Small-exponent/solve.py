from Crypto.Util.number import *

st = 15918444479466730428724746421579351578749396638612811040529655667411154134447492555232062914519585582267078927343259346511161944880745305024978384630261182
c  = 373881643430435889121617660133558570913921386270992708752951342303716978785915727289850090239186611960391755925896627419071832407861241021964078737791400479601972785358233228907716149151427216498194349130923382198373
n  = 63280074819326846331488160224720317100968601182115116766358584880263555209009248020846829115358284244596592143177675599949446728797498410136131668461860923501435133883776444372556759521515203662337957897725422291296420016362178484903165450419720112408162420735455097823260546205419409011401753223843348102397

l = 0
r = st ** 2 
while (l < r):
    mid = (l + r) >> 1
    if mid ** 2 == st ** 2 - 4 * n:
        l = mid
        r = mid 
        break
    elif mid ** 2 < st ** 2 - 4 * n:
        l = mid + 1
    else:
        r = mid - 1

p = (st + l) // 2
q = n // p 

e = 3

print(long_to_bytes(pow(c, pow(e, -1, (p - 1) * (q - 1)), p * q)))