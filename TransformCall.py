class TransformCall:
    def __init__(self, transform_call):
        self.transform_call = transform_call
        self.name = transform_call.attrib['name']
        self.sql_call = transform_call.find('DIAttributes/DIAttribute[@name="sql_transform_configurations"]/SQLTexts/SQLText/sql_text')
        if self.sql_call:
            self.sql_text = self.sql_call.text
        else:
            self.sql_call = 'None'

    def write_sql_call(self, parent_name):
        with open(f'calls/{parent_name}.{self.name}.txt', 'w') as f:
            f.write(self.sql_call)