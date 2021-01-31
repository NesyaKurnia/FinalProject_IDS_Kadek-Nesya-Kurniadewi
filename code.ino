int rainDetector = A0;
int sensorReading = 0;
int buzzer = 10;
int led = 11;

void setup() {
  Serial.begin(9600);
  pinMode(rainDetector, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);
}

void loop() {
  sensorReading = analogRead(rainDetector);
  Serial.println(sensorReading);
  if(sensorReading < 500){
    digitalWrite(buzzer, HIGH);
    digitalWrite(led, HIGH);
  }
  else{
    digitalWrite(buzzer, LOW);
    digitalWrite(led, LOW);
  }
  delay(3000);
}
