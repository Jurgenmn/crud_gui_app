
import csv

from nbformat import read


def read_rows():
    file = open('employees.csv', 'r')
    rows = csv.reader(file, delimiter=',')

    return list(rows)
    

def write_rows(rows):
    file = open('employees.csv', 'w')
    csv_writer = csv.writer(file, delimiter=',')

    for row in rows:
        csv_writer.writerow(row)


def main():
    rows = read_rows()


    first_row = rows[0]
    first_row.insert(0, 'Id')

    counter = 1
    for row in rows[1:]:
        row.insert(0, counter)
        counter += 1

    write_rows(rows)




main()