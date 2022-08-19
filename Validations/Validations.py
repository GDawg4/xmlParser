import xml.etree.ElementTree as ET

xml_file = 'odsVozCarga.xml'

tree = ET.parse(xml_file)
root = tree.getroot()
Validations = [] # List of Validations
Sources = {}

# Get quantity of validations
cantValidations = root.findall(".//Rule[@Enabled='true']")
# Get element of tree with name of validation
child = root.findall(".//Rule[@Enabled='true']/Expression/Custom")
extraSources = root.findall(".//DITransformCall[@name!='Validation']")

print('Has ', len(cantValidations), ' validations')

# For extra validations
for elem in extraSources:
    tempValue = (elem.attrib['name'])
    # Merge
    if elem.attrib['name'] == 'Merge':
        res = 'N/A'
        Sources[tempValue] = res
    # Case Operation
    elif elem.attrib['name'] == 'Case_Operation':
        tempo = elem.findall('./DICase/*')
        res = 'CASE:'
        # For taking each case of operator.
        for el in tempo:
            caseVal = ''
            caseVal = (el.attrib['label'] + ': ')
            # Check if the instruction is default
            if el.attrib['isDefault'] == 'true':
                caseVal += 'default'
            else:
                operators = el.find('./DIExpression')
                caseVal += operators.attrib['expr']
            res += (" " + caseVal)
        Sources[tempValue]=res

print(Sources)

# To do: Get del nombre del source de las Validaciones 
for i in range(len(child)):
    temp = "Validation" + str(i+1) + " Pass: " + child[i].text
    Validations.append(temp)

for i in Validations:
    print(i)