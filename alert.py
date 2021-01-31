from twilio.rest import Client
import serial
import time
sense = serial.Serial('COM3', 9600)

account_sid = 'AC633dbb4ed2cdf9a9592a5e9e5e5151e6'  
auth_token = 'f93029443c8e8b1a84d7a519edc3a20b'
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
			to='whatsapp:+6282145401774'
        	)
		time.sleep(1)

print(message.sid)