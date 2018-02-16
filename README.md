# sbcc-reservation-simplifier

Python script written to simplify SBCC Film & TV department's reservation forms. Also uses html for the form template, which was made in Kompozer.

SBCC Film & TV utilizes a free online booking software for students to reserve and checkout film gear for their class projects. The software works fine, however the form that it outputs when a reservation is made is not very satisfactory. Readability is not great, with a lot of redundant information not needed by the department. 

How to use:
  1. Download the reservation form off of booked website (as complete html file).
  2. Do not change the name of the download file. 
  3. There will be two cases: approved and unapproved reservations. Both contain different html, so I just wrote two different    scripts to parse either one. 
  4. run RUN_ME.py for approved reservations and UNAPPROVED_RUN_ME for unapproved.
  5. Browser should automatically be opened with improved form ready to be printed. 
  
  
