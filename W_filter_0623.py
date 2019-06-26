#coding:utf-8
import os,sys,re,openpyxl,multiprocessing,time

def get_value(row_index):
    return ws.cell(row = row_index,column = i).value

def get_date_row(cell):
    if cell:
        if cell.value == activity_time:
            return cell.row

def get_cell_str(cell):
    if cell: 
        return cell[0]

def not_none(n):
    return n != None

def remove_file(file):
    try:
        os.remove(file)
    except IOError:
        pass

print("Reading the excel data , plese wait a moment!\n")
wb = openpyxl.load_workbook(sys.argv[1])
ws = wb.active
option = {'1':'Tokyo', '2':'Kansai', '3':'Tokai', '0':'eixt'}
row_title = list(ws.rows)[0]
W_match_column = []
match_value = []
nodename_with_spec_char = []
column_value_list = []

while True:
    print("1.Tokyo   2.Kansai   3.Tokai   0.exit\n")
    region_select = input('Please select option upon? [1/2/3/0]\n ==>')
    activity_time = input('Please input the date format [1999-08-08]\n ==>')
    confirm_session = input('are you sure continue ? [Y/y] \n ==>')
    if region_select == '1' and confirm_session in ('Y','y') and activity_time:
        region = option[region_select]
        break
    elif region_select == '2' and confirm_session in ('Y','y') and activity_time:
        region = option[region_select]
        break
    elif region_select == '3' and confirm_session in ('Y','y') and activity_time:
        region = option[region_select]
        break
    elif region_select == '0' and confirm_session in ('Y','y'):
        print("Thank you for using, Bye!")
        sys.exit(0)
    else:
        print('Wrong inout ,please input again.')
        continue

start = time.time()

for cell in row_title:
    if re.search('W併設局#(\d)#?(\d)*$',cell.value):
        W_match_column.append(cell.column)
    elif re.search('UPG Plan$',cell.value):
        date_row_list = list(map(get_cell_str, ws.iter_rows(min_row=1, min_col = cell.column, 
                                          max_col = cell.column, max_row = ws.max_row)))
        temp_date_row = list(map(get_date_row,date_row_list))
        target_date_row = list(filter(not_none,temp_date_row))

for i in W_match_column:
    print('当前正在读取列: ' + ws.cell(row = 1, column = i).value)
    for j in target_date_row:
        if ws.cell(row = j, column = i).value != None:
            column_value_list.append(ws.cell(row = j, column = i).value)
    match_value.append(column_value_list)

with open('W_filter_temp.txt','w+') as f:
    match_value_str = re.sub('[\[\]\' ]','',str(match_value))
    match_value_list = match_value_str.split(',')
    for v in match_value_list:
        v = re.sub('[\' ]','',v)
        if '_' in v or '-' in v:
            nodename_with_spec_char.append(v)   #特殊字符的node写入列表
            v = re.split('[_-]',v)
            for i in v:
                if len(i) >= 4:
                    f.write(i + '\n')
            continue
        f.write(v + '\n')
    f.close()
stop = time.time()

os.system("sed 's/None//g' W_filter_temp.txt | sort -u > W_filter_result.txt")
os.system("sed -i -e 's/None//g' -e '/^$/d' W_filter_result.txt")
number_site = list(os.popen("cat W_filter_result.txt | wc -l"))[0].strip()
os.system("mv W_filter_result.txt " + region + "_W_sitelist_" + number_site)

remove_file('W_filter_temp.txt')
print('#'*10 + "Process completed, please check result ! " + '#'*10 +'\n')
print("special node name below \n")
for spec_char in nodename_with_spec_char:
    print(spec_char)
print('The number of node is : ' + number_site)
print('The whole process  takes ' + str(stop - start)[:4] + 's')