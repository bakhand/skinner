#include <PWMServo.h>
#include "button.h"
#include "motor.h"


const int servoConrol = 9;
bool give_on_press = false;

int startLeverPos = 0; 
int pos = 90;



const byte numChars = 32;
char receivedChars[numChars];

boolean newData = false;

Button onButton(A0, "Start");
Button leverPress(A1, "Lever");
Button nosePoke(A2 ,"NosePoke");
Button pelletCounter(A3, "Pellet");
Motor feeder(A3, 3);

PWMServo leverServo; 

void setup() {
  
  leverServo.attach(9, 1000, 2000);
  leverServo.write(pos);

  Serial.begin(115200);
  Serial.println("<Arduino is ready>");
  
}

// the loop routine runs over and over again forever:
void loop() {
   if (leverPress.check() & give_on_press) {
    feeder.give();
   }
   if (onButton.check()) {
    feeder.give();
   }
   nosePoke.check();
   feeder.check();
   recvWithStartEndMarkers();
   procesCommand();
}
