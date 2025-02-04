from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


def transformers_get_similarity(word, text, model_name="sentence-transformers/all-MiniLM-L6-v2"):
    # Загружаем модель
    model = SentenceTransformer(model_name)

    # Кодируем вектора
    text_embedding = model.encode(text).reshape(1, -1)
    word_embedding = model.encode(word).reshape(1, -1)

    # Вычисляем косинусное сходство
    similarity = cosine_similarity(text_embedding, word_embedding)[0][0]

    return similarity

