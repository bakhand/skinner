

void recvWithStartEndMarkers() {
    static boolean recvInProgress = false;
    static byte ndx = 0;
    char startMarker = '<';
    char endMarker = '>';
    char rc;
 
    while (Serial.available() > 0 && newData == false) {
        rc = Serial.read();

        if (recvInProgress == true) {
            if (rc != endMarker) {
                receivedChars[ndx] = rc;
                ndx++;
                if (ndx >= numChars) {
                    ndx = numChars - 1;
                }
            }
            else {
                receivedChars[ndx] = '\0'; // terminate the string
                recvInProgress = false;
                ndx = 0;
                newData = true;
            }
        }

        else if (rc == startMarker) {
            recvInProgress = true;
        }
    }
}

void procesCommand() {
    if (newData == true) {
        if (receivedChars[0] == '1'){
          if (receivedChars[1] == '0') {
            feeder.off();
            } else if (receivedChars[1] == '1') {
            feeder.on();
            } else {
              feeder.give();
            }
        }

       if (receivedChars[0] == '0'){
          int target_pos;
          if (receivedChars[1] == '0') {
            target_pos = 90;
            while (pos < target_pos) {
              
              pos += 5;
              leverServo.write(pos);
              delay(10);
            }
            } else {
            
             while (pos > target_pos) {
              pos -= 5;
              leverServo.write(pos);
              delay(10);
             }
            
            }
            
       }

        if (receivedChars[0] == '3'){
          if (receivedChars[1] == '0') {
            give_on_press = false;
            Serial.write("<Auto OFF>");
            }  else {
              give_on_press = true;
              Serial.write("<Auto ON>");
            }
        }

        newData = false;
        
    }
}
