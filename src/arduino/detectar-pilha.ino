int sensor = 8;
int btnRed = 38;
int btnBlue = 36;
int btnGreen = 32;
int btnYellow = 42;
int btnBlack = 40;
int sensor_sts;

bool stateBtnRed;
bool stateBtnBlue;
bool stateBtnGreen;
bool stateBtnYellow;
bool stateBtnBlack;


void setup() {
  Serial.begin(9600);
  pinMode(sensor_sts, INPUT);
  pinMode(btnRed, INPUT_PULLUP);
  pinMode(btnBlue, INPUT_PULLUP);
  pinMode(btnGreen, INPUT_PULLUP);
  pinMode(btnYellow, INPUT_PULLUP);
  pinMode(btnBlack, INPUT_PULLUP);
}

void loop() {
  stateBtnRed = digitalRead(btnRed);
  stateBtnBlue = digitalRead(btnBlue);
  stateBtnGreen = digitalRead(btnGreen);
  stateBtnYellow = digitalRead(btnYellow);
  stateBtnBlack = digitalRead(btnBlack);
  sensor_sts = digitalRead(sensor);

  if (!sensor_sts) {
    Serial.println("ente");
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
