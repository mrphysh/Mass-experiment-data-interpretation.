


There is an sqlite3 database.  It has 6 columns;  a datetime.datetime stamp;  data in column_two, data in column_three, data in column_four and comments  in column_five.  There are presently   500,000 rows of data and about 7,000 are added every day.   The project is to make sense of this large set of data.
If this has never been done, then it represents a significant development project.  I feel slight encouragement that this application is not all that unusual.   Imagine an automatic weather station.  How about an automated sensor that counts cars through an intersection, or customers going into a movie theater.  Or a careful monitor of a HVAC system in a commercial building.  Or an automated monitor on a industrial system that makes widgets.  The personal theme is that I need help!


I have an arduino based science project.  I am wondering about accepted physical constants.  Is gravity truly constant?  I have three pendulums that have been ticking away for many months and have 700K rows of data in a sqlite3 database.  I see a massive software development project to make a platform that will sort through all these numbers.

What am I trying to achieve?  For example, what is the average number between 1:00 am and 2:00am.  This would mean the average number every day at this time!  This would generate one number a day or 365 numbers a year.  That would be cool.  I have three pendulums.  If variations in one pendulum are seen in the others, then that would be interesting.  I watch the number pretty closely and see a bit os strange stuff.  There are variations and the variations do not seem very regular.  I would love to be able to look at the standard deviations in the same way.  Are there patterns in the irregularities? The Arduino software (C++) gives me seconds to a millionth of a second!  The sort of deviations I am looking at would never be significant in a clock.  

After years and even decades of experience with other languages, I have dived into Python.  I love it.  It is complex and scary.  Yes, but it can be very easy to accomplish very difficult things.  FORTRAN is a language?  Okay.  Python is a language, like a spoken language and I am approaching it on that level.  I practice and practice and go over the same code again and again so I can gain fluency.

I recently, this morning, made a big leap;  I see how to SELECT * WHERE time_column between (‘this time’ and ‘that time’).  Thank you Stack Exchange.  But I cannot do this myself!  I need help.  
Xxxxxxxxxxxxxxxxxxxxxxxxxx

description..I am not sure how this will be used.

Python and statistical analysis of very large sqlite3 databases.
Many Arduino project automatically generate massive amounts of data.  The Arduino (C++) nicely feeds into Python and the Python nicely feeds into sqlite3.   This project is all about “now what?”  how do we look at the this data?
Xxxxxxxxxxx

readme
Python and statistical analysis of very large sqlite3 databases.
Many Arduino projects automatically generate massive amounts of data.  The Arduino (C++) nicely feeds into Python and the Python nicely feeds into sqlite3.   This project is all about “now what?”  How can we make meaning from all this data?

There is an sqlite3 database.  It has 6 columns;  a datetime.datetime stamp;  data in column_two, data in column_three, data in column_four and comments  in column_five.  There are presently   500,000 rows of data and about 7,000 are added every day.   The project is to make sense of this large set of data.
If this has never been done, then it represents a significant development project.  I feel slight encouragement that this application is not all that unusual.   Imagine an automatic weather station.  How about an automated sensor that counts cars through an intersection, or customers going into a movie theater.  Or a careful monitor of a HVAC system in a commercial building.  Or an automated monitor on a industrial system that makes widgets.  The personal theme is that I need help!

These parts are done:

The Arduino (C++) is done.  It a fairly interesting sketch.  One sketch operates three pendulums.  The compiler flies by and trips these triggers for the timing.  With no ‘if’ statements is is able to operate all three.

The C++ passes the numbers out to the serial monitor and they are caught by the Python.  The numbers fall into three categories based upon size.  The numbers are on the order of 1.876588.  So that is 1.8 million.  (this is all about time;  1.8 million seconds) The Python sorts the values into the three sizes with ‘if’ statements and inserts them into a sqlite3 database.  They are put in the appropriate column, adding a datetime.datetime time stamp.   This is all done.  

There is an example sqlite3 database.  
Database      dec3_database     
				tables
					first_table                168000 lines
					dec26_table_cont        341 lines
					dec26_table                      9 lines

I use this database for development and use table   [dec26_table_cont]  .  I made it for that purpose, although it does contain real data. 

Take a look at the code.  The comments are included within the program and are fairly extensive.  Look at the database (ignore the [first_table]   ….   too big)

I have been actively and aggressively looking at Python, specifically at the Python/sqlite3 interface and have made progress.  I made a big break this morning.  I added an index, or rather modified the first column to include an index.  I did this through the sqlite3 command line.  

sqlite> CREATE INDEX IF NOT EXISTS index_time_table_one ON dec26_table_cont( column_one);

Then this worked:
 
c.execute ("SELECT * FROM dec26_table_cont WHERE column_one BETWEEN '2018-12-26 21:48:13.377000' and '2018-12-26 21:53:13.363000' ")

I had been struggling with this even for weeks.  (thank you Stack Exchange)

I have just recently started with pandas and it looks promising.

The code, scripts, sketches are interesting and not that difficult.  (If I can understand them anyone can)
Take a look. 
  
  
