// these constants describe the pins. They won't change:
const int xpin = A3;                  // x-axis of the accelerometer
const int ypin = A2;                  // y-axis
const int zpin = A1;                  // z-axis (only on 3-axis models)

// Si les fonctions ne sont pas définies (improbable), nous les ajoutons nous-même
#ifndef cbi
#define cbi(sfr, bit) (_SFR_BYTE(sfr) &= ~_BV(bit))
#endif
#ifndef sbi
#define sbi(sfr, bit) (_SFR_BYTE(sfr) |= _BV(bit))
#endif

void setup() {
  // initialize the serial communications:
  Serial.begin(115200);
  
  /*
  // Réutilisation du même rapport de 128
  sbi(ADCSRA, ADPS2);
  sbi(ADCSRA, ADPS1);
  sbi(ADCSRA, ADPS0);
  */
  //Utilisation du rapport de 16
  sbi(ADCSRA, ADPS2);
  cbi(ADCSRA, ADPS1);
  cbi(ADCSRA, ADPS0);
}

void loop() {
  // print the sensor values:
  Serial.print(analogRead(xpin));
  // print a tab between values:
  Serial.print(" ");
  Serial.print(analogRead(ypin));
  // print a tab between values:
  Serial.print(" ");
  Serial.println(analogRead(zpin));
  // delay before next reading:
}
