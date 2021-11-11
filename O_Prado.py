#2.1.1

#Construtor
def cria_posicao(x,y):
    if x < 0 or y < 0:
        raise ValueError('cria_posicao: argumentos invalidos')
    return (x,y)

def cria_copia_posicao(p):
    nova_posicao = (obter_pos_x(p),obter_pos_y(p))
    return nova_posicao

#Seletores
def obter_pos_x(posicao):
    return posicao[0]

def obter_pos_y(posicao):
    return posicao[1]

#Reconhecedores

def eh_posicao(arg):
    return type(arg) == tuple and len(arg) == 2 and type(arg[0]) == int and type(arg[1]) == int \
        and arg[0] >= 0 and arg[1] >= 0

#Teste

def posicoes_iguais(p1,p2):
    return p1 == p2

#Transformador
def posicao_para_str(p):
    return str(p)


#Funcoes alto nivel

def obter_posicoes_adjacentes(p):
    if p[0] - 1 > 0 and p[1] - 1 > 0:
        return ((p[0],p[1]-1),(p[0]+1,p[1]),(p[0],p[1]+1),(p[0]-1,p[1]))
    elif p[0] - 1 < 0:
        return ((p[0], p[1] - 1), (p[0] + 1, p[1]), (p[0], p[1] + 1))
    elif p[1] - 1 < 0:
        return ((p[0] + 1, p[1]), (p[0], p[1] + 1), (p[0] - 1, p[1]))


def ordenar_posicoes(t):
    novo_tuplo = ()
    for tuplo in t: #excluir tuplos com numeros negativos
        if eh_posicao(tuplo):
            novo_tuplo += (tuplo,)
    return sorted(novo_tuplo,key=lambda x : (x[1],x[0]))


#2.1.2
#Construtores
def cria_animal(s,r,a):
    if not(type(s) == str and len(s) != 0) or not(type(r) == int and r > 0) or not(type(a) == int and a >= 0 ):
        raise ValueError('cria_animal: argumentos invalidos')
    idade = 0
    fome = 0
    return [s,[idade,r],[fome,a]]

def cria_copia_animal(animal):
    copia_animal = [animal[0],[animal[1][0],animal[1][1]],[animal[2][0],animal[2][1]]]
    return copia_animal

#Seletores

def obter_especie(animal):
    return animal[0]

def obter_freq_reproducao(animal):
    return animal[1][1]

def obter_freq_alimentacao(animal):
    return animal[2][1]

def obter_idade(animal):
    return animal[1][0]

def obter_fome(animal):
    return animal[2][0]

#Modificadores

def aumenta_idade(animal):
    animal_atualizado = cria_copia_animal(animal)
    animal_atualizado[1][0] += 1
    return animal_atualizado

def reset_idade(animal):
    animal_atualizado = cria_copia_animal(animal)
    animal_atualizado[1][0] = 0
    return animal_atualizado

def aumenta_fome(animal):
    animal_atualizado = cria_copia_animal(animal)
    animal_atualizado[2][0] += 1
    return animal_atualizado

def reset_fome(animal):
    animal_atualizado = cria_copia_animal(animal)
    animal_atualizado[2][0] = 0
    return animal_atualizado

#Reconhecedor

def eh_animal(arg):
    if type(arg) == list and len(arg) == 3:
        if type(arg[0]) == str and arg[0] != '':
            if type(arg[1]) == list and len(arg[1]) == 2 and type(arg[1][0]) == int and type(arg[1][1]) == int and arg[1][0] >= 0 and arg[1][1] > 0:
                if type(arg[2]) == list and len(arg[2]) == 2 and type(arg[2][0]) == int and type(arg[2][1]) == int and arg[2][0] >= 0 and arg[2][1] >= 0:
                    return True
    return False


def eh_predador(arg):
    if eh_animal(arg) and arg[2][1] != 0:
        return True
    return False

def eh_presa(arg):
    if eh_animal(arg) and arg[2][1] != 0:
        return False
    return True


