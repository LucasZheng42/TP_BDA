
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

def print_dependencies(dependencies) :
    txt = ''
    for inout in dependencies :
        txt += ','.join(list(inout[0]))
        txt += ' -> '
        txt += ','.join(list(inout[1]))+"; \n"
    print(txt)

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

def is_SuperCle(relation,cle,dependencies):
    resultat = fermeture_cloture(cle,dependencies)

    return resultat == relation
def is_CleCandidate(relation,cle,dependencies ): 
    sous_cles = subsets(cle)
    if not is_SuperCle(relation,cle,dependencies):
        return False
    
    for sous_cle_possible in sous_cles : 
        if(is_SuperCle(relation,sous_cle_possible,dependencies)):
            return False     
    return True

def cles_candidates(relation,dependencies):
    cles_candidates = []
    sous_ensembles = subsets(list(relation))
    for sous_ensemble in sous_ensembles :
        if(is_CleCandidate(relation,sous_ensemble,dependencies)):
           cles_candidates.append(set(sous_ensemble))
    return cles_candidates

if __name__ == '__main__':
    print_dependencies(mydependencies)

    print(fermeture_cloture('A',mydependencies))
    print(fermeture_cloture_toute(mydependencies))

    print(is_AlphaDetermineBeta('A','B',mydependencies))
    print(is_AlphaDetermineBeta('H','A',mydependencies))

    print(is_SuperCle(myrelations[0],["A","G"],mydependencies))
    print(is_SuperCle(myrelations[0],["A"],mydependencies))

    print(cles_candidates(myrelations[0],mydependencies))
