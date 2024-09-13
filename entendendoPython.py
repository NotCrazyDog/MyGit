#texto
print ("Mucho texto mi amigo kkk")


#variáveis
x = "kk"
y = "iae"
z = "man"
print (x,y,z)


#variáveis em uma mesma linha
x, y, z = "kk", "iae", "man"
print (x)
print (y)
print (z)


#array
nomes = ["joão", "maria", "josé"]
x, y, z = nomes
print (x, y, z)


#tipos de variável
x = str(4)
y = int(4)
z = float(4)
print (x, y, z)


#mudando o conteúdo da variável
x = 5
x = "Olá"
x = 5.7
print(x)


#verificar o tipo da variável
x = 5j          #todo número com j no final é um número complexo   
print (type(x))


#variáveis diferentes, mesmo conteúdo
nome = "hugo"
nomeProf = "hugo"
print (nome, nomeProf)


#definindo uma funcao
x = "Teste de função"
def minhaFuncao():  #def serve para definir uma função
    print (x)       #conteúdo da função

minhaFuncao()       #essa linha vai dar um print na função


#variável local e variável global
y = "Gatos"                     #isto é uma variável global(variável fora de uma função; pode ser usada quando quiser)                                  

def funcao():
    y = "Cães"                  #isto é uma variável local(variável dentro de uma função; só pode ser usada dentro da função)
    print ("Eu gosto de " + y)

funcao()

print ("Eu gosto de " + y)


#tranfromando uma variável local em uma varável global
def primeiraFuncao():
    global x                            #global serve para transformar qualquer variável local em variável global; agora ela poderá ser usada por outras funções ou foras delas
    x = "circo"
    print ("hoje eu irei ao " + x)

primeiraFuncao()

def segundaFuncao():
    print ("eu gostei de ir ao " + x)

segundaFuncao()

print ("eu não gosto de ir ao " + x)


#convertendo variáveis numéricas
x = float(5)
y = complex(4.7)
z = int(4)

print (x)
print (y)
print (z)
print (type(x))
print (type(y))
print (type(z))


#fazendo o print mostrar apenas uma letra em uma posição específica
x = "hello man"
print (x[1])    #ele mostrará a letra na posição 1; lebre-se que o primeiro caractere fica na posição 0


#looping de caracteres
for x in "morango":     #vai fazer um looping fazendo print em cada letra da palavra morango
    print (x)


#comprimento de uma string
x = "aaaaaaaaaaaaaaaaaaaaaa"
print (len(x))    #len vai dizer qual o comprimento de uma string, ou seja, vai dizer quantos caracters aquela string contêm


#verficando de palvavras em uma string
x = "eu gosto de pizza"
print ("pizza" in x)    #vai verificar se a palavra pizza existe na string 


#usando um if na verficação dde palavras
x = "eu gosto de você"
if "você" in x:
    print ("a palavra [você] existe nesta string") 


#verificando se uma palavra não existe na string
x = "olá meus amigos kkk"
print ("gato" not in x) #vai verificar se a palavra gato não existe na string


#usando um if na vericação de palavras não existentes
x = "olá meus consagrados"
if "gatos" not in x:
    print ("a palavra [gatos] não existe nesta string")


#dando print em uma parte específica da palavra
x = "danone"
print (x[2:5]) #vai dar um print a partir da letra na 2° posição até a 5° posição; ele não irá da print na 5° letra, apenas usará ela como ponto máximo do print


#print da 1° letra até um ponto determinado da palavra
x = "melancia"
print (x[:6])   #vai da print desde a primeira letra a té a sexta; lembrando que ela não vai dar print na letra de 6° posição, apenas usará ela como o ponto final do print


#print de um ponto determinado até o final da palavra
x = "papagaio"
print (x[3:])   #vai dar um print de um determina do da string até o seu final


#print de um ponto determinado negativo da da palavra
x = "hello world"
print (x[-7:-2])    #vai dar um print de um ponto determinado até outro, mas começando do final da palavra e seguindo até seu inicio


#transformando caracteres minúsculos em caracteres maiúsculos em uma string
x = "porco"
print (x.upper())   #upper vai transformar todos os caracteres minúsculos em caracteres maiúsculos


#transformando caracteres maiúsculos em caracteres minúsculos em uma string
x = "AAA"
print (x.lower())   #lower vai transformar todos os caracteres maiúsculos de uma string em carcteres minúsculos



#removendo o espaço entre as aspas e o conteúdo da string
x = "olá galera              "
print (x.strip())   #strip vai remover todo espaço que tiver entre as aspas e o início e/ou fim de uma string


#trocando as letras de uma string
x = "iguana"
print (x.replace("a", "ooo")) #replace vai substituir uma parte da palavra por outra que você quiser


#transformando uma string em uma lista
#x = "ola,galera"
#y = x.split('','')      #!!!!!deve ser corrigida!!!
#print (y)   



#gerando números aleatórios
import random
print (random.randrange(1,20))      #random.randrange vai escolher um número aleatório de 1 a 20


#variáveis como string
x = "hello"
y = "world"
print (x + " " + y)


#juntando letras e números em uma frase
idade = 25
texto = f"eu tenho {idade} anos"        #f serve para escrever com varável
print (texto)


#fazendo preços em uma string
preco = 30
texto = f"este produto custa {preco:.2f} reais"
print (texto)


#fazendo contas em uma string
texto = f"o preço total fica {40 / 2} reais"
print (texto)


#usando caracters especiais
texto = "eu sou \"Brasileiro\" com muito orgulho"       #o \ permite usar caracteres que não seriam permitidos normalmente em uma string comum
print (texto)


#verificando variáveis verdadeiras ou falsas
