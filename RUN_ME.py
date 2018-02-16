#this script was written by Luke Lewis and is his intellectual property
#files must be downloaded as complete, NOT html only
#opening our file
import os, webbrowser
input_filename = "/Editing Reservation.html"
output_filename = "form.html"
path = os.path.dirname(os.path.realpath(__file__))
htmlFile = open(path + input_filename, "r", encoding="utf-8")
htmlString = htmlFile.read()


#name/email
atFind = htmlString.index('data-userid')
emailFind = htmlString.index('<', atFind)
eLoc = emailFind
while htmlString[eLoc] != ">":
    eLoc -= 1
email = htmlString[eLoc+1:emailFind]

#resources
resourceLocate = "resource-details-bound"
resourceIndex = 0
resourceLst = []
resourceCountLst = []
i = 0
while resourceIndex != -1:
    resourceIndex = htmlString.find(resourceLocate, resourceIndex + 1)
    if resourceIndex != -1:
        i += 1
        rStart = htmlString.index('>', resourceIndex)
        rEnd = htmlString.index('<', rStart)
        curResource = htmlString[rStart+1:rEnd]
        if i % 2 == 0:
            resourceLst.append('<li style=\"background-color:#DCDCDC\">' + curResource)
            resourceCountLst.append('<li style=\"background-color:#DCDCDC\">')
        else:
            resourceLst.append('<li>' + curResource)
            resourceCountLst.append('<li>')
resources_str = ''.join(resourceLst)
resourceCount_str = '<br>'.join(resourceCountLst)

#begin and end
dateFind = htmlString.index('reservation.init')
starter = htmlString.index(',', dateFind)
startLst = []
endLst = []
starter = htmlString.index('\'', starter+1)
ender = htmlString.index('\'', starter+1)
start = htmlString[starter+1:ender-3]
startLst = start.split(' ')
beginDate = startLst[0]
beginTime = startLst[1]
starter = htmlString.index('\'', ender+1)
ender = htmlString.index('\'', starter + 1)
end = htmlString[starter+1:ender-3]
endLst = end.split(' ')
endDate = endLst[0]
endTime = endLst[1]

#description
if 'Description of reservation' in htmlString:
    descriptionFind = htmlString.index('Description of reservation')
    dLoc = htmlString.index('>', descriptionFind)
    dLoc = htmlString.index('>', dLoc)
    dEnd = htmlString.index('</div>', dLoc)
    description = htmlString[dLoc+4:dEnd]
    description = description.strip()
    if 'no-data' in description:
        description = 'none'
    else:
        dLoc2 = htmlString.index('>', dLoc + 5)
        dLoc2 += 1
        description = htmlString[dLoc2:dEnd]
        description = description.strip()

#class name
classFind = htmlString.index('Class Name</label')
cLoc = htmlString.index('selected=', classFind)
cLoc += 20
ecLoc = htmlString.index('<', cLoc)
className = htmlString[cLoc:ecLoc]

#new instructor
instructorFind = htmlString.index('Instructor</label')
iLoc = htmlString.index('selected', instructorFind)
iLoc = htmlString.index('>', iLoc)
eiLoc = htmlString.index('<', iLoc)
instructor = htmlString[iLoc+1:eiLoc]

#assignment
assignmentFind = htmlString.index('Assignment</label')
aLoc = htmlString.index('value=', assignmentFind)
aLoc += 7
eaLoc = htmlString.index('\"', aLoc)
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
template_path = path + '/form_template.html'
output_path = path + '/' + output_filename

#opening output file template and replacing key elements
def outputForm(data, path=output_path):
    infile = open(template_path, 'r', encoding='utf-8')
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
    contents = contents.replace('_pending', '')
    outfile = open(output_filename, 'w', encoding='utf-8')
    outfile.write(contents)
    infile.close()
    outfile.close()
    
outputForm(data)
safari_path = 'open -a /Applications/Safari.app %s'
webbrowser.get(safari_path).open('file://' + output_path)
