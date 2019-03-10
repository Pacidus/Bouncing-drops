/*************************************************************
Motor Shield 1-Channel DC Motor Demo
by Randy Sarafan

For more information see:
https://www.instructables.com/id/Arduino-Motor-Shield-Tutorial/

*************************************************************/

float P2 = 1000.0/300;
float P1 = 1000.0/80 - (2*P2);

void setup() {
  //Setup Channel A
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  analogWrite(3, 255);   //Spins the motor on Channel A
  //Setup Channel B
  //pinMode(13, OUTPUT); //Initiates Motor Channel B pin
  //pinMode(8, OUTPUT); //Initiates Brake Channel B pin
  //digitalWrite(13, HIGH); //Establishes forward direction of Channel B
  //digitalWrite(8, LOW);   //Disengage the Brake for Channel B
  //analogWrite(11, 255);  //Spins the motor on Channel B
}

void loop(){
  
  //forward @ full speed
  digitalWrite(12, HIGH); //Establishes forward direction of Channel A
  
  delay(P2);
  
  digitalWrite(12, LOW); //Establishes forward direction of Channel A
  
  delay(P1);
}
