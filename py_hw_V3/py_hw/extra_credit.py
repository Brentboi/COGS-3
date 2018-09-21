'''
DIRECTIONS:
Hello! Welcome to the extra credit. You should have done the "warmup" by now. This part is an extension of our "excel" assignment. As you can see, we're using a lot of the same data as before, except this time we're going to manipulate things in Python instead of in Excel. We've included some sample outputs for each function, but you can also test things by in your terminal running:

>>> python test.py

Note, that you will get an error if you're not using python 3 with this. Please make sure you're using Python 3 as this is what we will be performing the final tests with.
'''

'''
Global Variables DO NOT EDIT THIS LINE
'''
data, names = [], []

'''
This function iterates through two file names and somehow stores their data.
How does it do this exactly?

DO NOT change this function, but look through the function and try to understand what's going on. Look up "python list comprehension" for a more thorough understanding.
'''
def import_files():
    files = ['data.txt', 'names.txt']
    for f in files:
        this_file = open(str(f), 'r')
        for line in this_file:
            if f == 'data.txt':
                line = line.split()
                line = [int(line[i]) if i != 0 else line[i] for i in range(len(line))]
                data.append(line)
            else:
                names.append(line.split())
        this_file.close()


'''
Now we want to capture a row from the "data" array given
a student's ID.

That is, the function below takes an id (as a string) and return
the row in the data array associated with it.

For instance, get_row_from_id("A0027") should return
["A0027", 16, 20, 19, 19]

Run the test.py file for more test cases.

If the function is given an invalid ID the function should return False.
'''
def get_row_from_id(id):
    # YOU'RE IMPLIMENTATION HERE!
    return None


'''
Now that we can grab a row based on student ID, we want to calculate
a given student's average on the quizes. That is, given a student
id we want to calculate the average of that student's quiz scores.

You should use the function get_row_from_id() in your solution.

For this function it is safe to assume that the students we're asking
about have each taken all 4 quizes.

So:
calc_avg_per_student('A0009')
>> 15.0

calc_avg_per_student('A0006')
>> 19.25

calc_avg_per_student('A0016')
>> 15.25
'''
def calc_avg_per_student(id):
    # YOU'RE IMPLIMENTATION HERE!
    return None


'''
Now we want to calculate the class average for a given test.
That is, given a test ID, calculate the average of class on that test.
You may assume that you will only be given a test_id where every
student has taken that test.

If a test_id that is less than 0 or greater than 3 is given, return False.

REMEMBER!! In programming languages we start counting at 0. So test_id 0 is the
first test!!

For example:
calc_avg_per_test(0)
>> 15.717948717948717

calc_avg_per_test(1)
>> 16.28205128205128

calc_avg_per_test(2)
>> 16.71794871794872

calc_avg_per_test(3)
>> False
'''
def calc_avg_per_test(test_id):
    # YOU'RE IMPLIMENTATION HERE!
    return None


'''
Now we want to get a student's name from their ID.
This is the first time you will need to utilize the names array.

Sample output:

get_name_from_id('A0014')
>> 'Barney Gumbell'

get_name_from_id('A0010')
>> 'Selma Bouvier'

get_name_from_id('A0016')
>> 'Lisa Simpson'

get_name_from_id('XXX')
>> False
'''
def get_name_from_id(id):
    # YOU'RE IMPLIMENTATION HERE!
    return None


'''
Given a student's full name, return their average on all tests.
You should utilize the functions we've defined above in your solution.

Sample output:

print_grade_from_name('Lisa Simpson')
>> 15.25

print_grade_from_name('Silvia Winfield')
>> 14.75

print_grade_from_name('Seymour Skiner')
>> 16.75

print_grade_from_name('Rick Sanchez')
>> False
'''
def print_grade_from_name(name):
    # YOU'RE IMPLIMENTATION HERE!
    return None


# That's it! Do not touch the line below.
import_files()
