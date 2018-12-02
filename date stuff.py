#this program calculate days between dates
import datetime
#create an object of the current date. the date variable stores that
date = datetime.date.today()
#this variable stores the second date you input
other_date = input("Enter your date(dd/mm/yyyy):")
#this variable stores your inputed date in a format that calculations can be carried out. the strptime function does that
date_to_right_format = datetime.datetime.strptime(date_of_birth,"%d/%m/%Y").date()
print(date_to_right_format)
#calculates the difference(in days)
calc_age = date - date_to_right_format
#converts the days to years
calcu_age_years = calc_age.days / 365
print(int(calcu_age_years))
