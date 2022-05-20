// класс кнопки
#pragma once
#include <Arduino.h>
#define _BTN_DEB_TIME 50  // таймаут антидребезга
class Button {
  public:
    Button (byte pin, const char *code) : _pin(pin) {
      pinMode(_pin, INPUT);
      _code = code;
      _prev_state = HIGH;
      _flag = false;
    }

    bool check() {
      bool btnState = digitalRead(_pin);

      if(btnState != _prev_state){
        _tmr = millis();
        _flag = true;
        }

      _prev_state = btnState;

      if (_flag && (millis() - _tmr >= _BTN_DEB_TIME)) {
          sprintf(_cstr, "%lu", _tmr);
          _flag = false;
          Serial.write("<btn ");
          Serial.write(_code);
      
          if (btnState == LOW) {        

              Serial.write(" pressed at ");
              
              Serial.write(_cstr);
              Serial.write(">");
              return true;
          } else {       

              Serial.write(" released at ");
              Serial.write(_cstr);
              Serial.write(">");
          }
 
        
      }

      return false;
    }

  private:
    const char *_code;
    const byte _pin;
    uint32_t _tmr;
    bool _flag;
    char _cstr[16];
    bool _prev_state;
};
