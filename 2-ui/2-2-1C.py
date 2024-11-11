from IPython.display import display
from ipywidgets import interact_manual


# Challenge 2-2-1

# Let's create a simple widget interaction for display student status for their GPA:

# inputs:

# - student name
# - major: one of "IMT", "IST", or "ADA"
# - gpa between 0.0 and 4.0

# process:

# - when gpa < 1.8 then status is "probation"
# - when gpa > 3.4 then status is "deans list"
# - else status is "no list"

# output:

# - display the following statement:
#     "NAME in MAJOR with GPA is on STATUS" 

name = 'Enter your name'
major =  ["IMT", "IST",  "ADA"]
gpa1, gpa2 = 0.0 , 4.0

"""
The interact manuel with ipwidgets creates user intercase UI to 
explore code and data, then calls the function with those elements
"""
@interact_manual(student_name = name, pick_major = major, grade = (gpa1, gpa2))

def simple_Widget(student_name, pick_major, grade):  
  
    if grade < 1.8:
        display(f"{student_name} in {pick_major}, with {grade} is on {'probation'}")
                
    elif grade > 3.4:
        display(f"{student_name} in {pick_major} with {grade} is on {'deans list'}")
        
    else:
        display(f"{student_name} in {pick_major} with {grade} is on {'no list'}") 






