from pickle import FALSE
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
from time import sleep


def registeerimine(kasutajad:list, paroolid:list)->any:
    """ Funktsion tagastab kasutajad ja paroolid
    :param list kasutajad: kasutajade nimed list
    :param list paroolid: kasutajade paroolid list
    :rtype list,list
    """
    while True:
        nimi=input("Mis on sinu ńimi?")
        if nimi not in kasutajad:
            while True:
                parool=input("Mis on sinu parool?")
                flag_p=False,
                flag_l=False,
                flag_u=False,
                flag_d=False
                if len(parool)>=8:
                     parool_list=list(parool)
                     for p in parool_list:
                         if p in punctuation:
                             flag_p=True
                         elif p in ascii_lowercase:
                             flag_l=True
                         elif p in ascii_uppercase:
                             flag_u=True
                         elif p in digits:
                             flag_d=True
                     if flag_p and flag_u and flag_l and flag_d:
                         kasutajad.append(nimi)
                         paroolid.append(parool)
                     break
                else:
                   print("Nõrk salasõna!")
            break
        else:
            print("Selline kasutaja on juba olemas!")

    return kasutajad, paroolid
def autoriseerimine(kasutajad:list, paroolid:list):
    """Funktsioon kuvab ekranile "Tere tulemast!" kui kasutaja on olemas nimekirjas
    nimi on järjendis kasutajad
    Salasõna on paroolide jarendis
    nimi ja salasõna indeksid on võrsed
    :param list kasutajad
    :param list paroolid
    """
    p=0
    while True:
        nimi=input("Sisesta kasutajanimi: ")
        parool=input("Sisesta salasõna: ")
        p+=1
        if nimi in kasutajad and parool in paroolid:
            if kasutajad.index(nimi)==kasutajad.index(parool):
                print(f"Tere tulemast! {nimi}")
            else:
                print("Vale nimi või salasõna!")
                if p==5:
                    print("Proovi uuesti 10 sek pärast")
                    for i in range(10):
                       sleep(10)
                       print(f"On jäänud {10-i} sek")
        else:
            print("Kasutajad pole")