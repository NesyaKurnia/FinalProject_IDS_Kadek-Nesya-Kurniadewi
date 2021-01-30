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

![rangkaianalat](https://github.com/NesyaKurnia/FinalProject_IDS_Kadek-Nesya-Kurniadewi/blob/main/rangkaianalat.jpg)

4. Upload code pada Arduino IDE ke Arduino, buka Serial Monitor untuk memastikan input dari sensor terbaca atau tidak
5. Meneteskan air pada plat raindrops sensor, jika angka yang dibaca **1023** berarti **kondisi normal (dry/tidak ada hujan)**, jika **kurang dari 500** berarti **ada air (hujan)** dan buzzer akan berbunyi dan LED akan menyala
#### Alert Message
