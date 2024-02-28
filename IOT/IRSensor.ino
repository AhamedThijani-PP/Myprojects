int IRSensor=7;
void setup() {
pinMode(7,INPUT);
Serial.begin(9600);
}
void loop() {
int sensordata=digitalRead(IRSensor);
if (sensordata==0){
Serial.println("Stop...Something is ahead");
Serial.println(sensordata);
delay(2000);
}
else{
Serial.println("Path is clear");
Serial.println(sensordata);
delay(2000);
}
}
