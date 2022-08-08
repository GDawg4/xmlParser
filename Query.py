class Query:
    def __init__(self, query):
        self.query = query
        self.transforms = {}
        if self.query.find('DIUIOptions/*[@name="ui_display_name"]') is not None:
            self.name = self.query.find('DIUIOptions/*[@name="ui_display_name"]').attrib['value']
        else:
            self.name = "Anonymous"
        if self.query.find('DIUIOptions/*[@name="ui_acta_from_schema_0"]') is not None:
            self.source = self.query.find('DIUIOptions/*[@name="ui_acta_from_schema_0"]').attrib['value']
        else:
            self.source = "Not Found"
        self.elements = self.query.findall('DISchema/DIElement')
        self.expressions = self.query.findall('DISelect/DIProjection/DIExpression')

    def process(self, parent_name):
        with open(f'queries/{parent_name}.{self.name}.txt', 'w') as f:
            for index in range(len(self.elements)):
                self.transforms[self.elements[index].attrib["name"]] = self.expressions[index].attrib["expr"]
                f.write(f'{self.elements[index].attrib["name"]}:{self.expressions[index].attrib["expr"]}\n')
