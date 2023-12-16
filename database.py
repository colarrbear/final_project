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

# csv_reader = ReadCsv('persons.csv')
# print(csv_reader.data)


"""
add in code for a Database class
"""


class DB:
    def __init__(self):
        self.database = []

    def get_all_table_name(self):
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

    def add_table(self, table):  # equal to insert table into database
        if table.table_name not in self.database:
            self.database.append(table)

    def get_table(self, table_name):
        for table in self.database:
            if table.table_name == table_name:
                return table
        return None

    def create_table(self, table_name, initial_data=None):
        if initial_data is None:
            initial_data = None
        new_table = Table(table_name, initial_data)
        self.add_table(new_table)
        return new_table


    # add create table below
    # def create_table(self, table_name, initial_data=None):
    #     """
    #     Creates a new table in the database.
    #
    #     :param table_name: The name of the new table
    #     :param initial_data: Optional initial data for the table, should be a list of dictionaries
    #     """
    #     if initial_data is None:
    #         initial_data = []
    #
    #     new_table = Table(table_name, initial_data)
    #     self.insert(new_table)

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

    # def add_data(self, new_data):
    #     """Add multiple entries to the table."""
    #     for entry in new_data:
    #         self.table.append(entry)
    #
    # def update(self, identifier_key, identifier_value, key, value):
    #     """Update a specific entry in the table."""
    #     for entry in self.table:
    #         if entry.get(identifier_key) == identifier_value:
    #             entry[key] = value
    #             break

    def insert_data(self, new_data: dict):
        """
        Insert new data into the table.
        Assumes all dictionaries in the table have the same keys.
        """
        if not self.table:
            self.table.append(new_data)
        else:
            # Check if the keys in new_data match the keys in the existing table
            existing_keys = set(self.table[0].keys())
            new_data_keys = set(new_data.keys())

            if existing_keys == new_data_keys:
                self.table.append(new_data)
            else:
                raise KeyError("Keys in new data do not match keys in the table")

    def update_data(self, identifier_key, identifier_value, update_key, update_value):
        """
        Update an existing entry in the table.
        """
        updated = False
        for entry in self.table:
            if entry.get(identifier_key) == identifier_value:
                entry[update_key] = update_value
                updated = True
                break
        if not updated:
            raise KeyError(f"No entry found with {identifier_key} = {identifier_value}")

    # def update(self, user_id, key, value):
    #     for i in self.table:
    #         user_id_key = list(i.keys())[0]
    #         if i[user_id_key] == user_id:
    #             i[key] = value


    # def updateTable(self, identifier_key, identifier_value, update_values):
    #     """
    #     Update multiple values in an entry that matches the specified identifier key and value.
    #
    #     :param identifier_key: The key used to identify the entry to update.
    #     :param identifier_value: The value of the identifier key for the entry to update.
    #     :param update_values: A dictionary of key-value pairs to update in the entry.
    #     """
    #     for entry in self.table:
    #         if entry.get(identifier_key) == identifier_value:
    #             for key, value in update_values.items():
    #                 entry[key] = value

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
    # def insert(self, entry, db_instance=None):  # insert table into all table list
    #     if self.table_name in ['Advisor_pending_request Table', 'Member_pending_request table']:
    #         project_id = entry.get('ProjectID')
    #         if project_id is not None and db_instance and not db_instance.project_id_exists(project_id):
    #             raise ValueError(f"ProjectID {project_id} does not exist in Project Table.")
    #     else:
    #         if isinstance(entry, dict):
    #             self.table.append(entry)
    #     # self.table.append(entry)
    #
    # def addData(self, entry):
    #     """
    #     Insert a new entry into the table.
    #
    #     :param entry: A dictionary representing the new entry.
    #     """
    #     if isinstance(entry, dict):
    #         self.table.append(entry)
    #
    # # add function "add field" below
    #
    # def add_field_to_dicts(self, dicts_list, field_name, field_value):  # add field into dict(each table)
    #     """
    #     Add a new field to each dictionary in a list of dictionaries.
    #
    #     :param dicts_list: List of dictionaries
    #     :param field_name: The name of the new field to add
    #     :param field_value: The value of the new field
    #     """
    #     for dict_item in dicts_list:
    #         dict_item[field_name] = field_value

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

