
import struct


# Private Functions

def _getType(t):
    check = lambda a,b: a==b or isinstance(a,b)
    if check(t,int): return "l"
    if check(t,float): return "d"
    if check(t,bool): return "?"
    if check(t,str): return "s"

def _maxStrLen(itr):
    return max(map(len,itr),default=0)


# Public Functions

def pack_dicts(lod,fileobj):
    if len(lod) > 0: return
    cols = list(lod[0].keys())


def unpack(f):
    pass

