# try wrapping the code below that reads a persons.csv file in a class and make it more general such that it can read in any csv file

import csv, os, copy
#
# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
# persons = []
# with open(os.path.join(__location__, 'persons.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         persons.append(dict(r))
# print(persons)

# ================[ try wrapping: ]=================
class CSVReader:
    def __init__(self, filename):
        self.data = []
        self.filename = filename
        self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def read_csv(self):
        # data = []
        with open(self.filename) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.data.append(dict(row))
        # return self.data

# ==================================================

# add in code for a Database class


class DB:
    def __init__(self):
        self.database = []

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

    def __repr__(self):
        return self.database

# add in code for a Table class

class Table:
    def __init__(self, table_name, table):
        self.table_name = table_name
        self.table = table

    def update(self, user_id, key, value):
        for i in self.table:
            user_id_key = list(i.keys())[0]
            if i[user_id_key] == user_id:
                i[key] = value
    # def __is_float(self, element):
    #     if element is None:
    #         return False
    #     try:
    #         float(element)
    #         return True
    #     except ValueError:
    #         return False

    def join(self, other_table, common_key):
        joined_table = Table(
            self.table_name + '_joins_' + other_table.table_name, [])
        for item1 in self.table:
            for item2 in other_table.table:
                if item1[common_key] == item2[common_key]:
                    dict1 = copy.deepcopy(item1)
                    dict2 = copy.deepcopy(item2)
                    dict1.update(dict2)
                    joined_table.table.append(dict1)
        return joined_table

    def insert(self, entry):
        if isinstance(entry, dict):
            self.table.append(entry)

    def filter(self, condition):
        filtered_table = Table(self.table_name + '_filtered', [])
        for item1 in self.table:
            if condition(item1):
                filtered_table.table.append(item1)
        return filtered_table

    def aggregate(self, function, aggregation_key):
        temps = []
        for item1 in self.table:
            temps.append(float(item1[aggregation_key]))
        return function(temps)

    def select(self, attributes_list):
        temps = []
        for item1 in self.table:
            dict_temp = {}
            for key in item1:
                if key in attributes_list:
                    dict_temp[key] = item1[key]
            temps.append(dict_temp)
        return temps

    def __str__(self):
        return self.table_name + ':' + str(self.table)

# modify the code in the Table class so that it supports the insert operation where an entry can be added to a list of dictionary
# modify the code in the Table class so that it supports the update operation where an entry's value associated with a key can be updated

# =================[ test code below ]===============================
# reader = CSVReader('persons.csv')
# persons = reader.read_csv()
#
# test_table = Table('persons', persons)
# print(test_table)
# test_DB = DB()
# test_DB.insert(test_table)
#
# test_output_table = test_DB.search("persons") # search the table
# print(test_output_table)
