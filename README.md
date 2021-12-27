


There is an sqlite3 database.  It has 6 columns;  a datetime.datetime stamp;  data in column_two, data in column_three, data in column_four and comments  in column_five.  There are presently   500,000 rows of data and about 7,000 are added every day.   The project is to make sense of this large set of data.
If this has never been done, then it represents a significant development project.  I feel slight encouragement that this application is not all that unusual.   Imagine an automatic weather station.  How about an automated sensor that counts cars through an intersection, or customers going into a movie theater.  Or a careful monitor of a HVAC system in a commercial building.  Or an automated monitor on a industrial system that makes widgets.  The personal theme is that I need help!


I have an arduino based science project.  I am wondering about accepted physical constants.  Is gravity truly constant?  I have three pendulums that have been ticking away for many months and have 700K rows of data in a sqlite3 database.  I see a massive software development project to make a platform that will sort through all these numbers.

What am I trying to achieve?  For example, what is the average number between 1:00 am and 2:00am.  This would mean the average number every day at this time!  This would generate one number a day or 365 numbers a year.  That would be cool.  I have three pendulums.  If variations in one pendulum are seen in the others, then that would be interesting.  I watch the numbers pretty closely and see a bit of strange stuff.  There are variations and the variations do not seem very regular.  I would love to be able to look at the standard deviations in the same way.  Are there patterns in the irregularities? The Arduino software (C++) gives me seconds to a millionth of a second!  The sort of deviations I am looking at would never be significant in a clock.  

After years and even decades of experience with other languages, I have dived into Python.  I love it.  It is complex and scary.  Yes, but it can be very easy to accomplish very difficult things.  FORTRAN is a language?  Okay.  Python is a language, like a spoken language and I am approaching it on that level.  I practice and practice and go over the same code again and again so I can gain fluency.

I recently, this morning, made a big leap;  I see how to SELECT * WHERE time_column between (‘this time’ and ‘that time’).  Thank you Stack Exchange.  But I cannot do this myself!  I need help.  
Xxxxxxxxxxxxxxxxxxxxxxxxxx

Python and statistical analysis of very large sqlite3 databases.
Many Arduino project automatically generate massive amounts of data.  The Arduino (C++) nicely feeds into Python and the Python nicely feeds into sqlite3.   This project is all about “now what?”  how do we look at the this data?
Xxxxxxxxxxx

Xxxx12/24/2021
Promotion ????  how am I going to present this to the world?  Let’s use Github for everything.  That is what it is for!
I seem to need three pictures for the three repositories

There are two repositories under my name.  I am thinking that this is good:  one repository for Arduino acquisition and python to sqlite3 storage and another for data summaries through python and data interpretation.  Maybe I need another; data interpretation for wswinging pendulum and data interpretation
Github bio
Sqlite3 and statistical analysis of large databases
I think rather than try to fix the three repositories, I should , like, start from scratch:

Arduino, C++ , Python, sqlite3  data capture for gravity and mass experiment
Two of the fundamental constants in physical science are gravity and mass.  My academic qualitifcations to approach this question are not strong, but I have the diverse background, creativity and curiosity to ask this question:  are they really constant?  I thnk f myself as the creative lab tech that came up with the question and the path toward an answer, but realize that my limits stop me at that point.   These experiments may indicate that gravity and mass are not constant.  If this is indicated (I hesitate to use the word ‘proven’) then I need to pass it all to another team.
The handle for gravity is the period of a swinging pendulum.  The period is described by this formula:

Garavity is assumed to be a constant.   The experiment is fairly straightforward:  look carefully at the period of a pendulum.  If there are variations in the period, then this indicated that gravity is not constant.  (everything else constant)
The anniversary clock is the one that is always found in a glass dome, about 14 inches high.  There is a shinny brass things with four balls  that swings back and forth.  The period of the swing is is determined by a complex set of variables, but at the center of this is the mass.  This experiment porposes that variations in the period indicate that mass is not constant.  These clocks have a reputation for not being very good.  Is there variations in the mass of the brass rotor?   Let’s hold all variables constant.  During the months of January and February, the period goes down, that is the rotor speeds up,  This is compicated, but mass is at the center.

It is important to appreciate this is all about the reproducibility of the data.  The specifics of the period

The Arduino microcontroller is a small, inexpensive computer that makes it easy for any computer to interact with the outside world.  It accepts input from sensors, sends output to motors, solenoids, lights etc.   I write a little program in C++ and put it in the little computer (Arduino Uno) and the program accepts input creats output and sends out data.  I have little understanding of it, but it is not difficult to do cool thigs with it.
The signals come in through a Hall detector.  There is a magnet on the pendulum.  At the end of its swing the magnet trips the Hall and the signal is sent to the Arduino which then sned it out and into a computer through the computer’s serial port.  
In the computer the signal is caught by Python.  This program adds a UNIX time stamp and puts it in a fied in an sqlite3 database.
There was am enormous amount of development behind both the C++ and the Python, but in the end neighter is tremendously complex.
The data streams are through essentiall clocks and both accurate and precise.  The Python simply separates them by size with ‘if’ statements.    Some of the fields threatened to overlap with others and I added 30 million and 20 million to two of the data streams respectively.  These were added unambiguously at the input.  With these the Python was able to absolutely separate them.




Gravity esperiment data interpretation

Mass experiment data interpretation.

xxxxxxxxxxxxxxxxxxx
I have three depositories now.  I can rename them and remae them, I assume into whatever I want.  They need to be cold and professional.  I am thinking of starting the whole communication with the existenace of six columns.  I thknk this is april 2020.  this discards all the previous data which means the first year and a half are not of interest.  I am comfortable with this.  Noone cares about the tiral i went through;  I do not even care.

With the addition of Mu,, the grandfather clock, I had four data streams.  I thnk I moved the collecting database to six plus datetime plus error or eight