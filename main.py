import xml.etree.ElementTree as ET
from Dataflow import Dataflow

print('Parsing input xml')
mytree = ET.parse('ods.xml')
myroot = mytree.getroot()

def print_nice(indent, *args):
    print(indent*'\t', *args)

def process_steps(steps, indent=1):
    print_nice(indent, 'Printing steps')
    for j in steps:
        print_nice(indent, j.tag)
        if j.tag == 'DIScript':
            script_name = j.find('DIUIOptions').findall('DIAttribute')[0].attrib['value']
            content = j.find('DIUIOptions').findall('DIAttribute')[1].attrib['value']
            print_nice(indent, 'Found Script named', script_name)
            print_nice(indent, 'Saving contents')
            with open(f'scripts/{job_name}_{script_name}.txt', 'w') as f:
                f.write(content)
        elif j.tag == 'DICallStep':
            call_name = j.attrib['name']
            print_nice(indent, 'Found CallStep named', call_name)
        elif j.tag == 'DIWhileStep':
            while_name = j.find('DIUIOptions').findall('DIAttribute')[0].attrib['value']
            while_cond = j.find('DIExpression').attrib['expr']
            print_nice(indent, 'Found WhileStep named', while_name, 'with condition', while_cond)
            process_steps(j.find('DISteps'), indent+1)
        elif j.tag == 'DIIfStep':
            if_name = j.find('DIUIOptions').findall('DIAttribute')[1].attrib['value']
            print_nice(indent, 'Found IfStep with name', if_name)
            print_nice(indent, 'Processing if option')
            process_steps(j.find('DIIf'), indent+1)
            if j.find('DIElse'):
                process_steps(j.find('DIElse'), indent+1)
            else:
                print_nice(indent, 'Skipping else')
            print_nice(indent, 'Processing else option')
# def process_targets(query, indent=1):


# for i in myroot.findall('DIJob'):
i = myroot.findall('DIJob')[0]
job_name = i.attrib['name']
print('\nFound job named', job_name)
print('Job', job_name, 'has', len(i[1]), 'steps')
# process_steps(i[1])
workflows =  myroot.findall('DIWorkflow')
dataflows = myroot.findall('DIDataflow')
print('File has', len(dataflows), 'dataflows')
# for dataflow in dataflows:
# process_dataflows(dataflows[0])
# for dataflow in dataflows:
dataflow = Dataflow(dataflows[1])
dataflow.process_dataflows()
dataflow.create_excel()