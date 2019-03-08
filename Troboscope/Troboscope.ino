/*************************************************************
Motor Shield 1-Channel DC Motor Demo
by Randy Sarafan

For more information see:
https://www.instructables.com/id/Arduino-Motor-Shield-Tutorial/

*************************************************************/
float P = 1000.0/80.0;

void setup() {
  //Setup Channel A
  pinMode(12, OUTPUT); //Initiates Motor Channel A pin
  pinMode(9, OUTPUT); //Initiates Brake Channel A pin
  digitalWrite(12, HIGH); //Establishes forward direction of Channel A
  digitalWrite(9, LOW);   //Disengage the Brake for Channel A
  //Setup Channel B
  pinMode(13, OUTPUT); //Initiates Motor Channel B pin
  pinMode(8, OUTPUT); //Initiates Brake Channel B pin
  digitalWrite(13, HIGH); //Establishes forward direction of Channel B
  digitalWrite(8, LOW);   //Disengage the Brake for Channel B
}

void loop(){
  
  //forward @ full speed
  analogWrite(3, 255);   //Spins the motor on Channel A
  analogWrite(11, 255);  //Spins the motor on Channel B
  
  delay(P);

  analogWrite(3, 0);  //Stop the motor on Channel A
  analogWrite(11,0);  //Stop the motor on Channel B
  delay(P);
}
