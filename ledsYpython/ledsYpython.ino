int led1 = 7;
int led2 = 6;
int option; // va en int xq devuelve codigo ASCII puede ser char
void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

}

void loop() {
  if (Serial.available()) {
    option = Serial.read();
    Serial.println(option);
    if (option == 'a') {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
    }
    else if (option == 'b') {
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
    }
  }


}
