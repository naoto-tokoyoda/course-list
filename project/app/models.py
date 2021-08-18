from django.db import models


# Create your models here.

#set uppercase and no space. ITE101, A.JOHN
class NameField(models.CharField):
    def __init__(self, *args, **kwargs):
        super(NameField, self).__init__(*args, **kwargs)

    def get_prep_value(self, value):
        return str(value).upper()

    
    
class Course(models.Model): 
    first_day = ( 
        ("Mon", "Mon"), 
        ("Tue", "Tue"), 
        ("Wed", "Wed"), 
        ("-", "-"), 
    )
    
    second_day = ( 
        ("Thur", "Thur"), 
        ("Fri", "Fri"), 
        ("Sat", "Sat"), 
        ("-", "-"), 
    )
    
    start_time = ( 
        ("8:30", "8:30"), 
        ("10:30", "10:30"), 
        ("12:30", "12:30"), 
        ("14:30", "14:30"), 
        ("16:30", "16:30"), 
    )  
    
    finish_time = ( 
        ("10:30", "10:30"), 
        ("12:30", "12:30"), 
        ("14:30", "14:30"), 
        ("16:30", "16:30"), 
        ("18:30", "18:30"), 
    ) 
    
    sections = ( 
        ("1", "1"), 
        ("2", "2"), 
        ("3", "3"), 
        ("4", "4"), 
        ("5", "5"), 
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("10", "10"), 
    ) 
    
    rooms = ( 
        ("StEP ONLINE", "StEP ONLINE"), 
        ("1201", "1201"), 
        ("1202", "1202"), 
        ("1203", "1203"), 
        ("1204", "1204"), 
        ("1206", "1206"), 
        ("1301", "1301"), 
        ("1302", "1302"), 
        ("1303", "1303"), 
        ("1304", "1304"), 
        ("1305", "1305"), 
        ("1306", "1306"), 
        ("1401", "1401"), 
        ("1404", "1404"), 
        ("1405", "1405"),
        ("1406", "1406"), 
        ("2202", "2202"), 
        ("2203", "2203"), 
        ("2204", "2204"), 
        ("2205", "2205"),
        ("2206", "2206"), 
        ("2207", "2207"), 
        ("2208", "2208"), 
        ("2301", "2301"), 
        ("2302", "2302"),
        ("2303", "2303"), 
        ("2304", "2304"),
        ("2305", "2305"), 
        ("2306", "2306"),
        ("2401", "2401"), 
        ("2404", "2404"),
        ("2405", "2405"), 
        ("2406", "2406"),
        ("2502", "2502"), 
        ("2503", "2503"),
        ("2504", "2504"), 
        ("2506", "2506"),
        ("Audi.", "Audi."),
        ("STUDIO", "STUDIO"), 
        ("COMLAB", "COMLAB"),
        ("DEMO", "DEMO"), 
        ("Restaurant", "Restaurant"),  
        ("Bar", "Bar"), 
        ("Kitchen", "Kitchen"),
    ) 
    
    
    
    #course id
    id = models.AutoField(primary_key = True)
    #course code
    course_code = NameField(max_length = 128, null = True)
    #course name
    course_name = NameField(max_length = 128, null = True)
    #first day
    first_day = models.CharField(max_length = 128, choices = first_day, default = 'Mon')
    #second day
    second_day = models.CharField(max_length = 128, choices = second_day, default = 'Thur')
    #start_time
    start_time = models.CharField(max_length = 128, choices = start_time, default = '8:30')
    #finish_time 
    finish_time = models.CharField(max_length = 128, choices = finish_time, default = '10:30')
    #section
    section = models.CharField(max_length = 128, choices = sections, default = '1')
    #room
    room = models.CharField(max_length = 128, choices = rooms, default = 'StEP ONLINE')
    #lecture name
    lecture_name = NameField(max_length = 128, null = True)
    #description
    description = models.CharField(max_length = 128, null = True, blank = True)
    #prerequisite
    prerequisite = models.CharField(max_length = 128, null = True, blank = True)
    
    