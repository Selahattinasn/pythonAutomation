# CODE_REUSABILITY by using FUNCTIONS & MODULES
In programming, we often reuse code that we've written or someone else has written. This is called code reuse and nearly all languages provide some way of doing it. For code reusability we use functions and module. Functions let us group code into logical blocks that can be executed at a later point and as many times as we need. 

Lets say we have a module named "areas", that imports another module and has three functions. How to use it: 
- Fist we need to import this moules. 
- Second we specify this module and sub functions and give the arguments. 

For example:

```python3

# we are now in interactive interpreter:

python3

import areas

areas.circle(10)
areas.triangle(3,5)
areas.rectangle(4,6)

```

## MODULES:

if we have complex modules structure, that has much more modules and sub modules we place all or the in a directory.

***__init.py__*** file must be in the directory, so that python_interpreter can understand, that this directory is a modul.  

![licp](images/licp.png)
