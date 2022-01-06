README FOR MASS DATA INTRPRETATION
Generic README for all three repositories.

Two of the fundamental constants in physical science are gravity and mass.  My academic qualifications to approach this question are not strong, but I have the diverse background, creativity and curiosity to ask this question:  are they really constant?  I think of myself as the creative lab tech that came up with the question and the path toward an answer, but realize that my limits stop me at that point.   These experiments may indicate that gravity and mass are not constant.  If this is indicated (I hesitate to use the word ‘proven’) then I need to pass it all to another team.

Gravity is assumed to be a constant.   The experiment is fairly straightforward:  look carefully at the period of a pendulum.  If there are variations in the period, then this indicates that gravity is not constant.  (Everything else is constant)

The power of this primitive experiment is the “micros()” function in C++.  The micros() function returns the number of microseconds from the time, the Arduino board begins running the current program. This number overflows i.e. goes back to zero after approximately 70 minutes

The anniversary clock is the one that is always found in a glass dome, about 14 inches high.  There is a shiny brass thing with four balls that rotates back and forth.  The period of the rotation is determined by a complex set of variables, but at the center of this is the mass.  This experiment proposes that variations in the period indicate that mass is not constant.  These clocks have a reputation for not being very good.  Are there variations in the mass of the brass rotor?   Let’s hold all variables constant.  For example, during the months of January and February, the period goes down, that is; the rotor speeds up, this indicates that the mass of the rotating object has gone down.  This is complicated, but mass is at the center.

It is important to appreciate this is all about the reproducibility of the data.  The specifics of the period are not of interest.
I originally joined GitHub to invite, even ask for help.  I thought that there was a general need for this software development and still believe this.  But I did not understand how the platform was to be used and, in any event, never attracted any attention.  

I developed it all myself and have looked at the data and found data that needs another set of eyes, that is, a peer review, as it is called in academic circles.  This GitHub account is changed to present the software with this project.  It is divided into three repositories:  
xxxxxx                                                                                                     xxxxx

Mass experiment data interpretation.
The data of the mass experiment is the timing of an anniversary clock.  This is the decorative shiny brass clock always found in a glass dome, about 14 inches high.  The rotating part is a little brass thing with four brass balls.  It is fairly heavy, about 100 grams.  The speed of the clock is adjusted with a mechanism that carefully moves the brass balls out and in.  The radius of the constant mass changes the speed.  We, of course, just leave it alone.  The specifics of the timing etc. are not of interest, only the reproducibility.
The rotation of a rotating pendulum is complex, but at the center of it is angular momentum.  The formula is 
L = mvr
L is angular momentum.  The variables are    
Mass, velocity and radius
Rather than insist that the Hall detector is at the end of the rotation, the Hall is in the middle.  This requires an addition to the C++ script, because two trips of the detector are required for one data capture.  
Let’s paint a physical picture of this:  There are six clocks.  The microcontroller has six LEDs that go HIGH with contact with the Hall.  The swinging pendulums period is about 1.877689.  So, they each make a number in somewhat less than 2 seconds.  The rotating pendulums take 13 to 15 seconds for one cycle.  (This is of course 13.394827 seconds, for example.  to the millionth of a second.)  The python in the main computer listens to this noise, about 130 per minute.  It picks one number out of nineteen.  It counts to 19 and takes a number.  Then does that again.
It puts this number into a database with the UNIX time stamp.  So, it takes about 7 numbers a minute.  This is all controllable by the programmer (me).  
There are much fewer numbers from the anniversary clocks, but still, lots of them.  The rotating pendulums wee added much later.  The present platform has three swinging pendulums and three anniversary clocks, but it all started with only swinging pendulums.
A given row in the source database has one time stamp and one value per row.
The software for this project is identical for the Gravity Interpretation project.  This repository shows some data and it is interesting.
