import os

path = os.path.expanduser('~\\Desktop\\notepad.txt')

with open(path, 'w', encoding='utf-8') as f:
    f.write('님 컴퓨터 해킹됨 ㅋㅋ' * 999)

while True:
    os.system(f"notepad.exe {path}")