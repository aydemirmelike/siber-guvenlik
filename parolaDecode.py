import base64
parolaDosya=open("parola.txt","r")
parola=parolaDosya.readline()
parolaDosya.close()
print parola
print base64.b64decode(parola)