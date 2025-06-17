import spacy 
from spacy import displacy


#functie care afiseaza textul cu displacy, afiseaza o lista de entitati si explica entitatile
def highlight_list_entities(text):

    doc = nlp(text)

    displacy.render(doc, style="ent", jupyter=True)

    #verifica daca exista entitati
    if doc.ents:
        print("\nNamed Entities found:")
        found_labels = set()
        i = 1
        #afiseaza textul cu entitatea corespunzatoare si adauga labelul in lista
        for ent in doc.ents:
            print(f"{i}.{ent.text} ({ent.label_})")
            found_labels.add(ent.label_)
            i+=1

        #explica doar entitatile din lista
        print("\nEntity label explanations:")
        for label in sorted(found_labels):
            explanation = spacy.explain(label)
            print(f"{label}: {explanation}")
    else:
        print("No named entities found.")