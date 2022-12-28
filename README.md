# Pendulum Period Detection
This program detects pendulum period of an image data using opencv in python. This program uses color detection to detect a color dominant object 
and analyze the pixel position of a moving object that satisfied simple harmonic motion to get the period
</br> To get the period:
- First, run the program located in color_based_obj_detection folder to get the maximum and minimum HSV value of a color dominant object.
- Then, input the maximum and minimum HSV value to the second program located in pendulum_period_detection folder.
</br> This program was inspired by @murtazahassan. 
