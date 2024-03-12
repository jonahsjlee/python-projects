'''
Name: Jonah Lee
Computing ID: wkx9ff
'''

def mean_all(table):
    num_elements = 0
    total_value = 0
    for row in table:
        for g in row:
            total_value += g
            num_elements += 1
    return total_value / num_elements

def mean_by_row(table):
    values_list = []
    for row in table:
        total_row_value = 0
        num_row_elements = 0
        for g in row:
            total_row_value += g
            num_row_elements += 1
        value = total_row_value / num_row_elements
        values_list.append(value)
    return values_list

def mean_by_col(table):
    values_list = []
    num_columns = len(table[0])

    for column in range(num_columns):
        total_col_values = 0
        for row in table:
            total_col_values += row[column]
        values_list.append(total_col_values / len(table))
    return values_list




