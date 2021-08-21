# Course list

## Motivation and why

I came up with this idea when I tried to register for the course I want in registration.
I felt there is a lot of space to improve our process of registration courses, and I want to make it easy for everyone to access the course for the upcoming term. So I start creating this project.


## Problem of the registration process before I start this project
When students register for their course for the upcoming course, they have to stare at both the full-name class schedule and class schedule at the same time and register for their class. In the full name class schedule, we can understand what course there will be open for an upcoming term but don't know which day or what time there will be. But in the class schedule, we can understand which day, what time, and which section we can take a course, and customize what time slot we want to make. 

## Built with

Django    --> 3.1.6 <br>
Python    --> 3.7.6 <br>
Bootstrap --> 5.0.2 <br>
SQlite3   --> 3.11.2 <br>


## What changes happen after I start this project
First off, the problem above is we have to stare at the two papers to choose what course should we take when we register for the course in the registration.
To prevent this, I combined information as an attribute in the database from both full name class schedule and class schedule:

- course code
- course name 
- prerequisite

and information which is from the class schedule:

- which day
- what time
- which section
- which room
- lecture name

Just in case, I also combined descriptions for each of the courses. Because I assume that lecturers may want to comment on something for their class.
So, using the information I chose above, we don't have to stare at two papers and think about what course I should take, what time, which day or what section, etc.
But now, everyone can see the course information based on the above, and you don't have to stare at two papers anymore.


## What I learned from this project


Things I learned:

- How to set up app and project 
- How to set up a webpage from settings.py, and create urls.py and views.py in-app
- How To setup static for creating CSS, bootstrap, and JS from settings.py to creating templates
- How to create models.py for the database with sqlite3
- How to make a migration for database
- How to use faker to populate courses
- How to setup admin panel
- How to print out based on the database into the specific template

I learned many things more than that. 
I appreciate python and Django communities are big communities to help each other.


## Current Features
- Page simply is showed course list 

## Upcoming Features
- Searching box based on course code
- Make a better looking





