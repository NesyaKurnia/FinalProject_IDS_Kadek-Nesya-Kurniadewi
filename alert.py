from twilio.rest import Client
import serial
import time
sense = serial.Serial('COM3', 9600)

account_sid = 'XXXXX'  
auth_token = 'XXXXX'
client = Client(account_sid, auth_token)

output_tinggi = 1024 
output_peringatan = 801
output_hujan = 501

while True:
	while sense.inWaiting():
		sensor=int(sense.readline().decode())
		if sensor < output_hujan:
			messageTosend="HUJANN DERASS!!! Angkat jemurannnn!!!. terdeteksi: "+str(sensor)
		elif (sensor > output_hujan and sensor < output_peringatan):
			messageTosend="Peringatan hujan ringan. Terdeteksi : "+str(sensor)
		elif (sensor > output_peringatan and sensor< output_tinggi):
			messageTosend="Aman tidak ada hujan. Terdeteksi : "+str(sensor) 

		message=client.messages.create(
			body= messageTosend,
			from_='whatsapp:+14155238886',
			to='whatsapp:+62821XXXXXXXX'
        	)
		time.sleep(1)

print(message.sid)
