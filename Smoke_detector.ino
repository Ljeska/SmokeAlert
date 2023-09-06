

const int gasSensorPin = A0;
const int buzzerPin = 4;
const int ledGreenPin = 7;
const int ledRedPin = 2;
const int threshold = 650;

void setup() {
  Serial.begin(9600);
  pinMode(gasSensorPin, INPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(ledGreenPin, OUTPUT);
  pinMode(ledRedPin, OUTPUT);
}

void loop() {
  int gas_value = analogRead(gasSensorPin);
  
  if (gas_value > threshold) {
    alarmState();
    triggerEmail();
  } else {
    normalState();
  }
  
  delay(200);
}

void alarmState() {
  tone(buzzerPin, 1000, 500);
  digitalWrite(ledRedPin, HIGH);
  digitalWrite(ledGreenPin, LOW);
}

void normalState() {
  noTone(buzzerPin);
  digitalWrite(ledGreenPin, HIGH);
  digitalWrite(ledRedPin, LOW);
}

void triggerEmail() {
  Serial.println("SendEmail");
}
