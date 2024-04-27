#define SHTR_H 2           //TTL for Shutter H
#define SHTR_V 3           //TTL for Shutter V
#define SHTR_45 4          //TTL for Shutter 45
#define SHTR_135 5         //TTL for Shutter 135 
#define SHTR_PLUS 6        //TTL for Shutter +
#define SHTR_CROSS 7       //TTL for Shutter x

#define D0_PLUS A0         //Detector +0
#define D1_PLUS A1         //Detector +1
#define D0_CROSS A2        //Detector x0
#define D1_CROSS A3        //Detector x1


double val0;
double val1;
double val2;
double val3;
int i;


void setup() {

  Serial.begin(9600);
  analogReadResolution(12);

  pinMode( SHTR_H, OUTPUT);        digitalWrite(SHTR_H, LOW);
  pinMode( SHTR_V, OUTPUT);        digitalWrite(SHTR_V, LOW);
  pinMode( SHTR_45, OUTPUT);       digitalWrite(SHTR_45, LOW);
  pinMode( SHTR_135, OUTPUT);      digitalWrite(SHTR_135, LOW);
  pinMode( SHTR_PLUS, OUTPUT);     digitalWrite(SHTR_PLUS, LOW);
  pinMode( SHTR_CROSS, OUTPUT);    digitalWrite(SHTR_CROSS, LOW);
  
  pinMode( D0_PLUS, INPUT);        analogWrite(D0_PLUS, 0);
  pinMode( D1_PLUS, INPUT);        analogWrite(D1_PLUS, 0);
  pinMode( D0_CROSS, INPUT);       analogWrite(D0_CROSS, 0);
  pinMode( D1_CROSS, INPUT);       analogWrite(D1_CROSS, 0);
  Serial.flush();

}

void loop() {
}


void serialEvent() {
  if (Serial.available()) {
    i = Serial.read();
  }

  if (i == '0') {
    CALL_0();
  }
  else if (i == '1') {
    CALL_1();
  }
    else if (i == '2') {
    CALL_2();
  }
    else if (i == '3') {
    CALL_3();
  }
    else if (i == '4') {
    CALL_4();
  }
    else if (i == '5') {
    CALL_5();
  }
    else if (i == '6') {
    CALL_6();
  }
    else if (i == '7') {
    CALL_7();
  }
}


void CALL_0() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_H, HIGH);        digitalWrite(SHTR_PLUS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("H");                 Serial.print("START");              //Serial.print("           ");
  Serial.write("+");                 Serial.print("BASE");               //Serial.print("           ");
  val0 = analogRead(D0_PLUS);        Serial.print(val0);                 Serial.print("DONE");                  //Serial.print("           ");
  val1 = analogRead(D1_PLUS);        Serial.print(val1);                 Serial.print("DTWO");                  //Serial.print("           ");
  val2 = analogRead(D0_CROSS);       Serial.print(val2);                 Serial.print("DTHR");                  //Serial.print("           ");
  val3 = analogRead(D1_CROSS);       Serial.print(val3);                 Serial.print("DFOU");                  //Serial.println("           ");
  /* SHUTTER CLOSING*/
  digitalWrite(SHTR_H, LOW);         digitalWrite(SHTR_PLUS, LOW);       delay(300);
}

void CALL_1() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_V, HIGH);        digitalWrite(SHTR_PLUS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("V");                 Serial.print("START");              //Serial.print("           ");
  Serial.write("+");                 Serial.print("BASE");               //Serial.print("           ");
  val0 = analogRead(D0_PLUS);        Serial.print(val0);                 Serial.print("DONE");                 //Serial.print("           ");
  val1 = analogRead(D1_PLUS);        Serial.print(val1);                 Serial.print("DTWO");                 //Serial.print("           ");
  val2 = analogRead(D0_CROSS);       Serial.print(val2);                 Serial.print("DTHR");                 //Serial.print("           ");
  val3 = analogRead(D1_CROSS);       Serial.print(val3);                 Serial.print("DFOU");                 //Serial.println("           ");
  /* SHUTTER CLOSING*/
  digitalWrite(SHTR_V, LOW);         digitalWrite(SHTR_PLUS, LOW);       delay(300);
}


void CALL_2() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_45, HIGH);       digitalWrite(SHTR_PLUS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("D");                 Serial.print("START");              //Serial.print("           ");
  Serial.write("+");                 Serial.print("BASE");               //Serial.print("           ");
  val0 = analogRead(D0_PLUS);        Serial.print(val0);                 Serial.print("DONE");                //Serial.print("           ");
  val1 = analogRead(D1_PLUS);        Serial.print(val1);                 Serial.print("DTWO");                //Serial.print("           ");
  val2 = analogRead(D0_CROSS);       Serial.print(val2);                 Serial.print("DTHR");                //Serial.print("           ");
  val3 = analogRead(D1_CROSS);       Serial.print(val3);                 Serial.print("DFOU");                //Serial.println("           ");
  /* SHUTTER CLOSING*/
  digitalWrite(SHTR_45, LOW);        digitalWrite(SHTR_PLUS, LOW);       delay(300); 
}


