int smoke=A1;
void setup(){
Serial.begin(9600);
pinMode(smoke, INPUT);
pinMode(2, OUTPUT);
}
void loop(){
int ss=analogRead(smoke);
Serial.println("Smoke value is:");
Serial.println(ss);
if(ss<50)
digitalWrite(2, HIGH); else
digitalWrite(2, LOW);
delay(1000);
}
