import random, serial
from time import sleep


meter_value = [0]*48

def main()
	if ser.isOpen():
		radom_mt = random.randint(1,40)
		if meter_value[radom_mt] == 0:
			meter_value[radom_mt] = 1
		else meter_value[radom_mt] = 0
		return_text = ','.join(meter_value)
		ser.write('m,{},!'.format(return_text))

if __name__=="__main__":
	ser = serial.Serial('com5', 115200, timeout=1)