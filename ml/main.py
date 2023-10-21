import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from sklearn.model_selection import GridSearchCV

nltk.download("stopwords")
from string import punctuation

russian_stopwords = stopwords.words("russian")

logs = pd.read_csv("unique_logs3.csv", delimiter=";", header=None, names=['log', 'error_type', 'class'])
# all_logs = pd.read_csv("all_logs.csv", delimiter=";", header=None, names=['id', 'data', 'description'])

# Получение текстовой строки из списка слов
def str_corpus(corpus):
    str_corpus = ''
    for i in corpus:
        str_corpus += ' ' + i
    str_corpus = str_corpus.strip()
    return str_corpus


# Получение списка всех слов в корпусе
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


corpus = get_corpus(logs['log'].values)

logs['log'] = logs['log'].map(lambda x: x.lower())
logs['log'] = logs['log'].map(lambda x: remove_punct(x))
logs['log'] = logs['log'].map(lambda x: x.split(' '))
logs['log'] = logs['log'].map(lambda x: [token for token in x if token not in russian_stopwords \
                                         and token != " " \
                                         and token.strip() not in punctuation])
logs['log'] = logs['log'].map(lambda x: ' '.join(x))

X_train, X_valid, y_train, y_valid = train_test_split(logs['log'], logs['class'], test_size=0.1, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

sgd_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('sgd_clf', SGDClassifier(random_state=42))])
knb_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('knb_clf', KNeighborsClassifier(n_neighbors=10))])
sgd_ppl_clf.fit(X_train, y_train)
knb_ppl_clf.fit(X_train, y_train)

predicted_sgd = sgd_ppl_clf.predict(X_test)
# print(metrics.classification_report(predicted_sgd, y_test))
#
# predicted_sgd = knb_ppl_clf.predict(X_test)
# print(metrics.classification_report(predicted_sgd, y_test))

sgd_ppl_clf = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2))),
    ('sgd_clf', SGDClassifier(penalty='elasticnet', class_weight='balanced', random_state=42))])
sgd_ppl_clf.fit(X_train, y_train)
# predicted_sgd = sgd_ppl_clf.predict(X_test)
# print(metrics.classification_report(predicted_sgd, y_test))
# predicted_sgd_val = sgd_ppl_clf.predict(all_logs['description'])
# log_descriptions = all_logs['description']
print(sgd_ppl_clf.predict(["The wait operation timed out"]))

# print(metrics.classification_report(predicted_sgd_val, y_valid))
