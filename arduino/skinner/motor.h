// motor class
#pragma once
#include <Arduino.h>
#define _FEEDER_DEB_TIME 20 // таймаут антидребезга
#define _STOP_TIME 100//rotation after end of response уменьшать если дает 2
#define ROT_VEL 100 //ПАРАМЕТР 2 увеличивать если свистит и не крутится
#define _RESP_ON HIGH
#define _RESP_OFF LOW

class Motor
{
  private:
    enum _feeder_states {_fs_on0, _fs_off1, _fs_on1, _fs_off2};
    _feeder_states _feeder_state;
    
    const byte _resp_pin;
    const byte _power_pin;

    
    bool _flag;
    bool _flag_rotation;

    
    bool _resp;
    bool _prev_resp;
    uint32_t _tmr_resp;

    bool _stp_flag;
    uint32_t _tmr_stop;

    
    char _cstr[16];
    bool _prev_state;

  public:

    
    Motor(byte resp_pin, byte power_pin ) : _resp_pin(resp_pin), _power_pin(power_pin), _prev_resp(_RESP_OFF), _flag(false), _flag_rotation(false), _stp_flag(false)
    {
      pinMode(_resp_pin, INPUT);
      pinMode(_power_pin, OUTPUT);
      digitalWrite(_power_pin, LOW);
      this->select_start_state();
    }
    
    void select_start_state() {
      if (digitalRead(_resp_pin) == _RESP_ON) {
          _feeder_state = _fs_on0;
          Serial.write("<START ON_0>\n");
        } else {
          _feeder_state = _fs_off1;
          Serial.write("<START OFF_1>\n");
        }
    }
    
    void on() {
      Serial.write("<Motor ON at ");
      analogWrite(_power_pin, ROT_VEL); // 85 рабочее
      sprintf(_cstr, "%lu", millis());
      Serial.write(_cstr);
      Serial.write(">");
    }

    void off() {
      Serial.write("<Motor OFF at ");
      digitalWrite(_power_pin, LOW);
      sprintf(_cstr, "%lu", millis());
      Serial.write(_cstr);
      Serial.write(">");

    }

    bool give() {
      if (not _flag_rotation and not _stp_flag) {
      Serial.write("<Motor GIVING at ");
      sprintf(_cstr, "%lu", millis());
      Serial.write(_cstr);
      Serial.write(">");
      _flag_rotation = true;
      this->select_start_state();
      this->on();
      } else {
      Serial.write("<Motor BUSY at ");
      sprintf(_cstr, "%lu", millis());
      Serial.write(_cstr);
      Serial.write(">");
        
        }

    }
    void check() {
      _prev_resp = _resp;
      _resp = (digitalRead(_resp_pin) == _RESP_ON);
      
      if (_resp != _prev_resp) {
        _tmr_resp = millis();
        _flag = true;
      }

       if (_flag && (millis() - _tmr_resp >= _BTN_DEB_TIME)){
              _flag = false;
              if (_flag_rotation) {
                    if (_resp){
                      this->resp_on_process();
                    }
                    else {
                      this->resp_off_process();
                    }
              }
             }


      if (_stp_flag && (millis() - _tmr_stop >= _STOP_TIME)){
              _stp_flag = false;
              Serial.write("<Actually stoppind after delay>\n");
              this->off();
              
           }
    }

   void resp_on_process() {
      switch (_feeder_state) {
        case _fs_on0:
          break;
        case _fs_off1:
          _feeder_state = _fs_on1;
          Serial.write("<ON1>\n");
          break;
        case _fs_on1:
          break;
        case _fs_off2:
          Serial.write("<ON IN OFF2 PERELET>\n");
          break;
        }
     }
     
   void resp_off_process () {
      switch (_feeder_state) {
        case _fs_on0:
          _feeder_state = _fs_off1;
          Serial.write("<OFF1>\n");
          break;
        case _fs_off1:
          break;
        case _fs_on1:
          _feeder_state = _fs_off2;
          Serial.write("<OFF2 turning off>\n");
          //digitalWrite(_power_pin, LOW); try to move motor to drop pellets
          //delay(10);
          //digitalWrite(_power_pin, HIGH);
          //delay(10);
          //analogWrite(_power_pin, 85);
          _tmr_stop = millis();
          _stp_flag = true;
          _flag_rotation = false;
          break;
        case _fs_off2:
          break;
        } 
        }

    
      
      
     
    



};
