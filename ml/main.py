import pandas as pd
from string import punctuation
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline


def get_corpus(data):
    corpus = []
    for phrase in data:
        for word in phrase.split():
            corpus.append(word)
    return corpus


def remove_punct(text):
    table = {33: ' ', 34: ' ', 35: ' ', 36: ' ', 37: ' ', 38: ' ', 39: ' ', 40: ' ', 41: ' ', 42: ' ', 43: ' ', 44: ' ',
             45: ' ', 46: ' ', 47: ' ', 58: ' ', 59: ' ', 60: ' ', 61: ' ', 62: ' ', 63: ' ', 64: ' ', 91: ' ', 92: ' ',
             93: ' ', 94: ' ', 95: ' ', 96: ' ', 123: ' ', 124: ' ', 125: ' ', 126: ' '}
    return text.translate(table)


russian_stopwords = stopwords.words("russian")
logs = pd.read_csv("unique_logs_splitted.csv", delimiter=";", header=None, names=['log', 'error_type', 'key_words'])
all_logs = pd.read_csv("all_logs.csv", delimiter=";", header=None, names=['id', 'time', 'log'])
corpus = get_corpus(logs['log'].values)

logs['log'] = logs['log'].map(lambda x: x.lower())
logs['log'] = logs['log'].map(lambda x: remove_punct(x))
logs['log'] = logs['log'].map(lambda x: x.split(' '))
logs['log'] = logs['log'].map(lambda x: [token for token in x if token not in russian_stopwords \
                                         and token != " " \
                                         and token.strip() not in punctuation])
logs['log'] = logs['log'].map(lambda x: ' '.join(x))

sgd_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
    ('sgd_clf', SGDClassifier(penalty='elasticnet', class_weight='balanced', random_state=42))])
sgd_ppl_clf.fit(logs['log'], logs['error_type'])

got_error = input(">> ")
error_type = sgd_ppl_clf.predict([got_error])

print(f"Полученная ошибка: {got_error}")
print(f"Тип: {error_type}")