void CALL_3() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_135, HIGH);      digitalWrite(SHTR_PLUS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("A");                 Serial.print("START");              //Serial.print("           ");
  Serial.write("+");                 Serial.print("BASE");               //Serial.print("           ");
  val0 = analogRead(D0_PLUS);        Serial.print(val0);                 Serial.print("DONE");                //Serial.print("           ");
  val1 = analogRead(D1_PLUS);        Serial.print(val1);                 Serial.print("DTWO");                //Serial.print("           ");
  val2 = analogRead(D0_CROSS);       Serial.print(val2);                 Serial.print("DTHR");                //Serial.print("           ");
  val3 = analogRead(D1_CROSS);       Serial.print(val3);                 Serial.print("DFOU");                //Serial.println("           ");
  /* SHUTTER CLOSING*/
  digitalWrite(SHTR_135, LOW);       digitalWrite(SHTR_PLUS, LOW);       delay(300);
}


void CALL_4() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_H, HIGH);       digitalWrite(SHTR_CROSS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("H");                Serial.print("START");               //Serial.print("           ");
  Serial.write("x");                Serial.print("BASE");                //Serial.print("           ");
  val0 = analogRead(D0_PLUS);       Serial.print(val0);                  Serial.print("DONE");                //Serial.print("           ");
  val1 = analogRead(D1_PLUS);       Serial.print(val1);                  Serial.print("DTWO");                //Serial.print("           ");
  val2 = analogRead(D0_CROSS);      Serial.print(val2);                  Serial.print("DTHR");                //Serial.print("           ");
  val3 = analogRead(D1_CROSS);      Serial.print(val3);                  Serial.print("DFOU");                //Serial.println("           ");
  /* SHUTTER CLOSING*/
  digitalWrite(SHTR_H, LOW);        digitalWrite(SHTR_CROSS, LOW);       delay(300);
}

void CALL_5() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_V, HIGH);       digitalWrite(SHTR_CROSS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("V");                Serial.print("START");               //Serial.print("           ");
  Serial.write("x");                Serial.print("BASE");                //Serial.print("           ");
  val0 = analogRead(D0_PLUS);       Serial.print(val0);                  Serial.print("DONE");                //Serial.print("           ");
  val1 = analogRead(D1_PLUS);       Serial.print(val1);                  Serial.print("DTWO");                //Serial.print("           ");
  val2 = analogRead(D0_CROSS);      Serial.print(val2);                  Serial.print("DTHR");                //Serial.print("           ");
  val3 = analogRead(D1_CROSS);      Serial.print(val3);                  Serial.print("DFOU");                //Serial.println("           ");
  /* SHUTTER CLOSING*/
  digitalWrite(SHTR_V, LOW);        digitalWrite(SHTR_CROSS, LOW);       delay(300);
}


void CALL_6() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_45, HIGH);     digitalWrite(SHTR_CROSS, HIGH);       delay(30);
  /* SENDING DETECTORS DATA */
  Serial.print("D");               Serial.print("START");                //Serial.print("           ");
  Serial.print("x");               Serial.print("BASE");                 //Serial.print("           ");
  val0 = analogRead(D0_PLUS);      Serial.print(val0);                   Serial.print("DONE");               //Serial.print("           ");
  val1 = analogRead(D1_PLUS);      Serial.print(val1);                   Serial.print("DTWO");               //Serial.print("           ");
  val2 = analogRead(D0_CROSS);     Serial.print(val2);                   Serial.print("DTHR");               //Serial.print("           ");       
  val3 = analogRead(D1_CROSS);     Serial.print(val3);                   Serial.print("DFOU");               //Serial.println("           ");
  /* SHUTTER CLOSING*/  
  digitalWrite(SHTR_45, LOW);      digitalWrite(SHTR_CROSS, LOW);        delay(300);
}


void CALL_7() {
  /* SHUTTER OPENING*/
  digitalWrite(SHTR_135, HIGH);     digitalWrite(SHTR_CROSS, HIGH);      delay(30);
  /* SENDING DETECTORS DATA */
  Serial.write("A");                Serial.print("START");               //Serial.print("           ");
  Serial.write("x");                Serial.print("BASE");                //Serial.print("           ");
  val0 = analogRead(D0_PLUS);       Serial.print(val0);                  Serial.print("DONE");                //Serial.print("           ");
  val1 = analogRead(D1_PLUS);       Serial.print(val1);                  Serial.print("DTWO");                //Serial.print("           ");
  val2 = analogRead(D0_CROSS);      Serial.print(val2);                  Serial.print("DTHR");                //Serial.print("           ");
  val3 = analogRead(D1_CROSS);      Serial.print(val3);                  Serial.print("DFOU");                //Serial.println("           ");
  /* SHUTTER CLOSING*/ 
  digitalWrite(SHTR_135, LOW);      digitalWrite(SHTR_CROSS, LOW);       delay(300);
}



             
