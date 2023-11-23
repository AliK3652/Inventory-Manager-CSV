# Mohammad Khan
# 1986351

import csv
from datetime import datetime

class Output:

    def __init__(self, data_list):
        self.data_list = data_list

    def inventory(self):
        with open('FullInventory.csv', 'w') as csvfile:
            data = self.data_list
            info = sorted(data.keys(), key=data.get('manufacturer'))
            for datas in info:
                id = datas
                manf_name = data[datas]['manufacturer']
                item_typ = data[datas]['item type']
                item_price = data[datas]['item price']
                service_date = data[datas]['service date']
                damg_ind = data[datas]['damage']
                csvfile.write('{},{},{},{},{},{}\n'.format(id, manf_name, item_typ, item_price, service_date, damg_ind))
 

    def type(self):
        with open('LaptopInventory.csv', 'w') as csvfile:
            data = self.data_list
            info = sorted(data.keys())
            for datas in info:
                item_typ = data[datas]['item type']
                if item_typ == 'laptop':
                    id = datas
                    manf_name = data[datas]['manufacturer']
                    item_typ = data[datas]['item type']
                    item_price = data[datas]['item price']
                    service_date = data[datas]['service date']
                    damg_ind = data[datas]['damage']
                    csvfile.write('{},{},{},{},{}\n'.format(id, manf_name, item_price, service_date, damg_ind))
        with open('PhoneInventory.csv', 'w') as csvfile:
            data = self.data_list
            info = sorted(data.keys())
            for datas in info:
                item_typ = data[datas]['item type']
                if item_typ == 'phone':
                    id = datas
                    manf_name = data[datas]['manufacturer']
                    item_typ = data[datas]['item type']
                    item_price = data[datas]['item price']
                    service_date = data[datas]['service date']
                    damg_ind = data[datas]['damage']
                    csvfile.write('{},{},{},{},{}\n'.format(id, manf_name, item_price, service_date, damg_ind))       
        with open('TowerInventory.csv', 'w') as csvfile:
            data = self.data_list
            info = sorted(data.keys())
            for datas in info:
                item_typ = data[datas]['item type']
                if item_typ == 'tower':
                    id = datas
                    manf_name = data[datas]['manufacturer']
                    item_typ = data[datas]['item type']
                    item_price = data[datas]['item price']
                    service_date = data[datas]['service date']
                    damg_ind = data[datas]['damage']
                    csvfile.write('{},{},{},{},{}\n'.format(id, manf_name, item_price, service_date, damg_ind))  

    def past(self):
        data = self.data_list
        info = sorted(data.keys(), key=data.get('service date'))
        with open('PastServiceDateInventory.csv', 'w') as csvfile:
            for datas in info:
                service_date = data[datas]['service date']
                today = datetime.now().date()
                expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                if expiration < today:
                    id = datas
                    manf_name = data[datas]['manufacturer']
                    item_typ = data[datas]['item type']
                    item_price = data[datas]['item price']
                    damg_ind = data[datas]['damage']
                    csvfile.write('{},{},{},{},{},{}\n'.format(id, manf_name, item_price, item_typ, service_date, damg_ind))

    def damaged(self):
        with open('DamagedInventory.csv', 'w') as csvfile:
            data = self.data_list
            info = sorted(data.keys(), key=data.get('price'), reverse=True)
            for datas in info:
                id = datas
                manf_name = data[datas]['manufacturer']
                item_typ = data[datas]['item type']
                item_price = data[datas]['item price']
                service_date = data[datas]['service date']
                damg_ind = data[datas]['damage']
                if damg_ind:
                    csvfile.write('{},{},{},{},{}\n'.format(id, manf_name, item_typ, item_price, service_date))
            




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

    Allinventory = Output(data)
    Allinventory.inventory()
    Allinventory.type()
    Allinventory.past()
    Allinventory.damaged()