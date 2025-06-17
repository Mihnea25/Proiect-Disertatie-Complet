from sentence_transformers import SentenceTransformer
import joblib

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
classification_model = joblib.load("backend_files/models/svm_model.pkl")

def classify_text(text):
    text_embedding = embedding_model.encode([text])
    prediction = classification_model.predict(text_embedding)

    if prediction[0] == 0:
        return "Textul face parte din categoria Company"
    elif prediction[0] == 1:
        return "Textul face parte din categoria EducationalInstitution"
    elif prediction[0] == 2:
        return "Textul face parte din categoria Artist"
    elif prediction[0] == 3:
        return "Textul face parte din categoria Athlete"
    elif prediction[0] == 4:
        return "Textul face parte din categoria OfficeHolder"
    elif prediction[0] == 5:
        return "Textul face parte din categoria MeanOfTransportation"
    elif prediction[0] == 6:
        return "Textul face parte din categoria Building"
    elif prediction[0] == 7:
        return "Textul face parte din categoria NaturalPlace"
    elif prediction[0] == 8:
        return "Textul face parte din categoria Village"
    elif prediction[0] == 9:
        return "Textul face parte din categoria Animal"
    elif prediction[0] == 10:
        return "Textul face parte din categoria Plant"
    elif prediction[0] == 11:
        return "Textul face parte din categoria Album"
    elif prediction[0] == 12:
        return "Textul face parte din categoria Film"
    elif prediction[0] == 13:
        return "Textul face parte din categoria WrittenWork"
    else:
        return "Labelul prezis nu este valid"
