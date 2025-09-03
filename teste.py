
y = True
gen = []
sex = []
fut = []
br = []
contXS = contXN = contYN = contYS = contZN = contZS = contFS = contFN = contMS = contMN = contFuSS = contFuSN = contFuNS = contFuNN = 0

while y:

    g = input('Qual a geração (X/Y/Z): ').upper()
    gen.append(g)

    s = input('Qual o sexo (F - M): ').upper()
    sex.append(s)

    f = input('Pratica/praticou futbol (S/N): ').upper()
    fut.append(f)

    b = input('Brasil vai ganhar (S/N): ').upper()
    br.append(b)

    x = input('Deseja preencher novamente o formulario (S/N): ').upper()
    if x == 'N':
       y = False

for i in range (len(gen)):

    if gen[i] == 'X' and br[i] == 'S':
        contXS += 1

    elif gen[i] == 'X' and br[i] == 'N':
        contXN += 1

    elif gen[i] == 'Y' and br[i] == 'S':
        contYS +=1 

    elif gen[i] == 'Y' and br[i] == 'N':
        contYN +=1 

    elif gen[i] == 'Z' and br[i] == 'S':
        contZS +=1 

    elif gen[i] == 'Z' and br[i] == 'N':
        contZN +=1 

    if sex[i] == 'F' and br[i] =='S':
        contFS +=1 

    elif sex[i] == 'F' and br[i] =='N':
        contFN +=1      

    elif sex[i] == 'M' and br[i] =='S':
        contMS +=1 

    elif sex[i] == 'M' and br[i] =='N':
        contMN +=1      

    if fut[i] == 'S' and br[i] =='S':
        contFuSS +=1 

    elif fut[i] == 'S' and br[i] =='N':
        contFuSN +=1 

    elif fut[i] == 'N' and br[i] =='S':
        contFuNS +=1 

    elif fut[i] == 'N' and br[i] =='N':
        contFuNN +=1 


print(f'Geração X: {(contXS/(contXS + contXN))*100}% ganhar, {(contXN/(contXS + contXN))*100}% perder!t sta')
print(f'Geração Y: {(contYS/(contYS + contYN))*100}% ganhar, {(contYN/(contYS + contYN))*100}% perder!')
print(f'Geração Z: {(contZS/(contZS + contZN))*100}% ganhar, {(contZN/(contZS + contZN))*100}% perder!')

print(f'Feminino: {(contFS/(contFS + contFN))*100}% ganhar, {(contFN/(contFS + contFN))*100}% perder!')
print(f'Masculino: {(contMS/(contMS + contMN))*100}% ganhar, {(contMN/(contMS + contMN))*100}% perder!') 

print(f'Pratica futbol: {(contFuSS/(contFuSS + contFuSN))*100}% ganhar, {(contFuSN/(contFuSS + contFuSN))*100}% perder!')
print(f'Não pratica futbol: {(contFuNS/(contFuNS + contFuNN))*100}% ganhar, {(contFuNN/(contFuNS + contFuNN))*100}% perder!')