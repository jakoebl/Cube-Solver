#include <string.h>

//delayTime for delay between steps in us
int delayTime = 160;
// delayTime betweeen moves in ms
int delayTimeMoves_ms = 120;

int pin_U = 11;
int pinDirection_U = 10;
int pin_F = 13;
int pinDirection_F = 12;
int pin_L = 5;
int pinDirection_L = 4;
int pin_B = 3;
int pinDirection_B = 2;
int pin_R = 9;
int pinDirection_R = 8;
int pin_D = 7;
int pinDirection_D = 6;


void setup() {
    Serial.begin(9600);
    randomSeed(analogRead(0));
    for (int i = 2; i < 14; i++) {
      pinMode(i, OUTPUT);
    }
}

void loop() {
  String moves = getString();
  Serial.println(moves);
   makeMoves(moves);
  moves = "";
}
String getString() {
  while (Serial.available() == 0) {}     //wait for data available
  String result = Serial.readStringUntil('z');  //read until timeout
  result.trim();
  return result;
}

void makeMove(int pinNum) {
  for (int i = 0; i < 400; i++) {
digitalWrite(pinNum,HIGH);
delayMicroseconds(delayTime);
digitalWrite(pinNum,LOW);
delayMicroseconds(delayTime);
}
}
void chooseMove(char character) {
  switch (character)  {
    case 's':
      for (int i = 0; i < 27; i++) {
        makeMove(random(1, 7) * 2 + 1);
        delay(delayTimeMoves_ms);
      }
    case 'U':
      makeMove(pin_U);
      break;
      
    case 'u':
      digitalWrite(pinDirection_U, HIGH);
      makeMove(pin_U);
      digitalWrite(pinDirection_U, LOW);
      break;
      
    case 'V':
      makeMove(pin_U);
      makeMove(pin_U);
      break;
      
    case 'f':
      makeMove(pin_F);
      break;
      
    case 'F':
      digitalWrite(pinDirection_F, HIGH);
      makeMove(pin_F);
      digitalWrite(pinDirection_F, LOW);
      break;

    case 'G':
      makeMove(pin_F);
      makeMove(pin_F); 
      break;
      
    case 'l':
      makeMove(pin_L);
      break;
      
    case 'L':
      digitalWrite(pinDirection_L, HIGH);
      makeMove(pin_L);
      digitalWrite(pinDirection_L, LOW);
      break;
      
    case 'M':
      makeMove(pin_L);
      makeMove(pin_L);   
      break;
      
    case 'B':
      makeMove(pin_B);
      break;
      
    case 'b':
      digitalWrite(pinDirection_B, HIGH);
      makeMove(pin_B);
      digitalWrite(pinDirection_B, LOW);
      break;
      
    case 'C':
      makeMove(pin_B);
      makeMove(pin_B);
      break;

    case 'r':
      makeMove(pin_R);
      break;
      
    case 'R':
      digitalWrite(pinDirection_R, HIGH);
      makeMove(pin_R);
      digitalWrite(pinDirection_R, LOW);
      break;
      
    case 'S':
      makeMove(pin_R);
      makeMove(pin_R);      
      break;

    case 'D':
      makeMove(pin_D);
      break;
      
    case 'd':
      digitalWrite(pinDirection_D, HIGH);
      makeMove(pin_D);
      digitalWrite(pinDirection_D, LOW);
      break;
      
    case 'E':
      makeMove(pin_D);
      makeMove(pin_D);     
      break;      
  }
}

void makeMoves(String moves)  {
  for (int i = 0; i < moves.length(); i++) {
    chooseMove(moves[i]);
    delay(delayTimeMoves_ms);
  }
}
