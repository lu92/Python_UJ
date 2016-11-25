import re



p = re.compile('ab|bc')
print(p)

print(p.match('bc'))


# zad2

# RUN [[NUMER Z DOKŁADNIE 6 CYFR]] COMPLETED. OUTPUT IN FILE [[NAZWA]].dat. [[COKOLWIEK]]
pattern = "^RUN \d{6} COMPLETED\. OUTPUT IN FILE[a-z]+\.dat\.$"

number2 = 0
with open('atoms.log', 'r') as atoms:
    for line in atoms:
        if re.compile(pattern):
            print(line)
            number2 += 1

print("zad 2: " + str(number2) + " dopasowanych lini")


# zad3a
pattern = ".*Invalid user.*"

number3 = 0
with open('messages.txt', 'r') as atoms:
    for line in atoms:
        if re.compile(pattern):
            print(line)
            number3 += 1

print("zad 3: " + str(number3) + " dopasowanych lini")

# zad3b
# Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
# Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18

pattern3b = "(\w{3}) ( \d|\d\d) (\d\d:\d\d):\d\d .* Invalid user (\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
number3b = 0
moths = {'Jan': 'stycznia', 'Feb':'lutego', 'Mar' : 'Marca', 'Apr':'kwietnia',
         'May':'maja', 'Jun': 'czerwca', 'Jul':'lipca', 'Aug':'sierpnia',
         'Sep':'wrzesnia', 'Oct':'pazdziernika', 'Nov':'listopada', 'Dec':'grudnia'}

zad3bCompiler = re.compile(pattern3b)
with open('messages.txt', 'r') as atoms:
    for line in atoms:
        if zad3bCompiler.match(line):
            for n in zad3bCompiler.finditer(line):
                # Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18
                print("Niepoprawna nazwa użytkownika: " + n.group(4) + ", połaczenie z " + n.group(5) + " nawiazano " + n.group(2) + " " + moths[n.group(1)] + " o godz. " + n.group(3));
            print(line)
            number3b += 1



