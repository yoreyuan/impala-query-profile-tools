#
# Autogenerated by Thrift Compiler (0.12.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys
import ErrorCodes.ttypes

from thrift.transport import TTransport
all_structs = []


class TStatus(object):
    """
    Attributes:
     - status_code
     - error_msgs

    """


    def __init__(self, status_code=None, error_msgs=None,):
        self.status_code = status_code
        self.error_msgs = error_msgs

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.status_code = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.LIST:
                    self.error_msgs = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.error_msgs.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('TStatus')
        if self.status_code is not None:
            oprot.writeFieldBegin('status_code', TType.I32, 1)
            oprot.writeI32(self.status_code)
            oprot.writeFieldEnd()
        if self.error_msgs is not None:
            oprot.writeFieldBegin('error_msgs', TType.LIST, 2)
            oprot.writeListBegin(TType.STRING, len(self.error_msgs))
            for iter6 in self.error_msgs:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.status_code is None:
            raise TProtocolException(message='Required field status_code is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(TStatus)
TStatus.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'status_code', None, None, ),  # 1
    (2, TType.LIST, 'error_msgs', (TType.STRING, 'UTF8', False), None, ),  # 2
)
fix_spec(all_structs)
del all_structs
