import sys
import binascii

class sovico_DRG116:
    def __init__(self,id,data):
        self.bit_Binary_Array = ['0000','1000','0100','0010','0001','1100','1010','1001','0110','0101','0011','1110','1101','1011','0111','1111']
        self.bit_index = [0,1,2,4,8,3,5,9,6,10,12,7,11,13,14,15]
        self.data = data
        setlist = self.data.split(',')
        id = ('a{}'.format(id))
        address1 = self.binaryValue40(''.join(setlist[0:4]))
        address2 = self.binaryValue30(''.join(setlist[4:8]))
        address3 = self.binaryValue40(''.join(setlist[8:12]))
        address4 = self.binaryValue30(''.join(setlist[12:16]))
        self.setString = '029390{0}{1}{2}{3}{4}304030403040304003'.format(id,address4,address3,address2,address1)
        #self.setString = binascii.unhexlify(self.setString)

    def drg116(self):
        return (self.setString)

    def binaryValue40(self, data):
        for i, line in enumerate(self.bit_Binary_Array):
            if line == data:
                byteReturn = hex(self.bit_index[i] + 64)
                return byteReturn[2:]

    def binaryValue30(self, data):
        for i, line in enumerate(self.bit_Binary_Array):
            if line == data:
                byteReturn = hex(self.bit_index[i] + 48)
                return byteReturn[2:]

if __name__ == "__main__":
    print ("Start")
    main = sovico_DRG116(1, '00000011')