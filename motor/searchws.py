# Search in tweets
# -*- coding=utf-8 -*-
import os, sys
# Adding this to path to be able to import irlib
#sys.path.append('../../')

from irlib.preprocessor import Preprocessor
from irlib.matrix import Matrix
#from nltk.corpus import stopwords
from model import db_default_session
from model.matrixdb import Matrixdb
from datetime import date
from pickle import Pickler, Unpickler
import CGIHTTPServer

class Search:

    def __init__(self):
        self._mx = Matrix()
        self._prep = Preprocessor(pattern='\W+', lower=True, stem=True)

    def readfiles(self, fold_path='all-folds/fold1/'):

        ruta = os.path.split(sys.argv[0])
        abs = os.path.join(ruta[0], fold_path)
        files = os.listdir(abs)
        for filename in files:
            abs_arch = os.path.join(abs, filename)
            fd = open(abs_arch, 'r')
            file_data = fd.read()

            self.createMX(filename, file_data)

        print 'Number of read documents:', len(self._mx.docs)
        print 'Number of read terms', len(self._mx.terms)
        #print mx.terms[0:5], mx.terms[-5:-1]
        '''print mx.terms
        for doc in mx.docs:
            print doc'''
        self.saveMX(self._mx)

    def saveMX(self, mx):
        ruta = os.path.split(sys.argv[0])
        abs = os.path.join(ruta[0], "db/matrix.mx")
        filemx = open(abs, 'w')
        serializer = Pickler(filemx)
        serializer.dump(mx)
        print 'matrix salvada'

    def createMX(self, file_id, file_data, lenguaje = 'english'):
        stop = stopwords.words(lenguaje)
        file = file_data.split(" ")
        content = [w for w in file if w.lower() not in stop]
        data = content.__str__()
        terms = self._prep.ngram_tokenizer(text=data)
        if len(terms) > 0:
            self._mx.add_doc(doc_id=file_id, doc_terms=terms,
                        frequency=True, do_padding=True)

    def search(self):
        ruta = os.path.split(sys.argv[0])
        abs = os.path.join(ruta[0], "db/matrix.mx")

        filemx = open(abs, 'r')
        serializer = Unpickler(filemx)
        self._mx = serializer.load()

        web = cgi.FieldStorage()
        cadena = web['buscar']
        cade = cadena.lower()
        cad = self._prep.ngram_tokenizer(text=cade)
        resultado = list()
        for doc in self._mx.docs:
            vector = list()
            for q in cad:
                if q in self._mx.terms:
                    pos = self._mx.terms.index(q)
                    vector.append(doc['terms'][pos])
            resultado.append((doc['id'],vector))
        resultado.sort(lambda a,b: self.__Deuclidiana(a[1]) - self.__Deuclidiana(b[1]), reverse = True)
        print resultado

    def __Deuclidiana(self, vector):
        dist = 0
        for v in vector:
            dist+=v**2
        return dist.__int__()


    def main(self):
        #self.readfiles()
        self.search(True)

if __name__ == "__main__":
    motor = Search()
    motor.main()

