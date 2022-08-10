def getSubjectMaxStudent(subject:str , dataset:dict):
    max_mark = 0
    max_mark_student = ''

    for name,mark in dataset.items():
        if max_mark < mark:
            max_mark = mark
            max_mark_student = name

    return max_mark , max_mark_student

def getTotalMarks(mark_touple):
    return[mark_touple[1]]
    

lines = None
with open('marks.txt') as file:
    lines = file.readlines()

if not lines:
    print('something went wrong')
    exit()

marks_lines = lines[1:]
exam_result_dic = {}
student_mark = {}
for line in marks_lines : 
    items = line.split(',')
    name = items[0].strip()
    subject = items[1].strip()
    mark = int(items[2].strip())

    if subject not in exam_result_dic:
        exam_result_dic[subject] = {}
    
    exam_result_dic[subject][name] = mark

    previous_mark = student_mark.get(name,0)
    student_mark[name] = previous_mark + mark


msj_list = []

for subject,dataset in exam_result_dic.items():
    max_mark,max_student = getSubjectMaxStudent(subject,dataset)
    msj = f'{max_student} has the highest score {max_mark} for {subject}'
    msj_list.append(msj)

std_mark_list = [ (name,mark) for name,mark in student_mark.items() ]

std_mark_list.sort(key=getTotalMarks, reverse=True)
top = std_mark_list[0]

msj = f'Top Student is {top[0]} with {top[1]} marks'
msj_list.append(msj)


with open('results.txt', 'w') as output_file :
    for msj in msj_list:
        output_file.write(msj)
        output_file.write('\n')