


There is an sqlite3 database.  It has 6 columns;  a datetime.datetime stamp;  data in column_two, data in column_three, data in column_four and comments  in column_five.  There are presently   500,000 rows of data and about 7,000 are added every day.   The project is to make sense of this large set of data.
If this has never been done, then it represents a significant development project.  I feel slight encouragement that this application is not all that unusual.   Imagine an automatic weather station.  How about an automated sensor that counts cars through an intersection, or customers going into a movie theater.  Or a careful monitor of a HVAC system in a commercial building.  Or an automated monitor on a industrial system that makes widgets.  The personal theme is that I need help!


I have an arduino based science project.  I am wondering about accepted physical constants.  Is gravity truly constant?  I have three pendulums that have been ticking away for many months and have 700K rows of data in a sqlite3 database.  I see a massive software development project to make a platform that will sort through all these numbers.

What am I trying to achieve?  For example, what is the average number between 1:00 am and 2:00am.  This would mean the average number every day at this time!  This would generate one number a day or 365 numbers a year.  That would be cool.  I have three pendulums.  If variations in one pendulum are seen in the others, then that would be interesting.  I watch the numbers pretty closely and see a bit os strange stuff.  There are variations and the variations do not seem very regular.  I would love to be able to look at the standard deviations in the same way.  Are there patterns in the irregularities? The Arduino software (C++) gives me seconds to a millionth of a second!  The sort of deviations I am looking at would never be significant in a clock.  

After years and even decades of experience with other languages, I have dived into Python.  I love it.  It is complex and scary.  Yes, but it can be very easy to accomplish very difficult things.  FORTRAN is a language?  Okay.  Python is a language, like a spoken language and I am approaching it on that level.  I practice and practice and go over the same code again and again so I can gain fluency.

I recently, this morning, made a big leap;  I see how to SELECT * WHERE time_column between (‘this time’ and ‘that time’).  Thank you Stack Exchange.  But I cannot do this myself!  I need help.  
Xxxxxxxxxxxxxxxxxxxxxxxxxx

Python and statistical analysis of very large sqlite3 databases.
Many Arduino project automatically generate massive amounts of data.  The Arduino (C++) nicely feeds into Python and the Python nicely feeds into sqlite3.   This project is all about “now what?”  how do we look at the this data?
Xxxxxxxxxxx

