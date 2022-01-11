import sqlite3   
import datetime
from datetime import datetime,timedelta
import os
import sys
python_script = sys.argv[0]
print ("script name   ", python_script)
###
###
data_source_database =  "031 mar22_2021_db_sorted"
###
##
##
conn = sqlite3.connect('C:\\Users\\mrphy\\dec 2021 ROT summaries\\data by julian month\\031 mar22_2021_db_sorted')      # one table only 'first_table'
c = conn.cursor()
#
#
bonn = sqlite3.connect('C:\\Users\mrphy\\dec 2021 ROT summaries\\sorted final summary\\rotating_pend_summary_example')      
b = bonn.cursor()
b.execute("CREATE TABLE IF NOT EXISTS anniversary_clocks_march (UNIX_date TEXT,rodney REAL,robbie REAL,\
python_script TEXT,total_rows REAL,rodney_rows REAL,robbie_rows REAL,search_number REAL,contributing_DB TEXT )") 
print ("++++++++++++++++++")

def dynamic_data_entry_averages():
    b.execute("INSERT INTO  anniversary_clocks_march(UNIX_date,rodney,robbie,python_script,total_rows,rodney_rows,robbie_rows,search_number,contributing_DB) VALUES (?,?,?,?,?,?,?,?,?)",\
              ( date_var,one_average,two_average,python_script,row_count,one_count,two_count,search_number,data_source_database  ) )
    bonn.commit()
##
##    
date_var = '2021-03-22 22:00:00'
#
search_number =  5000
#
print("start date for this script            "       , date_var)
var_one = 34 
print("database is  ",        data_source_database     )
number = 0
total_count = 0
num_added_db = 0
print ("++++++++++++++++++++++++++")
while (var_one  ):
    var_one = None                  #this needs to null  ..  will it be reset?
    c.execute ("SELECT column_one, column_two,column_five FROM first_table WHERE column_one > '%s'" %date_var)
    number =0                      
    no_val = 0;    one_sum   = 0;   one_count = 0;   two_sum   = 0;   two_count = 0;    thr_sum   = 0; thr_count = 0
    for_sum   = 0; for_count = 0;   five_sum   = 0;  five_count = 0;  six_sum   = 0;     six_count = 0;one_average = 0
    two_average = 0; thr_average = 0
    for row in c.fetchmany(search_number):
        var_one = row[0]
        var_two = row[1]
        var_thr = row[2]
        if var_two != None and type(var_two) == (float):
            #five_var =  (row[i])
            one_sum = one_sum + var_two
            one_count = one_count + 1
            
        if var_thr != None and type(var_thr) == (float):
            #five_var =  (row[i])
            two_sum = two_sum + var_thr
            two_count = two_count + 1
        number = number +1
    num_added_db = num_added_db + 1
    total_count = total_count + number
    number = 0
    if one_count != 0:
        one_average = int(one_sum/(one_count ))
    if two_count != 0:
        two_average = int(two_sum/(two_count ))

    row_count = one_count + two_count 


    
    print("date   ",date_var," rodney ",one_average," robbie ", two_average  )
   ## print ("the targets are,repectively   ",one_target,"        ",two_target,"      ", thr_target,\
        ##   "   ",for_target,"  ",five_target,"    ",six_target )
    print ("row count...total of all counts    ", row_count)

    dynamic_data_entry_averages() 

        
    date = datetime.strptime(date_var, "%Y-%m-%d %H:%M:%S")  # this sets up the variable for altering
    date = str(date + timedelta(days = 1))     
    date_var = date
    
    print ()
"""
summarize it all:  how many rows were read
                   how many rows were entered into the recieving database?
"""    
print ("total rows pulled from db is     ", total_count)
print ("total rows added to database is   ", num_added_db)
print ("           end                end          end                  end                end ")

"""
7777777777777   date format   '2021-08-25 22:00:00'
                             just use search number 5000
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\


'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept11_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept18_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept24_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\001_sept4_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct01_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct08_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct13_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\002_oct21_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\004_dec3_database first table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\004_dec3_database second table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\005_jan18_2019_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\007_mar_2_2019_database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\008_april_19_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\008_april_26_no sort_db'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\009_may_15_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\009_may_26_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\011_july_4_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\012_aug21_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\013_sept19_2019_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\015_nov11_2019_db_no_sort_bigger'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\017_jan08_2020_partdb_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\018_feb22__database'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\019_mar14_2020_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\021_may27_2020_'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\023_jul18_2020_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\025 sept15_2020_db_no_sort'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\026 oct09_2020_db_no_sort first_table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\026 oct09_2020_db_no_sort second table'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\027 nov23_2020_db_sorted'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\029 jan23_2021_db_sorted'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\031 mar22_2021_db_sorted'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\033 all_numbers_june28_2021_aa_7_6'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\034 june26_all_numbers'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\035 one_of_two_july11_2021'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\036 one_of_two_aug24_2021'
'C:\\Users\\mrphy\\dec 2021 data summaries\\data by julian month\\038 one_of_four_oct26_2021'
"""
   