#Testes

def animais_iguais(a1,a2):
    return obter_especie(a1) == obter_especie(a2) and obter_freq_reproducao(a1) == obter_freq_reproducao(a2) and obter_idade(a1) == obter_idade(a2) \
        and obter_freq_alimentacao(a1) == obter_freq_alimentacao(a2) and obter_fome(a1) == obter_fome(a2)

#Transformadores

def animal_para_char(a):
    if eh_presa(a):
        return str(list(a[0])[0]).lower()
    else:
        return str(list(a[0])[0]).upper()

def animal_para_str(a):
    if eh_predador(a):
        string = '%s [%d/%d;%d/%d]' %(a[0],a[1][0],a[1][1],a[2][0],a[2][1])
    elif eh_presa(a):
        string = '%s [%d/%d]' %(a[0],a[1][0],a[1][1])
    return string


#Funcoes de Alto nivel


def eh_animal_fertil(a):
    return obter_freq_reproducao(a) <= obter_idade(a)

def eh_animal_faminto(a):
    return obter_freq_alimentacao(a) <= obter_fome(a)

def reproduz_animal(a):
    a = reset_idade(a)
    if eh_predador(a):
        cria = reset_idade(a)
        cria = reset_fome(cria)
    else:
        cria = reset_idade(a)
    return cria


#2.1.3
#Construtor

def cria_prado(d,r,a,p):
    if type(r) == tuple and (r == () or all(True for x in r if d[0] > x[0] > 0 and d[1] > x[1] > 0)): #Verifica se esta dentro das montanhas
        if type(a) == tuple and len(a) >= 1 and all(True for x in a if eh_animal(x)): #verifica se todos sao animais
            if type(p) == tuple and len(a) == len(p) and all(True for x in p if d[0] > x[0] > 0 and d[1] > x[1] > 0): #verififca se esta dentro das montanhas
                if len(a) + len(r) > ((d[0]-2) * (d[1]-2)): #verifica se ocupam mais espaco do que ha
                    raise ValueError('criar_prado: argumentos invalidos')
                else:
                    prado = {'montanhas' : [],'rochas' : [], 'animal': []}
                    for y in range(d[1]+1):
                        if y != 0 or y != d[1]:
                            prado['montanhas'].append((0, y),)
                            prado['montanhas'].append((d[0], y),)
                        if y == 0 or y == d[1]:
                            for x in range(d[0] + 1):
                                prado['montanhas'].append((x,y),)
                    for tuplo in prado['montanhas']:
                        if prado['montanhas'].count(tuplo) > 1:
                            prado['montanhas'].remove(tuplo)

                    for tuplo in r:
                        prado['rochas'].append(tuplo)

                    for i in range(len(a)):
                        prado['animal'].append([a[i],p[i]])

                    return prado
    else:
        raise ValueError('criar_prado: argumentos invalidos')


def cria_copia_prado(m):
    return {'montanhas':m['montanhas'],'rochas':m['rochas'],'animal':m['animal']}

#Seletores
def obter_tamanho_x(m):
    return m['montanhas'][len(m['montanhas'])-1][0]+1

def obter_tamanho_y(m):
    return m['montanhas'][len(m['montanhas'])-1][1]+1

def obter_numero_predadores(m):
    count = 0
    for animal in m[2]:
        if animal[2][1] != 0:
            count += 1
    return count

def obter_numero_presas(m):
    count = 0
    for animal in m[2]:
        if animal[2][1] == 0:
            count += 1
    return count

def obter_posicao_animais(m):
    return sorted(m[3],key=lambda x : (x[0],x[1]))


def obter_animal(m,p):
    for animal in m['animal']:
        if animal[1] == p:
            return animal[0]
#Modificadores

def eliminar_animal(m,p):
    m1 = cria_copia_prado(m)
    for animais in range(len(m1['animal'])):
        if p == m1['animal'][animais][1]:
            m1['animal'].remove(m1['animal'][animais])
            return m1
    return m1

