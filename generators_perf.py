import random
import time
import resource

RACES = ['human', 'orc', 'elf', 'gnome', 'troll']
NAMES = ['Tomek', 'Ania', 'Karol', 'Gerlat', 'Kasia', 'Aga']

usage = resource.getrusage(resource.RUSAGE_SELF)


def list_npc(num: int) -> list:
    res = []
    for i in range(num):
        npc = {
            'id': i,
            'race': random.choice(RACES),
            'name': random.choice(NAMES)
        }
        res.append(npc)
    return res


def generate_npc(num: int):
    for i in range(num):
        npc = ({
            'id': i,
            'race': random.choice(RACES),
            'name': random.choice(NAMES)
        })
        yield npc


npc = generate_npc(666666)

for name, desc in [
    ('ru_utime', 'User time'),
    ('ru_stime', 'System time'),
    ('ru_maxrss', 'Max. Resident Set Size'),
    ('ru_ixrss', 'Shared Memory Size'),
    ('ru_idrss', 'Unshared Memory Size'),
    ('ru_isrss', 'Stack Size'),
    ('ru_inblock', 'Block inputs'),
    ('ru_oublock', 'Block outputs'),
    ]:
    print('{} {} = {}'.format(desc, name, getattr(usage, name)))
print(f'Time: {time.process_time()}s')
