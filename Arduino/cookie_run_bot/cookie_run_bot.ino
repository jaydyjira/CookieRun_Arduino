#include <Servo.h>
#include <avr/pgmspace.h>
#include "timing_table.h"

// ---------------------------------------------------------------- pins
const uint8_t PIN_JUMP  = 6;
const uint8_t PIN_SLIDE = 7;
const uint8_t PIN_START = 2;   // push button: one leg here, other leg to GND

// ------------------------------------------------- servo travel angles
// Tune these against a drawing app before touching Cookie Run.
const uint8_t REST_JUMP  = 20;
const uint8_t PRESS_JUMP = 10;
const uint8_t REST_SLIDE  = 10;
const uint8_t PRESS_SLIDE = 20;

// Shifts the whole sequence. Positive = everything happens later.
const int32_t TIME_OFFSET_MS = 0;

Servo servoJump, servoSlide;

// ---------------------------------------------------------------- state
bool running = false;
uint32_t startMs = 0;
uint16_t nextEv = 0;

bool jumpDown = false, slideDown = false;
uint32_t jumpReleaseAt = 0, slideReleaseAt = 0;

void setup() {
  Serial.begin(9600);
  pinMode(PIN_START, INPUT_PULLUP);

  servoJump.attach(PIN_JUMP);
  servoSlide.attach(PIN_SLIDE);
  servoJump.write(REST_JUMP);
  servoSlide.write(REST_SLIDE);

  Serial.print(F("Ready. "));
  Serial.print(EV_COUNT);
  Serial.println(F(" events loaded. Press the button to start."));
}

void loop() {
  // ---- waiting for the start button ----
  if (!running) {
    if (digitalRead(PIN_START) == LOW) {
      delay(20);                                 // debounce
      while (digitalRead(PIN_START) == LOW) { }  // wait for release
      startMs = millis();
      nextEv = 0;
      running = true;
      Serial.println(F("GO"));
    }
    return;
  }

  int32_t now = (int32_t)(millis() - startMs) - TIME_OFFSET_MS;

  // ---- fire every event that has come due ----
  while (nextEv < EV_COUNT &&
         (int32_t)pgm_read_dword(&evTime[nextEv]) <= now) {

    uint8_t  which = pgm_read_byte(&evWhich[nextEv]);
    uint16_t dur   = pgm_read_word(&evDur[nextEv]);

    if (which == JUMP) {
      servoJump.write(PRESS_JUMP);
      jumpDown = true;
      jumpReleaseAt = now + dur;
    } else {
      servoSlide.write(PRESS_SLIDE);
      slideDown = true;
      slideReleaseAt = now + dur;
    }
    nextEv++;
  }

  // ---- lift each head once its hold time is up ----
  if (jumpDown && now >= (int32_t)jumpReleaseAt) {
    servoJump.write(REST_JUMP);
    jumpDown = false;
  }
  if (slideDown && now >= (int32_t)slideReleaseAt) {
    servoSlide.write(REST_SLIDE);
    slideDown = false;
  }

  // ---- finished ----
  if (nextEv >= EV_COUNT && !jumpDown && !slideDown) {
    running = false;
    Serial.println(F("Run complete."));
  }
}
