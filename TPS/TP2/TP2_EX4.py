myrelations =[
    { 'A' , 'B' , 'C' , 'G' , 'H' , 'I'} ,{ 'X' , 'Y'}
]

mydependencies = [
    [ {'A'},{'B'} ],
    [ {'A'},{'C'} ],
    [ {'C','G'},{'H'} ],
    [ {'C','G'},{'I'} ],
    [{'B'},{'H'} ],
]
def subsets(arr):
    n = len(arr)
    res = []
    
    # Loop through all possible 
    # subsets using bit manipulation
    for i in range(1 << n):
        subset = []

        # Loop through all elements 
        # of the input array
        for j in range(n):

            # Check if the jth bit is 
            # set in the current subset
            if (i & (1 << j)) != 0:

                # If the jth bit is set, add 
                # the jth element to the subset
                subset.append(arr[j])
        
        # Push the subset into result
        res.append(subset)
    
    return res

def print_dependencies(dependencies) :
    txt = ''
    for dependency in dependencies :
        txt += ','.join(list(dependency[0]))
        txt += ' -> '
        txt += ','.join(list(dependency[1]))+"; \n"
    print(txt)

def max_alpha_len(dependencies):
    max_len = 1
    for dependency in dependencies :
        if len(dependency[0]) > max_len : 
            max_len = len(dependency[0])
    return max_len

def fermeture_cloture(letters,dependencies):
    result = set(letters)
    loop = 0
    max_loop = max_alpha_len(dependencies)
    while loop < max_loop : 
        for dependency in dependencies :
            if dependency[0].issubset(result):
                result.update(dependency[1])
             
        loop+=1

    return result

def fermeture_cloture_toute(dependencies):
    result_F=set()
    lettres_initiales = set()
    for dependency in dependencies : 
        lettres_initiales.update(dependency[0])
        
    result_F.update(fermeture_cloture(lettres_initiales,mydependencies))
        
    return result_F

def is_AlphaDetermineBeta(Alpha,Beta,dependencies):

    AlphaPlus=fermeture_cloture(Alpha,dependencies)
    return Beta in AlphaPlus
#7
def is_SuperCle(relation,cle,dependencies):
    resultat = fermeture_cloture(cle,dependencies)

    return resultat == relation
#8
def is_CleCandidate(relation,cle,dependencies ): 
    sous_cles = subsets(cle)
    if not is_SuperCle(relation,cle,dependencies):
        return False
    
    for sous_cle_possible in sous_cles : 
        if(is_SuperCle(relation,sous_cle_possible,dependencies)):
            return False     
    return True
#9
def cles_candidates(relation,dependencies):
    cles_candidates = []
    toutes_relations = subsets(list(relation))
    for dependency in dependencies :
        for cle_possible in toutes_relations : 
            if(is_CleCandidate(relation,list(cle_possible),dependencies)):
                cles_candidates.append(list(cle_possible))
    return cles_candidates

#10
def super_cles(relation,dependencies):
    super_cles = []
    toutes_relations = subsets(list(relation))
    for dependency in dependencies : 
        for cle_possible in toutes_relations : 
            if(is_SuperCle(relation,list(cle_possible),dependencies)):
                super_cles.append(list(cle_possible))
    return super_cles
"""
    En absence de solutions trouvées par soi-même, j'ai pris les corrigées.
"""
#11
def computeOneCandidateKey ( F , R):
    K = set (R)
    while not is_CleCandidate (F , R , K ):
        for A in K:
            if is_SuperCle ( F , R , K. difference ({ A }) ):
                K.remove (A)
            break
    return K

#12
def isBCNFRelation (F, R):
    for K in subsets (R) :
        K_plus = fermeture_cloture (F , K)
        Y = K_plus . difference (K )
        if not R . issubset ( K_plus ) and not Y. isdisjoint (R):
            return False , [ K , Y & R ]
    return True , [ {} , {} ]

#13
def isBCNFRelations (F, T):
    for R in T:
        if isBCNFRelation (F , R ) == False :
            return False , R
    return True , {}
#14
def computeBCNFDecomposition (F, T):
    OUT , size = list (T) , 0
    while size != len ( OUT ):
        size = len ( OUT )
        for R in OUT :
            _isR_BCNF , [ alpha , beta ] = isBCNFRelation (F , R )
            if _isR_BCNF == False :
                if alpha | beta not in OUT :
                    OUT . append ( alpha | beta )
                if R. difference ( beta ) not in OUT :
                    OUT . append ( R. difference ( beta ) )
                OUT . remove (R)
                break

    return OUT

if __name__ == '__main__':

    print_dependencies(mydependencies)

    print(fermeture_cloture('A',mydependencies))
    print(fermeture_cloture_toute(mydependencies))

    print("A -> B ? ",is_AlphaDetermineBeta('A','B',mydependencies))
    print("H -> A ? ",is_AlphaDetermineBeta('H','A',mydependencies))

    print("A G est une super clé ? ",is_SuperCle(myrelations[0],["A","G"],mydependencies))
    print("A est une super clé ? ",is_SuperCle(myrelations[0],["A"],mydependencies))

    print("Les clés candidates sont : ", cles_candidates(myrelations[0],mydependencies))

    print("Les super clés sont : ", super_cles(myrelations[0],mydependencies))
