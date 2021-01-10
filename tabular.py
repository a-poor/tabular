
import struct




def dumps():
    pass

def loads():
    pass

def dump(data,fo):
    fo.write(dumps(data))

def load(fo):
    return loads(fo.read())

