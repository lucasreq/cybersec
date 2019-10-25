from collections import OrderedDict

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
crypt = []
message = input('ecrivez votre message').lower
dec = int(input('entrez un nombre décalage'))
i = 0
def chiffrement(x) :
    for i in message: 
        if i in alpha:
            match = alpha.index(i)
            cryp = alpha[match + dec]
            crypt.append(cryp)
            print(crypt)
            return(crypt)
        else:
            print('caractère pas encore traité')

def dechiffrement(message):
# alph="abcdefghijklmnopqrstuvwxyz"
    phrasedecodee=""
    lettre=""
    rang=0
    cle=1

    for i in message:
        for lettre in message:
            if lettre==" ":
                message=message+" "
            else: 
                for k in range(26):
                    if lettre==alpha[k]:
                        rang=[k]
                phrasedecodee=phrasedecodee+alpha[(rang+cle)%26]
                print(message)   
                cle=cle+1

def exercice3(): 
    x= 0
    txt = "Bi mid kissj anild jils btvvtzlwdtep tm uadceuadtzp t zam applse jil utme ase pdtww rseades Jil bi mid seawwj lmbespdamb piuedctmr lmwepp jil zam egqwatm td di jils rsambuidces Eblzadtim tp kcad seuatmp avdes ime cap visriddem kcad ime cap weasmeb tm pzciiw Tmpamtdj tp bitmr dce paue dctmr ifes amb ifes aratm amb egqezdtmr btvvesemd seplwdp Kcad a pab esa kcem td tp eaptes di puapc am adiu dcam a qsexlbtze Dce pezsed iv zseadtftdj tp ymiktmr cik di ctbe jils pilszep Dsj mid di neziue a uam iv plzzepp nld sadces di neziue a uam iv fawle Ziuuim pempe tp dce ziwwezdtim iv qsexlbtzep azoltseb nj are etrcdeem".lower()
	
    ca = txt.count('a')
    cb = txt.count('b')
    cc = txt.count('c')
    cd = txt.count('d')
    ce = txt.count('e')
    cf = txt.count('f')
    cg = txt.count('g')
    ch = txt.count('h')
    ci = txt.count('i')
    cj = txt.count('j')
    ck = txt.count('k')
    cl = txt.count('l')
    cm = txt.count('m')
    cn = txt.count('n')
    co = txt.count('o')
    cp = txt.count('p')
    cq = txt.count('q')
    cr = txt.count('r')
    cs = txt.count('s')
    ct = txt.count('t')
    cu = txt.count('u')
    cv = txt.count('v')
    cw = txt.count('w')
    cx = txt.count('x')
    cy = txt.count('y')
    cz = txt.count('z')

    nb_let = ca+cb+cc+cd+ce+cf+cg+ch+ci+cj+ck+cl+cm+cn+co+cp+cq+cr+cs+ct+cu+cv+cw+cx+cy+cz
    classif = [(ca/nb_let)*100,(cb/nb_let)*100,(cc/nb_let)*100,(cd/nb_let)*100,(ce/nb_let)*100,(cf/nb_let)*100,(cg/nb_let)*100,(ch/nb_let)*100,(ci/nb_let)*100,(cj/nb_let)*100,(ck/nb_let)*100,(cl/nb_let)*100,(cm/nb_let)*100,(cn/nb_let)*100,(co/nb_let)*100,(cp/nb_let)*100,(cq/nb_let)*100,(cr/nb_let)*100,(cs/nb_let)*100,(ct/nb_let)*100,(cu/nb_let)*100,(cv/nb_let)*100,(cw/nb_let)*100,(cx/nb_let)*100,(cy/nb_let)*100,(cz/nb_let)*100]
    classifre = {'a' : 8.12,'b' : 1.49,'c' : 2.71,'d' : 4.32,'e' : 12.02,'f' : 2.30, 'g' : 2.03 , 'h' : 5.92, 'i' : 7.31, 'j' : 0.10,'k' : 0.69,'l' : 3.98, 'm' : 2.61,'n' : 6.95, 'o' : 7.68,'p' : 1.82,'q' : 0.11,'r' : 6.02,'s' : 6.28,'t' : 9.10,'u' : 2.88,'v' : 1.11,'w' : 2.09,'x' : 0.17,'y' : 2.11,'z' : 0.07}
    rclassif = []
    d = OrderedDict(sorted(classifre.keys(), key=lambda t: t[0]))
    l = sorted(classif)
    for i in classif:
        rclassif.append(round(i,2))

    print (d)
    




	




exercice3()

