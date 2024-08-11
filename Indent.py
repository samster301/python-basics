#y = [(v*v + i) for i,v in enumerate((4,3,6,3,6))]
#print(y)


from asyncio.windows_events import NULL
import string


def reverse(strg):
    revStr = [strg[len(strg) -1 -i] for i in range(len(strg))]
    return ''.join(revStr)


    
    