int led1 = 2;
int led2 = 3;
int led3 = 4;
int led4 = 5;
int led5 = 6;
int led6 = 7;
int led7 = 8;

int option;
int val;
void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);

}

void loop() {
  if (Serial.available() > 0) {
    option = Serial.read();
    //-Serial.print(option);

    if (option == 't') { //triangulo
      digitalWrite(led1, HIGH);
    }
    else if (option == 'c') { //cuadrado
      digitalWrite(led2, HIGH);
    }
    else if (option == 'r') { //rectangulo
      digitalWrite(led3, HIGH);
    }
    else if (option == 'p') { //pentagono
      digitalWrite(led4, HIGH);
    }
    else if (option == 'x') { //hexagono
      digitalWrite(led5, HIGH);
    }
    else if (option == 'i') { //circulo
      digitalWrite(led6, HIGH);
    }
    else if (option == '?') { //desconocido
      digitalWrite(led7, HIGH);
    }
    else if (option == '-') {
      digitalWrite(led1, LOW);
      digitalWrite(led2, LOW);
      digitalWrite(led3, LOW);
      digitalWrite(led4, LOW);
      digitalWrite(led5, LOW);
      digitalWrite(led6, LOW);
      digitalWrite(led7, LOW);
    }
    delay(100);
  
  }
}
