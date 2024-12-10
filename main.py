
# Advent of code
# --- Day 2: Red-Nosed Reports ---
def read_reports(filename: str):
    my_file = open(filename, "r")
    data = my_file.read()
    rows = data.strip().split('\n')  # Split text into each row
    my_file.close()
    # Returns
    return rows


if __name__ == '__main__':
    # Read and close file
    reports = read_reports("input.txt")
    print(reports)
    for i, report in enumerate(reports):
        # report from string to numbers
        report = report.strip().split(' ')
        report = list(map(int, report))  # ineteger from string
        print(report)
        # Keep safe through conditions
        safe = True
        # Make difference to check plus/minus (ascend/descend)
        diffs_report = res = [report[j + 1] - report[j] for j in range(len(report)-1)]
        print(diffs_report)
