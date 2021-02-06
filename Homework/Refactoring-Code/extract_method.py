# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math 

def print_stat():
    grade_list = get_grade_list()

    # Calculate the mean and standard deviation of the grades
    total = 0 # Do you think 'sum' is a good var name? Run pylint to figure out!
    for grade in grade_list:
        total = total + grade
    mean = total / len(grade_list)

    sd = find_standard_deviation(grade_list, mean)
    # print out the mean and standard deviation in a nice format.
    print_out(mean, sd)

def find_standard_deviation(grade_list, mean):
    sd = 0 # standard deviation
    sum_of_sqrs = 0
    for grade in grade_list:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grade_list))
    return sd

def get_grade_list():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(0, n_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def print_out(mean, sd):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_stat()
