import re
import csv
from pprint import pprint

with open("phonebook_raw.csv", encoding="UTF-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

def index_sorting_phoneformat():
    for li in contacts_list[1:]:
        line = li[0] + ' ' + li[1] + ' ' + li[2]
        pattern_obj = (r'\w+')
        result = re.findall(pattern_obj, line)
        for it in result:
            li[result.index(it)] = it
        pattern_obj = re.compile(
            r"(\+7|8)(\s*)?(\()?(\d{3})(\))?(\s*|-)?(\d{3})([-\s]+)?(\d{2})([-\s]+)?(\d{2})((\s*)?(\()?((доб.) (\d+))(\))?)?")
        li[5] = pattern_obj.sub(r"+7(\4)\7-\9-\11 \16\17", li[5])

def data_aggregation():
    k = 0
    while k < len(contacts_list) - 1:
        for lk in contacts_list:
            if contacts_list[k][0] == lk[0] and contacts_list[k][1] == lk[1] and contacts_list[k] != contacts_list[contacts_list.index(lk)]:
                new_list = [list1 or list2 for list1, list2 in zip(contacts_list[k], contacts_list[contacts_list.index(lk)])]
                contacts_list[k] = new_list
                contacts_list.remove(contacts_list[contacts_list.index(lk)])
        k += 1

def data_recording():
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)

def main():
    index_sorting_phoneformat()
    data_aggregation()
    data_recording()
    pprint(contacts_list)

if __name__ == '__main__':
    main()