def mover_animal(m,p1,p2):
    m1 = cria_copia_prado(m)
    for animais in m1['animal']:
        if p1 == animais[1]:
            animais[1] = p2
            return m1
    return m1

def inserir_animal(m, a, p):
    m1 = cria_copia_prado(m)
    m1['animal'].append((a,p))
    return m1

#Reconhecedores

def eh_prado(arg):
    if type(arg) == dict and len(arg) == 3:
        if arg.keys() == ['montanhas','rochas','animal']:
            if type(arg['montanhas']) == list and type(arg['rochas']) == list and type(arg['animal']) == list:
                if len(arg['montanhas']) >= 8 and len(arg['rochas']) + len(arg['animal']) <= obter_tamanho_y(arg) * obter_tamanho_x(arg):
                    return True
    return False

def eh_posicao_animal(m,p):
    for animal in m['animal']:
        if animal[1] == p:
            return True

def eh_posicao_obstaculo(m,p):
    return p in m['montanhas'] or p in m['rochas']

def eh_posicao_livre(m, p):
    for animal in m['animal']:
        if p == animal[1] or p in m['montanhas'] or p in m['rochas']:
            return False
    return True
#Teste

def prado_iguais(p1,p2):
    return p1 == p2

#Transformador

def prado_para_str(m):
    lista = []
    string = ''
    for i2 in range(m['montanhas'][len(m['montanhas']) - 1][1] + 1):
        for i in range(m['montanhas'][len(m['montanhas'])-1][0]+1):
            lista.append((i,i2))
    for posicao in range(len(lista)):
        if eh_posicao_livre(m,lista[posicao]):
            string += '.'
        elif eh_posicao_animal(m,lista[posicao]):
            if eh_predador(obter_animal(m,lista[posicao])):
                string += animal_para_char(obter_animal(m,lista[posicao])).upper()
            else:
                string += animal_para_char(obter_animal(m, lista[posicao])).lower()
        elif lista[posicao] == (0,0) or lista[posicao] == (0,obter_tamanho_y(m)-1) or lista[posicao] == (obter_tamanho_x(m)-1,0)\
            or lista[posicao] == (obter_tamanho_x(m)-1,obter_tamanho_y(m)-1):
            string += '+'
        elif (lista[posicao][0] == obter_tamanho_x(m)-1 or lista[posicao][0] == 0) and lista[posicao][1] != lista[posicao][0]:
            string += '|'
        elif lista[posicao] in m['montanhas']:
            string += '-'
        elif eh_posicao_obstaculo(m,lista[posicao]) and lista[posicao] not in m['montanhas']:
            string += '@'
        if posicao < len((lista))-1:
            if lista[posicao][1] != lista[posicao+1][1]:
                string += '\n'
    return string

dim = cria_posicao(11, 4)
obs = (cria_posicao(4, 2), cria_posicao(5, 2))
an1 = tuple(cria_animal('rabbit', 5, 0) for i in range(3))
an2 = (cria_animal('lynx', 20, 15),)
pos = tuple(cria_posicao(p[0], p[1]) for p in ((5, 1), (7, 2), (10, 1), (6, 1)))
prado = cria_prado(dim, obs, an1 + an2, pos)
print(prado)
print(prado_para_str(prado))
#Funcoes de alto nivel
def obter_valor_numerico(m,p):
    return p[0] + (obter_tamanho_x(m) * p[1])

def obter_movimento(m,p):
    if eh_posicao_animal(p):
        if eh_predador(obter_animal(m,p)):
            if not obter_posicoes_adjacentes(p):
                return p
            for posicao in obter_posicoes_adjacentes(p):
                if eh_posicao_animal(m,posicao) and eh_presa(obter_animal(m,posicao)):
                    return posicao
        if eh_presa(obter_animal(m, p)):
            if not obter_posicoes_adjacentes(p):
                return p
            for posicao in obter_posicoes_adjacentes(p):
                if eh_posicao_livre(m,posicao):
                    return posicao



