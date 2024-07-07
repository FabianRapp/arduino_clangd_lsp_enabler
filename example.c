#include <avr/io.h>
#include <util/delay.h>

#include "main.h"

void	init() {
    DDRB |= (1 << DDB5);
}

void	main_loop() {
    PORTB ^= (1 << PORTB5);
    _delay_ms(1000);
}



//int led = 9;         // the PWM pin the LED is attached to
//int brightness = 0;  // how bright the LED is
//int fadeAmount = 5;  // how many points to fade the LED by
//
//// the setup routine runs once when you press reset:
//void setup() {
//  // declare pin 9 to be an output:
//  pinMode(led, OUTPUT);
//}
//
//
//// the loop routine runs over and over again forever:
//void loop() {
//  // set the brightness of pin 9:
//  analogWrite(led, brightness);
//
//  // change the brightness for next time through the loop:
//  brightness = brightness + fadeAmount;
//
//  // reverse the direction of the fading at the ends of the fade:
//  if (brightness <= 0 || brightness >= 255) {
//    fadeAmount = -fadeAmount;
//  }
//  // wait for 30 milliseconds to see the dimming effect
//  delay(30);
//}

//void setup() {
//    pinMode(LED_BUILTIN, OUTPUT);
//}
//
//void loop() {
//    digitalWrite(LED_BUILTIN, HIGH);
//    delay(1000);
//    digitalWrite(LED_BUILTIN, LOW);
//    delay(1000);
//}

