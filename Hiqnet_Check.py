import sys,socket
import binascii

def hiqnet_checksum(type,nodeAddr,nodeId,parameterValue):
    checksum = 0
    substitute = []

    #SET, SUBSCRIBE, SUBSCRIBE PERCENT, BUMP PERCENT
    if type == '88' or type == '89' or type == '8D' or type == '8E' or type == '90':
        int_Array = [0]*13
        int_Array[0] = int.from_bytes(binascii.unhexlify(type),"big")
        for i,v in enumerate(nodeAddr):
            int_Array[i+1] = int.from_bytes(binascii.unhexlify(nodeAddr[i]),"big")
        id_Value = divmod(nodeId,256)
        int_Array[7] = id_Value[0]
        int_Array[8] = id_Value[1]
        parameterValue_bytes = parameterValue.to_bytes(4,'big')
        for i, v in enumerate(parameterValue_bytes):
            int_Array[i+9] = parameterValue_bytes[i]

    #UNSUBSCRIBE, UNSUBSCRIBE PERCENT
    elif type == '8A' or type == '8F':
        int_Array = [0]*9
        int_Array[0] = int.from_bytes(binascii.unhexlify(type),"big")
        for i,v in enumerate(nodeAddr):
            int_Array[i+1] = int.from_bytes(binascii.unhexlify(nodeAddr[i]),"big")
        id_Value = divmod(nodeId,256)
        int_Array[7] = id_Value[0]
        int_Array[8] = id_Value[1]

    #PARAMETER PRESET RECALL
    elif type == '8C':
        int_Array = [0]*5
        int_Array[0] = int.from_bytes(binascii.unhexlify(type),"big")
        parameterValue_bytes = parameterValue.to_bytes(4,'big')
        for i, v in enumerate(parameterValue_bytes):
            int_Array[i+1] = parameterValue_bytes[i]

    #CHECKSUM CULCURATOR
    for i,v in enumerate(int_Array):
        checksum  = checksum ^ int_Array[i]

    #SET SUBSTITUTE
    for i,v in enumerate(int_Array):
        if int_Array[i] == 2 or int_Array[i] == 3 or int_Array[i] == 6 or int_Array[i] == 21 or int_Array[i] == 27:
            int_Array[i] = (128 + v)
            substitute.append(i)
    for i,v in enumerate(substitute):
        int_Array.insert(v+i,27)

    #PACK HIQNET CODE
    int_Array.insert(0,2)
    int_Array.append(checksum)
    int_Array.append(3)

    for i,v in enumerate(int_Array):
        int_Array[i] = "%02X"%v

    #RETURN DATA
    rtString = ''.join(int_Array)
    return(rtString)

if __name__ == "__main__":
    hiqnet_checksum('88',['20','11','03','00','07','01'],33,1)