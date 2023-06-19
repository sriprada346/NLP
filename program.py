#Empty lists
from io import StringIO

def nlp_fun(x,buffer):
    pronoun_lst=[]
    adjuctive_lst=[]
    adverb_lst=[]
    verb_lst=[]
    interjection_lst=[]
    conjunction_lst=[]
    preposition_list=[]
    noun_list=[]

    pronoun_file=open(r'static/txtfiles/pronouns.txt','r')
    pronouns=pronoun_file.read()

    adjective_file=open(r'static/txtfiles/adjectives.txt','r')
    adjectives=adjective_file.read()

    verb_file=open(r'static/txtfiles/verbs.txt', 'r')
    verbs=verb_file.read()

    conjunction_file=open(r'static/txtfiles/conjunctions.txt','r')
    conjunctions=conjunction_file.read().replace(","," ")

    interjection_file=open(r'static/txtfiles/interjection.txt','r')
    interjection=interjection_file.read()

    adverb_file=open(r'static/txtfiles/adverb.txt','r')
    adverbs=adverb_file.read()

    preposition_file=open(r'static/txtfiles/prepositions.txt','r')
    prepositions=preposition_file.read()


    sentence=x.replace(","," ")
    sentence=sentence.replace(".","")
    sentence=sentence.lower()
    for i in sentence.split():
        if i in pronouns.split():
            if i not in pronoun_lst:
                pronoun_lst+=[i]

        elif i in adjectives.split():
            if i not in adjuctive_lst:
                adjuctive_lst+=[i]
        elif i in adverbs.split():
            if i not in adverb_lst:
                adverb_lst+=[i]
        elif i in verbs.split():
            if i not in verb_lst:
                verb_lst+=[i]
        elif i in conjunctions.split():
            if i not in conjunction_lst:
                conjunction_lst+=[i]
        elif i in interjection.split():
            if i not in interjection_lst:
                interjection_lst+=[i]
        elif i in prepositions.split():
            if i not in preposition_list:
                preposition_list+=[i]
        else:
            noun_list+=[i]


    
    buffer.write("Pronouns:" + ', '.join(pronoun_lst) + "\n")
    buffer.write("adjectives:" + ', '.join(adjuctive_lst) + "\n")
    buffer.write("adverbs:" + ', '.join(adverb_lst) + "\n")
    buffer.write("verbs:" + ', '.join(verb_lst) + "\n")
    buffer.write("conjunctions:" + ', '.join(conjunction_lst) + "\n")
    buffer.write("interjections:" + ', '.join(interjection_lst) + "\n")
    buffer.write("Prepositions:" + ', '.join(preposition_list) + "\n")
    buffer.write('Nouns:' + ', '.join(noun_list) + "\n")
    
    '''
    buffer.write("<span class='pronouns'>Pronouns:</span>" + ', '.join(pronoun_lst) + "\n")
    buffer.write("<span class='adjectives'>adjectives:</span>" + ', '.join(adjuctive_lst) + "\n")
    buffer.write("<span class='adverbs'>adverbs:</span>" + ', '.join(adverb_lst) + "\n")
    buffer.write("<span class='verbs'>verbs:</span>" + ', '.join(verb_lst) + "\n")
    buffer.write("<span class='conjunctions'>conjunctions:</span>" + ', '.join(conjunction_lst) + "\n")
    buffer.write("<span class='interjections'>interjections:</span>" + ', '.join(interjection_lst) + "\n")
    buffer.write("<span class='prepositions'>Prepositions:</span>" + ', '.join(preposition_list) + "\n")
    buffer.write("<span class='nouns'>Nouns:</span>" + ', '.join(noun_list) + "\n")
    '''

    adverb_file.close()
    interjection_file.close()
    conjunction_file.close()
    verb_file.close()
    adjective_file.close()
    pronoun_file.close()
    preposition_file.close()

    return buffer.getvalue()

