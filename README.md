Course list

Motivation and why

I came up this idea when I tried to register the course I want in the registration.
I felt there is a lot space to improve our process of registration course, 
and I want to make it easy for everyone to access the course for the upcoming term.
So I start creating this project.


Problem of the registration process before I start this project:
When students register their course for the upcoming course, they have to stare at both the full-name class schedule and class schedule at same time, 
and register their class. In the full name class schedule, we can understand what course there will be open for upcoming term, 
but don't know which day or what time there will be. But in the class schedule, we can understand which day, what time,
and which section we can take a course, and customize what time-slot we want to make. 

Built 

Django    --> 3.1.6
Python    --> 3.7.6
Bootstrap --> 5.0.2


What changes happen after I start this project:
First off, problems above is we have to stare at the two papers to choose what course should we take when we register the course in the registration.
To prevent this, I combined information as attribute in the database from both full name class schedule and class schedule:

- course code
- course name 
- prerequisite

and information which is from class schedule:

- which day
- what time
- which section
- which room
- lecture name

Just in case, I also combined description for each of course. Because I assume that lectures may want to comment something for their class.
So, using those information I chose above, we don't have to stare at two papers, and think about what course I should take, what time, which day or what section etc.
But now,everyone can see the course information based on above, and you don't have to stare at two papers anymore.


What I learned from this project


I leaernd how:

- To setup app and project 
- To setup webpage from settings.py, and create urls.py and views.py in app
- To setup static for creating CSS, bootstrap, and JS from settings.py to creating templates
- To create models.py for database with sqlite3
- To make a migration for database
- To use faker to populate courses
- To setup admin panel
- To print out based on the database into the specific template

I really apprecite python and django community are big community to help each other..


Current Features
- Page simply is showed course list 

Upcoming Features
- Searching box based on course code
- Make a better looking





