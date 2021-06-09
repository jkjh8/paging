import sys
import binascii



class blueRg:
    def __init__(self,id,data):
        self.setList = [0x02,0x02,0xfd,0x01,0x39,0x00,0x00,0x00,0x03]
        data_StringToList = data.split(',')

        data_Array_1 = data_StringToList[0:8]
        data_Array_2 = data_StringToList[8:16]
        data_Array_3 = data_StringToList[16:24]
        
        data_Array_1.reverse()
        data_Array_2.reverse()
        data_Array_3.reverse()

        self.setList[3] = int(id)

        self.setList[7] = int(''.join(data_Array_1),2)
        self.setList[6] = int(''.join(data_Array_2),2)
        self.setList[5] = int(''.join(data_Array_3),2)

        checksum = 0
        for i,v in enumerate(self.setList):
            checksum = checksum + v

        checksum = checksum & 0xff
        self.setList.append(checksum)

        self.run()

    def run(self):
        setString = ''
        for i,v in enumerate(self.setList):
            setString = setString + "{0:0>2X}".format(v)
        print (setString)
        print (self.setList)
        return setString 

if __name__ == "__main__":
    print ("Start")
    main = blueRg(2, '1,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')