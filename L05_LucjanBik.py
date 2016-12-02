import re



# zad2

# RUN [[NUMER Z DOKŁADNIE 6 CYFR]] COMPLETED. OUTPUT IN FILE [[NAZWA]].dat. [[COKOLWIEK]]
pattern = "^RUN \d{6} COMPLETED$"

result2 = []
zad2Compiler = re.compile("^RUN \d{6} COMPLETED\. OUTPUT IN FILE [a-z]+\.dat\.$")
with open('atoms.log', 'r') as atoms:
    for line in atoms:
        if zad2Compiler.match(line):
            # print(line)
            result2.append(line)

print("zad 2: " + str(len(result2)) + " dopasowanych lini")


# zad3a
pattern = ".*Invalid user.*"
zad3aCompiler = re.compile(".*Invalid user.*")


result3a = []
with open('messages.txt', 'r') as atoms:
    for line in atoms:
        if zad3aCompiler.match(line):
            # print(line)
            result3a.append(line)

print("zad 3a: " + str(len(result3a)) + " dopasowanych lini")

# zad3b
# Jun 29 20:18:40 noether sshd[5805]: Invalid user tester from 218.189.194.200
# Niepoprawna nazwa użytkownika: "tester", połaczenie z 218.189.194.200 nawiązano 29 czerwca o godz. 20:18

pattern3b = "(\w{3}) ( \d|\d\d) (\d\d:\d\d):\d\d .* Invalid user (\w+) from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
moths = {'Jan': 'stycznia', 'Feb':'lutego', 'Mar' : 'Marca', 'Apr':'kwietnia',
         'May':'maja', 'Jun': 'czerwca', 'Jul':'lipca', 'Aug':'sierpnia',
         'Sep':'wrzesnia', 'Oct':'pazdziernika', 'Nov':'listopada', 'Dec':'grudnia'}

result3b = []
zad3bCompiler = re.compile(pattern3b)
with open('messages.txt', 'r') as atoms:
    for line in atoms:
        if zad3bCompiler.match(line):
            for n in zad3bCompiler.finditer(line):
                proceedLine = "Niepoprawna nazwa użytkownika: " + n.group(4) + ", połaczenie z " + n.group(
                    5) + " nawiazano " + n.group(2) + " " + moths[n.group(1)] + " o godz. " + n.group(3)
                result3b.append(proceedLine)
                # print(proceedLine);
print("zad 3b : " + str(len(result3b)) + " dopasowanych lini");


# zad5


def validate(email):
    # match=re.search("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-Z0-9.]*\.{1}[com|org|edu]{3}$)",email)
    # match=re.search("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$",email)
    match=re.search(r"(^[a-zA-Z0-9;_.#!$%&'*+-]+@[a-zA-Z0-9-]+\.[a-z]{2,3}$)",email)
    if match:
        return True
    else:
        return False


# valid emails
print("valid emails tests:")
print(validate("prettyandsimple@example.com") == True)
print(validate("very.common@example.com") == True)
print(validate("disposable.style.email.with+symbol@example.com") == True)
print(validate("other.email-with-dash@example.com") == True)
print(validate("x@example.com") == True)


# Invalid emails
print("invalid emails tests:")
print(validate("Abc.example.com") == False)
print(validate("A@b@c@example.com") == False)
print(validate("not right@example.com") == False)
print(validate("not\allowed@example.com") == False)
print(validate("this\ still\"not\\allowed@example.com") == False)
print(validate("john.doe@example..com") == False)


