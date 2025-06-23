import spacy 
from spacy import displacy

nlp = spacy.load("en_core_web_trf")

#functie care afiseaza textul cu displacy, afiseaza o lista de entitati si explica entitatile
def highlight_list_entities(text):
    doc = nlp(text)
    output = ""

    if doc.ents:
        output += "Named Entities found:\n"
        found_labels = set()
        i = 1
        for ent in doc.ents:
            output += f"{i}. {ent.text} ({ent.label_})\n"
            found_labels.add(ent.label_)
            i += 1

        output += "\nEntity label explanations:\n"
        for label in sorted(found_labels):
            explanation = spacy.explain(label)
            output += f"{label}: {explanation}\n"
    else:
        output += "No named entities found."

    return output