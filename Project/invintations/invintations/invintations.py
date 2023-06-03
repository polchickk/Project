import csv

def positionData(row):
    work = row[6].split()
    for i in range(len(work)):
        if work[i][-2] == '�' and work[i][-1] == '�':
            work[i] = work[i][:-2] + '���'
        elif work[i][-1] == '�' or work[i][-1] == '�':
            work[i] = work[i] + '�'
    position = ' '.join(work)
    return position

def affiliationGen(row):
    job = row[5].split()
    for i in range(len(job)):
        if len(job[i]) >= 2:
            if job[i][-2] == '�' and job[i][-1] == '�':
                job[i] = job[i][:-2] + '���'
            elif job[i][-2] == '�' and job[i][-1] == '�':
                job[i] = job[i][:-2] + '���'
            elif job[i][-1] == '�':
                job[i] = job[i] + '�'
    institute = ' '.join(job)
    return institute

def surnameData(row):
    surname = row[1].split()[-1]
    if surname.endswith('��') or surname.endswith('��') or surname.endswith('��') or surname.endswith('��'):
        surname += '�'
    elif surname.endswith('���') or surname.endswith('���') or surname.endswith('���') or surname.endswith(
            '���'):
        surname = surname[:-1] + '��'
    elif surname.endswith('��') or surname.endswith('��') or surname.endswith('��') or surname.endswith('��'):
        surname = surname[:-2] + '���'
    elif surname.endswith('��'):
        surname = surname[:-2] + '��'
    elif surname.endswith('��'):
        surname = surname[:-2] + '��'
    else:
        surname = surname
    return surname


def gender_by_patronymic(patronymic):
    male_suffixes = ['����', '����', '��']
    if any(patronymic.endswith(suffix) for suffix in male_suffixes):
        return '�'
    else:
        return '�'

def adv(row):
    if gender_by_patronymic(row[3]) == '�':
        gender_end = "���������"
    else:
        gender_end = "���������"
    return gender_end

with open("������������ ���� ������.csv", newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    with open("������������ ������� �����������.tex", 'r', encoding='utf-8') as input_file:
        input_str = input_file.read()
        i=0
        for row in reader:
            pos = input_str.replace('PositionDat', positionData(row)).replace('AffiliationGen', affiliationGen(row))\
            .replace('SurnameDat',surnameData(row)).replace('NameF', row[2][0]).replace('PatronimF', row[3][0]).replace('���������',adv(row))\
            .replace('Name',row[2]).replace('Patronim',row[3])

            with open(f'invintation{i}.tex', 'w') as output_file:
                output_file.write(pos)
            i+=1

