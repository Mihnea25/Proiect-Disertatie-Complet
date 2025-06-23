import spacy

nlp = spacy.load("en_core_web_trf")

def highlight_list_entities(text):
    doc = nlp(text)
    output_text = ""
    last_end = 0

    for ent in doc.ents:
        # Text normal până la entitate
        output_text += text[last_end:ent.start_char]
        # Entitate între paranteze drepte + tipul în paranteze rotunde
        output_text += f"[{ent.text} ({ent.label_})]"
        last_end = ent.end_char

    # Adaugă restul textului după ultima entitate
    output_text += text[last_end:]

    return output_text
