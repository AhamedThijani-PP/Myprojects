void setup() {
pinMode(2,OUTPUT);
pinMode(7,INPUT);
Serial.begin(9600);
}
void loop() {
int r=digitalRead(7);
if(r==HIGH){
  Serial.println("It is dark.LED is turned ON");
  digitalWrite(2,HIGH);
}
else{
  Serial.println("It is day.LED is turned OFF");
  digitalWrite(2,LOW);
}
delay(1000);
}
