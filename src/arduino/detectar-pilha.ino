#include <Ultrasonic.h>

int btnRed = 38;
int btnBlue = 36;
int btnGreen = 32;
int btnYellow = 42;
int btnBlack = 40;

bool stateBtnRed;
bool stateBtnBlue;
bool stateBtnGreen;
bool stateBtnYellow;
bool stateBtnBlack;

Ultrasonic ultrasonic(8, 10);
int distance;

void setup() {
  Serial.begin(9600);
  pinMode(btnRed, INPUT_PULLUP);
  pinMode(btnBlue, INPUT_PULLUP);
  pinMode(btnGreen, INPUT_PULLUP);
  pinMode(btnYellow, INPUT_PULLUP);
  pinMode(btnBlack, INPUT_PULLUP);
}

void loop() {
  distance = ultrasonic.read();
  stateBtnRed = digitalRead(btnRed);
  stateBtnBlue = digitalRead(btnBlue);
  stateBtnGreen = digitalRead(btnGreen);
  stateBtnYellow = digitalRead(btnYellow);
  stateBtnBlack = digitalRead(btnBlack);


  if (distance < 8 && distance != 6 && distance != 0) {
    Serial.println(distance);
    delay(125);
  } 

  if (stateBtnRed == LOW) {
    Serial.println("righ");
    delay(475);
  } else if (stateBtnBlue == LOW) {
    Serial.println("sobe");
    delay(475);
  } else if (stateBtnGreen == LOW) {
    Serial.println("left");
    delay(475);
  } else if (stateBtnYellow == LOW) {
    Serial.println("down");
    delay(475);
  }
}
