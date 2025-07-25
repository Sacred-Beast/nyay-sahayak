import spacy
import re

nlp = spacy.load("en_core_web_lg")

def mine_arguments(text):
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

    # Rule-based: Claims = sentences with modal verbs or assertive phrases
    # Premises = sentences with "because", "since", "as", etc.
    claims, premises = [], []
    for sent in doc.sents:
        s = sent.text.strip()
        if re.search(r"\b(shall|must|should|is entitled|claims?|alleges?|asserts?)\b", s, re.I):
            claims.append(s)
        elif re.search(r"\b(because|since|as|due to|for the reason)\b", s, re.I):
            premises.append(s)
    return entities, claims, premises
