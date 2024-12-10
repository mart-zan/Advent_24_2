import numpy as np
# Advent of code
# --- Day 2: Red-Nosed Reports ---
def read_reports(filename: str):
    my_file = open(filename, "r")
    data = my_file.read()
    rows = data.strip().split('\n')  # Split text into each row
    my_file.close()
    # Returns
    return rows

def all_same_sign(list_numbers):
    # Check if all numbers are plus or minus. If they are all same, returns true value.
    # If there is a zero, return false. If there is at least one different sign, returns false.
    if all(col > 0 for col in list_numbers):
        return True
    elif all(col < 0 for col in list_numbers):
        return True
    else:
        return False

def problem_dampener(list_numbers):
    # Takes report and creates a dampened report without one mistaken number (that does not fall to the consitions).
    if any(col == 0 for col in report):
        where_zero = list_numbers.item(0)
        report.remove(where_zero[0])


if __name__ == '__main__':
    # Read and close file
    reports = read_reports("input.txt")
    save_reports = 0
    for i, report in enumerate(reports):
        # report from string to numbers
        report = report.strip().split(' ')
        report = list(map(int, report))  # integer from string
        # Create dampened report for second task

        # Make difference to check plus/minus (ascend/descend)
        diffs_report = [report[j + 1] - report[j] for j in range(len(report)-1)]
        # Check all conditions
        if all_same_sign(diffs_report):
            if all(np.abs(y) < 4 for y in diffs_report):
                save_reports = save_reports + 1

    print('In unusual data from the Red-Nosed reactor is ' + str(save_reports) + ' save reports.')
