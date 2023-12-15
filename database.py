"""
try wrapping the code below that reads a persons.csv file in a class
and make it more general such that it can read in any csv file
"""

import csv, os, copy

# __location__ = os.path.realpath(
#     os.path.join(os.getcwd(), os.path.dirname(__file__)))
#
# persons = []
# with open(os.path.join(__location__, 'persons.csv')) as f:
#     rows = csv.DictReader(f)
#     for r in rows:
#         persons.append(dict(r))
# print(persons)


class ReadCsv:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_data()

    def read_data(self):
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        data = []
        with open(os.path.join(__location__, self.filename)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return data

csv_reader = ReadCsv('persons.csv')
# print(csv_reader.data)


"""
add in code for a Database class
"""


class DB:
    def __init__(self):
        self.database = []

    def table_name(self):
        return [i.table_name for i in self.database]

    def insert(self, table):
        self.database.append(table)

    def search(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

    # add new def below
    def project_id_exists(self, project_id):
        project_table = self.search('Project Table')
        if project_table:
            return any(row.get('ProjectID') == project_id for row in project_table.table)
        return False

    # def __repr__(self):
    #     return self.database
    def __str__(self):
        return '\n'.join(map(str, self.database))


"""
add in code for a Table class
"""


class Table:
    """
    - modify the code in the Table class so that it supports the insert operation
        where an entry can be added to a list of dictionary

    - modify the code in the Table class so that it supports the update operation
        where an entry's value associated with a key can be updated
    """

    def __init__(self, table_name: str, table: list or dict):
        self.table_name = table_name
        self.table = table
        # self.__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

    def update(self, user_id, key, value):
        for i in self.table:
            user_id_key = list(i.keys())[0]
            if i[user_id_key] == user_id:
                i[key] = value

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

    # def insert(self, entry):
    #     if isinstance(entry, dict):
    #         self.table.append(entry)

    # modify insert below
    def insert(self, entry, db_instance=None):
        if self.table_name in ['Advisor_pending_request Table', 'Member_pending_request table']:
            project_id = entry.get('ProjectID')
            if project_id is not None and db_instance and not db_instance.project_id_exists(project_id):
                raise ValueError(f"ProjectID {project_id} does not exist in Project Table.")
        else:
            if isinstance(entry, dict):
                self.table.append(entry)
        # self.table.append(entry)

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

