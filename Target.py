class Target:
    def __init__(self, target):
        self.name = target.attrib['tableName']
        self.input_view = target.find('DIInputView').attrib['name']