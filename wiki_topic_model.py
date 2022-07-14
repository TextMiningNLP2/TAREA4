#Importamos librerias
import os
import random
import codecs
import pickle
from gensim.models.ldamodel import LdaModel as Lda
from gensim import corpora
from nltk.corpus import stopwords 
from nltk.stem.wordnet import WordNetLemmatizer


#Función para eliminar stop words y lematizar verbos
def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
    normalized = " ".join(lemma.lemmatize(word,'v') for word in stop_free.split())
    x = normalized.split()
    y = [s for s in x if len(s) > 2]
    return y

corpus_path = "articles-corpus/"
article_paths = [os.path.join(corpus_path,p) for p in os.listdir(corpus_path)]

#Leer el contenido de todos los artículos en un lista doc_complete
doc_complete = []
for path in article_paths:
    fp = codecs.open(path,'r','utf-8')
    doc_content = fp.read()
    doc_complete.append(doc_content)  

#Obtener una muestra aleatoria de 10000 artículos 
docs_all = random.sample(doc_complete, 10000)
docs = open("docs_wiki.pkl",'wb')
pickle.dump(docs_all,docs)

#Utilizar 60000 artículos para entrenar el modelo
docs_train = docs_all[:60000]

#Eliminando stop word de la muestra obtenida
stop = set(stopwords.words('english'))
lemma = WordNetLemmatizer()
doc_clean = [clean(doc) for doc in docs_train]

#Creación de diccionario
dictionary = corpora.Dictionary(doc_clean)

# Filtrar los términos que han ocurrido en menos de 3 artículos y más del 40% de los mismos
dictionary.filter_extremes(no_below=4, no_above=0.4)

#Lista de algunas palabras que deben eliminarse del diccionario ya que son de contenido neutral pueden haber mas pero se uso un ejemplo como base
stoplist = set('also use make people know many call include part find become like mean often different \
                usually take wikt come give well get since type list say change see refer actually iii \
                aisne kinds pas ask would way something need things want every str'.split())
stop_ids = [dictionary.token2id[stopword] for stopword in stoplist if stopword in dictionary.token2id]
dictionary.filter_tokens(stop_ids)

#Convirtiendo la lista en una mátriz de términos en base al diccionario generado anteriormente
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

#Se crea el objeto para el modelo LDA usando gensim
ldamodel = Lda(doc_term_matrix, num_topics=50, id2word = dictionary, passes=50, iterations=500)
ldafile = open('lda_model_sym_wiki.pkl','wb')
pickle.dump(ldamodel,ldafile)
ldafile.close()

#Se imprimen los 50 temas con una cantidad de 10 palabras esto es configurable
for topic in ldamodel.print_topics(num_topics=50, num_words=10):
    print (topic[0]+1, " ", topic[1],"\n")

#Conclusiones
# A medida que analizamos los temas descubiertos por el modelo LDA, vemos que estos temas son básicamente una distribución probabilística de palabras que pueden describir muy bien un tema 
# o contenido en particular. Después de experimentar varias veces llegamos a la conclusión de que las palabras en los temas modelados pueden no ser perfectamente similares, 
# pero definitivamente están asociadas. Por el ejemplo el topico 23 esta relacionado con musica.    





















           
                       
                       
                       
