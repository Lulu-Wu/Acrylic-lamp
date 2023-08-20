from micropython import const

class BLEConst(object):
    class IRQ(object):
        IRQ_CENTRAL_CONNECT = const(1)
        IRQ_CENTRAL_DISCONNECT = const(2)
        IRQ_GATTS_WRITE = const(3)


    class Appearance(object):
        Unknown = const(0) # None
        GENERIC_PHONE = const(64) # Generic category
        GENERIC_COMPUTER = const(128) # Generic category


    class ADType(object):
        '''
        Advertising Data Type
        '''
        AD_TYPE_FLAGS = const(0x01) # Flags for discoverability.
        AD_TYPE_16BIT_SERVICE_UUID_COMPLETE = const(0x03) # Complete list of 16 bit service UUIDs.
        AD_TYPE_32BIT_SERVICE_UUID_COMPLETE = const(0x05) # Complete list of 32 bit service UUIDs.
        AD_TYPE_128BIT_SERVICE_UUID_COMPLETE = const(0x07) # Complete list of 128 bit service UUIDs.
        AD_TYPE_COMPLETE_LOCAL_NAME = const(0x09) # Complete local device name.
        AD_TYPE_APPEARANCE = const(0x19) # Appearance. 