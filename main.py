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
    """
    Check if all numbers are plus or minus. If they are all same, returns true value.
    If there is a zero, return false. If there is at least one different sign, returns false.
    """

    if all(col > 0 for col in list_numbers):
        return 1
    elif all(col < 0 for col in list_numbers):
        return 1
    else:
        return 0

def problem_dampener(x):
    """
    Checks if a report can become safe by removing one level.
    """
    n = len(x)
    for i in range(n):
        # Create a modified sequence by removing one level
        modified_report = x[:i] + x[i+1:]
        # Compute differences for the modified sequence
        diffsx = [int(modified_report[j+1] - modified_report[j]) for j in range(len(modified_report) - 1)]
        # Check if the modified report is safe
        if (all_same_sign(diffsx)) and all(np.abs(y) < 4 for y in diffsx):
            return 1
    return 0

if __name__ == '__main__':
    # Read and close file
    reports = read_reports("input.txt")
    save_reports = 0
    save_reports_dumpened = 0

    for i, report in enumerate(reports):

        # report from string to numbers
        report = report.strip().split(' ')
        report = list(map(int, report))  # integer from string

        # Make difference to check plus/minus (ascend/descend)
        diffs_report = [int(report[j + 1] - report[j]) for j in range(len(report)-1)]

        # Check all conditions for safe report
        if (all_same_sign(diffs_report)) and all(np.abs(y) < 4 for y in diffs_report):
            save_reports += 1
            save_reports_dumpened += 1
        else: # check the problem dampener
            result_dump = problem_dampener(diffs_report)
            save_reports_dumpened = save_reports_dumpened + result_dump

    print('In unusual data from the Red-Nosed reactor is ' + str(save_reports) + ' safe reports.')
    print('With problem dampener there are ' + str(save_reports_dumpened) + ' safe reports.')
