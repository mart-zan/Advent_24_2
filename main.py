
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
    if all(col > 0 for col in list_numbers):
        return True
    elif all(col < 0 for col in list_numbers):
        return True
    else:
        return False


if __name__ == '__main__':
    # Read and close file
    reports = read_reports("input.txt")
    save_reports = 0
    for i, report in enumerate(reports):
        # report from string to numbers
        report = report.strip().split(' ')
        report = list(map(int, report))  # ineteger from string
        # print(report)
        # Keep safe through conditions
        # safe = True
        # Make difference to check plus/minus (ascend/descend)
        diffs_report = res = [report[j + 1] - report[j] for j in range(len(report)-1)]
        # print(diffs_report)
        # safe_sign =
        # print(safe_sign)
        if all_same_sign(diffs_report):
            if any(y > 3 for y in diffs_report):
                if (all(y != 0 for y in diffs_report)):
                    save_reports = save_reports + 1


    print('In unusual data from the Red-Nosed reactor is ' + str(save_reports) + ' save reports.')
