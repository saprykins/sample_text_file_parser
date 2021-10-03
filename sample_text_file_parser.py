import statistics
import argparse


def interface_parser():
    parser = argparse.ArgumentParser(description = "Input action, column numbers and file name")
    parser.add_argument('--a', '-action', default = 1, type = int, help = "choose from 1, 2 or 3 to get max, min or standard deviation values")
    parser.add_argument('--c', '-column', default = 7, type = int, help = "choose column number")
    parser.add_argument('--f', '-file', default = "downld-sample.txt", help = "choose file name")
    args = parser.parse_args()
    return args


def get_a_column(x, file_name):
    # function returns a column number "x"
    # count of columns starts from 0
    # starts to read lines from 3rd line because the lines before are headers
    # function checks catches exceptions related to conversion to numerical type

    a_column = []
    with open(file_name) as feed:
        # line_number starts from 3 because we do not take headers intro account
        line_number = 3 
        for line in list(feed)[3:]:
            try:
                a_column.append(float(line.split()[x]))
            except Exception as e:
                print(f'There is a problem "{e}" on line {line_number} of the file')
            line_number = line_number + 1
        return a_column


def file_test_ok(file_name):
    # function checks if file exists and return True of False
    # commment for developper: need to add a check of data
    
    try:
        open(file_name)
    except FileNotFoundError:
        print("File not found")
        return False
    return True
    

def action_on_column(a, x, file_name):
    # function allows to choose an action from min, max or standard deviation
    # "a" represents an action over a column
    # in case a = 1, it will search for min
    # in case a = 2, it will search for max
    # in case a = 3, it will search for standard deviation
    
    values = get_a_column(x, file_name)
    print(values) 
    if a == 1:
        minimum = min(values)
        print(f"The min value is {minimum:.2f}")
    elif a == 2:
        maximum = max(values)
        print(f"The max value is {maximum:.2f}")
    elif a == 3:
        standard_deviation = statistics.stdev(values)
        print(f"The standard deviation of values is {standard_deviation:.2f}")
    

def main_function():
    # args contains atributes with file name that can be called as args.f
    # as far as actions (called by args.a) and column number (args.c)
    
    args = interface_parser()
    
    action_number = args.a
    column_number = args.c
    file_name = args.f
    
    if file_test_ok(file_name):
        try:
            action_on_column(action_number, column_number, file_name)
        except Exception as e:
            print(f'The following exception raised "{e}"')
    

if __name__ == "__main__":
    main_function()
