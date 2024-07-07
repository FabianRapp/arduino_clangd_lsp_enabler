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

