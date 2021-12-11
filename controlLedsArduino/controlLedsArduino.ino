int led1 = 2;
int led2 = 3;
int option;

void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);

}

void loop() {
  if (Serial.available() ) {
    option = Serial.read();
    Serial.print(option);
    if (option == 'P') {
      digitalWrite(led1, HIGH);
      digitalWrite(led2, LOW);
    }
    else if (option == 'N') {
      digitalWrite(led1, LOW);
      digitalWrite(led2, HIGH);
    }
    else if(option == 'X'){
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
    }
  }
 
}
