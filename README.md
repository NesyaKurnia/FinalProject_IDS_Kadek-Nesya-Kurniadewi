# Final Project mata kuliah Intrusion Detection System
## Mendeteksi Hujan dengan Raindrops Sensor
### *Kadek Nesya Kurniadewi (05311840000009)*

#### Alat yang diperlukan
- Arduino UNO
- Raindrops Sensor
- LED
- Buzzer
- Jumper wire
#### Application
- Arduino UNO
#### Langkah-langkah :
1. Install aplikasi Arduino UNO pada laptop
2. Masukkan code pada aplikasi arduino, kemudian compile untuk memastikan tidak ada error pada code
3. Merangkai alat dengan rangkaian seperti dibawah ini :
  - Sensor **A0** = Arduino **A0 pin**
  - Sensor **GND** = Arduino **GND pin**
  - Sensor **VCC** = Arduino **5V pin**
  - LED **+ive** = Arduino **11 pin**
  - LED **-ive** = Arduino **GND pin**
  - Buzzer **+ive** = Arduino **10 pin**
  - Buzzer **-ive** = Arduino **GND pin**

![rangkaianalat](https://github.com/NesyaKurnia/FinalProject_IDS_Kadek-Nesya-Kurniadewi/blob/main/image/rangkaianalat.jpg)

4. Upload code pada Arduino IDE ke Arduino, buka Serial Monitor untuk memastikan input dari sensor terbaca atau tidak
5. Meneteskan air pada raindrops sensor. Ketika tidak ada tetesan / rintik hujan, output digital **bernilai tinggi**, lampu deteksi dan buzzer *mati*. Ketika terdeteksi tetesan air hujan, output digital mengeluarkan **nilai rendah** sehingga lampu deteksi dan buzzer *menyala*.
#### Alert Message
1. Melakukan registrasi pada akun twilio, caranya bisa dilihat pada [link ini](https://create.arduino.cc/projecthub/highvoltages/arduino-whatsapp-messages-send-whatsapp-messages-using-pi-605f52)
2. Setelah memiliki akun twilio, selanjutnya melakukan install twilio library yaitu dengan command `pip install twilio`
3. Membuat code API. Code dapat dilihat [disini](https://github.com/NesyaKurnia/FinalProject_IDS_Kadek-Nesya-Kurniadewi/blob/main/alert.py)
4. Menjalankan program python pada command prompt dengan command `python "namafile".py`
5. Output akan langsung masuk ke whatsapp yang dituju, seperti tampilan dibawah ini :

![](https://github.com/NesyaKurnia/FinalProject_IDS_Kadek-Nesya-Kurniadewi/blob/main/image/alert.jpg)

TERIMA KASIH ^-^
