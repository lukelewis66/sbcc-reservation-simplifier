#this script was written by Luke Lewis and is his intellectual property
#files must be downloaded as complete, NOT html only
#opening our file
import os, webbrowser
input_filename = "/Viewing Reservation.html"
output_filename = "form.html"
path = os.path.dirname(os.path.realpath(__file__))
htmlFile = open(path + input_filename, "r", encoding="utf-8")
htmlString = htmlFile.read()

#name/email
atFind = htmlString.index('@')
emailFind = htmlString.index('<', atFind)
eLoc = emailFind
while htmlString[eLoc] != ">":
    eLoc -= 1
email = htmlString[eLoc+1:emailFind]

#resources
resourceFind = htmlString.index('<label>Resources</label>')
rLoc = resourceFind
rLoc = rLoc + 18
fLoc = rLoc
while htmlString[fLoc:fLoc+len('</div>')] != '</div>':
    fLoc += 1
resources = htmlString[rLoc + 5:fLoc]
resources_lst = resources.split('\n')
sanitized_lst = []
resourceCount_lst = []
i = 0
for resource in resources_lst:
    if len(resource.strip()) > 1:
        i += 1
        singlesource = resource.strip()
        if i % 2 == 0:
            sanitized_lst.append('<li style=\"background-color:#DCDCDC\">' + singlesource[1:len(singlesource)].strip())
            resourceCount_lst.append('<li style=\"background-color:#DCDCDC\">')
        if i % 2 != 0:
            sanitized_lst.append('<li>' + singlesource[1:len(singlesource)].strip())
            resourceCount_lst.append('<li>')
resources_str = ''.join(sanitized_lst)
resourceCount_str= '<br>'.join(resourceCount_lst)



#begin and end
beginFind = htmlString.index('>Begin</label>')
bLoc = beginFind + 15
beginDate = htmlString[bLoc:bLoc + 10]
bTime = htmlString.index('BeginPeriod')
bTime += 20
beginTime = htmlString[bTime:bTime + 5]
beginAll = beginDate + "          " + beginTime
endFind = htmlString.index('>End</label>')
eeLoc = endFind + 13
endDate = htmlString[eeLoc:eeLoc + 10]
eTime = htmlString.index('EndPeriod')
eTime += 18
endTime = htmlString[eTime:eTime + 5]
endAll = endDate + "          " + endTime


#description
if 'Description of reservation' in htmlString:
    descriptionFind = htmlString.index('Description of reservation')
    dLoc = htmlString.index('>', descriptionFind)
    dLoc = htmlString.index('>', dLoc)
    dEnd = htmlString.index('</div>', dLoc)
    description = htmlString[dLoc + 5:dEnd]
    description = description.strip()
    if 'no-data' in description:
        description = 'none'
    else:
        dLoc2 = htmlString.index('>', dLoc + 5)
        dLoc2 += 2
        description = htmlString[dLoc2:dEnd]
        description = description.strip()

#class name
classFind = htmlString.index('Class Name</label')
cLoc = htmlString.index('attributeValue', classFind)
cLoc += 17
ecLoc = htmlString.index('<', cLoc)
className = htmlString[cLoc:ecLoc]

#instructor
instructorFind = htmlString.index('Instructor</label')
iLoc = htmlString.index('attributeValue', instructorFind)
iLoc += 17
eiLoc = htmlString.index('<', iLoc)
instructor = htmlString[iLoc:eiLoc]

#assignment
assignmentFind = htmlString.index('Assignment</label')
aLoc = htmlString.index('attributeValue', assignmentFind)
aLoc += 17
eaLoc = htmlString.index('<', aLoc)
assignment = htmlString[aLoc:eaLoc]

data = dict()
data['resources'] = resources_str
data['resourceCount'] = resourceCount_str
data['name_email'] = email
data['begin_date'] = beginDate
data['begin_time'] = beginTime
data['end_date'] = endDate
data['end_time'] = endTime
data['class_name'] = className
data['instructor_'] = instructor
data['assignment_'] = assignment
data['description_'] = description
data['pending'] = 'APPROVAL PENDING'
template_path = path + '/form_template.html'
output_path = path + '/' + output_filename
def outputForm(data, path=output_path):
    infile = open(template_path, 'r')
    contents = infile.read()
    contents = contents.replace('_resources_list', data['resources'])
    contents = contents.replace('_name_email', data['name_email'])
    contents = contents.replace('begin_date', data['begin_date'])
    contents = contents.replace('begin_time', data['begin_time'])
    contents = contents.replace('end_date', data['end_date'])
    contents = contents.replace('end_time', data['end_time'])
    contents = contents.replace('class_name', data['class_name'])
    contents = contents.replace('instructor_name', data['instructor_'])
    contents = contents.replace('assignment_name', data['assignment_'])
    contents = contents.replace('_packed', data['resourceCount'])
    contents = contents.replace('_returned', data['resourceCount'])
    contents = contents.replace('_description', data['description_'])
    contents = contents.replace('_pending', data['pending'])
    outfile = open(output_filename, 'w', encoding="utf-8")
    outfile.write(contents)
    infile.close()
    outfile.close()
    
outputForm(data)
safari_path = 'open -a /Applications/Safari.app %s'
webbrowser.get(safari_path).open('file://' + output_path)
