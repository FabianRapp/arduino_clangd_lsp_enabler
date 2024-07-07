# Arduino Clangd Lsp Enabler
Short python script that creates a header that includes all arduino headers and compile_commands.json for clangd

# Issues
Only tested with C.
Unix only

Currently I pretend that '-D__AVR_ATmega328P__' is a compile flag which is like 
```
#define __AVR_ATmega328P__
```
this could case isses. I only have aliexpress arduinos and don't know how to get the board info via software yet that why I hardcoded this.


# How to use 
Add this to you header file (example.h):
```
#ifdef LSP
#  include "lsp.h"
#endif
```
and have a a basic makefile rule 'echo_sources' which simply prints out the project sources seperated by any whitespace (Makefile_minium)


# Why
This will not only help me with arduino but also at school where the OS is too outdated for a brew bear install.
After tring and failing to get some language server for arduion to work I realised it's time to make my own basic tool to get stuff to work with clangd (even though it's very naive xd)

