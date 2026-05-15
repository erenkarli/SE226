// 1. Pin Tanımlamaları
const int LED1 = 43, LED2 = 44, LED3 = 45, LED4 = 46;
const int btn1Pin = 38, btn2Pin = 39;

// Değişkenler
bool systemOn = false;    // Sistem açık/kapalı durumu
int currentMode = 1;      // Aktif mod (1, 2 veya 3)
bool lastBtn1 = LOW, lastBtn2 = LOW; // Önceki buton durumları

unsigned long prevTime = 0; // Zaman takibi için
int ledStep = 0;           // Mod 2 ve 3 için LED sırası

void setup() {
  pinMode(LED1, OUTPUT); pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT); pinMode(LED4, OUTPUT);
  pinMode(btn1Pin, INPUT); pinMode(btn2Pin, INPUT);
}

void loop() {
  // Butonları oku
  bool btn1 = digitalRead(btn1Pin);
  bool btn2 = digitalRead(btn2Pin);

  // BUTON 1: SİSTEM AÇ/KAPAT (Toggle)
  if (btn1 == HIGH && lastBtn1 == LOW) {
    systemOn = !systemOn;
    if (!systemOn) allOff(); // Kapandığında her şeyi söndür
    delay(50); // Titreşim engelleme
  }
  lastBtn1 = btn1;

  // BUTON 2: MOD DEĞİŞTİR (Sadece sistem açıkken)
  if (systemOn && btn2 == HIGH && lastBtn2 == LOW) {
    currentMode++;
    if (currentMode > 3) currentMode = 1;
    ledStep = 0; // Yeni moda geçince LED sırasını sıfırla
    allOff();    // Geçişte LED'leri temizle
    delay(50); 
  }
  lastBtn2 = btn2;

  // MODLARI ÇALIŞTIR
  if (systemOn) {
    unsigned long now = millis();
    if (now - prevTime >= 1000) { // 1 saniye dolunca bir sonraki adıma geç
      prevTime = now;
      runSelectedMode();
    }
  }
}

void runSelectedMode() {
  allOff();
  switch (currentMode) {
    case 1: // Hepsi beraber yanıp söner
      static bool toggle = false;
      toggle = !toggle;
      if (toggle) {
        digitalWrite(LED1, HIGH); digitalWrite(LED2, HIGH);
        digitalWrite(LED3, HIGH); digitalWrite(LED4, HIGH);
      }
      break;

    case 2: // Soldan Sağa Sırayla
      digitalWrite(43 + ledStep, HIGH);
      ledStep = (ledStep + 1) % 4;
      break;

    case 3: // Sağdan Sola Sırayla
      digitalWrite(46 - ledStep, HIGH);
      ledStep = (ledStep + 1) % 4;
      break;
  }
}

void allOff() {
  digitalWrite(LED1, LOW); digitalWrite(LED2, LOW);
  digitalWrite(LED3, LOW); digitalWrite(LED4, LOW);
}