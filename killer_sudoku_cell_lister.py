import os

def search_cells(cells, target, size=0):
     return_list = []
     if size == 0:
         size = len(cells)
     cell = cells[0]
     remaining_cells = []
     if len(cells) > 1:
         remaining_cells = cells.copy()
         remaining_cells.remove(cell)
     for value in cell:
         remain_tar = target - value
         if remaining_cells:
             other_vals = search_cells(remaining_cells, remain_tar, size)
             if other_vals:
                 for other_val in other_vals:
                     if len(other_val) != size:
                         other_val.append(value)
                     return_list.append(other_val)
         elif remain_tar == 0:
             return_list.append([value])
     return return_list

def clean_search(cells, target):
    cleaned = []
    raw = search_cells(cells, target)
    if raw:
        for_cell = []
        for i in range(len(raw[0])):
            single_cell = []
            for r in raw:
                single_cell.append(r[i])
            for_cell.append(single_cell)
        for f in for_cell:
            cleaned.append(dedupe(f))
        cleaned.reverse()
    return cleaned

def dedupe(val):
     return sorted(list(set(val)))

def validate_input(val):
    try:
        int(val)
        return True
    except:
        return False

while True:
    print('Welcome you filthy cheater')
    print('Enter empty to continue, q to quit')
    cell_list_s = []
    while True:
        cell_val = input('Enter Cell values:')
        if not validate_input(cell_val):
            break
        else:
            cell_list_s.append(cell_val)
    if cell_val != '' and not validate_input(cell_val):
        break
    target_s = input("Target value:")
    try:
        target = int(target_s)
    except:
        target = 0
    if target and cell_list_s:
        cell_list = []
        for cell_s in cell_list_s:
            cell = []
            for i in range(len(cell_s)):
                try:
                    cell.append(int(cell_s[i]))
                except:
                    # Shouldn't be able to reach this state... 
                    os.system('clear')
                    print('Invalide input found goodbye.')
                    break
            cell_list.append(cell)
        results = clean_search(cell_list, target)
        print(f"Results: {results}")
        diff_list = []
        for input_cell, result_cell in zip(cell_list, results):
            diff_list.append([val for val in input_cell if val not in result_cell])
        print(f"Unuseable values: {diff_list}")
    input('Press any key to startover')
    os.system('clear')