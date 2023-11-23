# Mohammad Khan
# 1986351

import csv
from datetime import datetime


if __name__ == '__main__':
    files = ['ManufacturerList.csv', 'ServiceDatesList.csv', 'PriceList.csv']
    data = {}
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                itemID = row[0]
                if file == 'ManufacturerList.csv':
                    data[itemID] = {}
                    manf_name = row[1]
                    item_typ = row[2]
                    damg_ind = row[3]
                    data[itemID]['manufacturer'] = manf_name.strip()
                    data[itemID]['item type'] = item_typ.strip()
                    data[itemID]['damage'] = damg_ind
                elif file == 'ServiceDatesList.csv':
                    service_date = row[1]
                    data[itemID]['service date'] = service_date
                elif file == 'PriceList.csv':
                    item_price = row[1]
                    data[itemID]['item price'] = item_price

    manf = []
    itemTyp = []

    for item in data:
        find_manf = data[item]['manufacturer']
        find_typ = data[item]['item type']
        if find_manf not in itemTyp:
            manf.append(find_manf)
        if find_typ not in itemTyp:
            itemTyp.append(find_typ)

    ask = None
    while ask != 'q':
        ask = input("Enter Item Manufacturer and Type. Enter q to Quit.\n")
        if ask == 'q':
            break
        else:
            ask = ask.split()
            user_manf = None
            user_typ = None
            incorrect = False
            for word in ask:
                if word in manf:
                    if user_manf:
                        incorrect = True
                    else:
                        user_manf = word
                elif word in itemTyp:
                    if user_typ:
                        incorrect = True
                    else:
                        user_typ = word

            if not user_manf or not user_typ or incorrect:
                print("No such item in inventory")
            else:
                info = sorted(data.keys(), key=data.get('item price'), reverse=True)
                matching = []
                alike = {}

                for item in info:
                    if data[item]['item type'] == user_typ:
                        service_date = data[item]['service date']
                        today = datetime.now().date()
                        expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                        expire = expiration < today
                        if data[item]['manufacturer'] == user_manf:
                            if not expire and not data[item]['damage']:
                                matching.append((item, data[item]))
                        else:
                            if not expire and not data[item]['damage']:
                                alike[item] = data[item]

                if matching:
                    item = matching[0]
                    itemID = item[0]
                    manf_name = item[1]['manufacturer']
                    item_typ = item[1]['item type']
                    item_price = item[1]['item price']
                    print("You item is: {}, {}, {}, {}\n".format(itemID, manf_name, item_typ, item_price))

                    if alike:
                        matching_price = item_price 
                        near_price = None
                        near_item = None

                        for item in alike:
                            if near_price == None:
                                near_item = alike[item]
                                near_price = abs(int(matching_price) - int(alike[item]['item price']))
                                itemID = item
                                manf_name = alike[item]['manufacturer']
                                item_typ = alike[item]['item type']
                                price = alike[item]['item price']
                                continue
                            diff = abs(int(matching_price) - int(alike[item]['item price']))
                            if diff < near_price:
                                near_item = item
                                near_price = diff
                                itemID = item
                                manf_name = alike[item]['manufacturer']
                                item_typ = alike[item]['item type']
                                price = alike[item]['item price']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(itemID, manf_name, item_typ, item_price))
                else:
                    print("No such item in inventory")
