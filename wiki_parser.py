#Importando librerias
import xml.etree.ElementTree as ET
import codecs
import re

#Función que validad que el texto contengo solo caracteres ASCII
def is_ascii(s):
    return all(ord(c) < 128 for c in s)

#El dump de xml esta formado por una estructura de arbol
tree = ET.parse('enwiki-20220620-pages-articles-multistream1.xml')
root = tree.getroot()
dir_path = 'articles-corpus//'

#Recorremos dicha estructura hasta llegar al texto y limpiamos el mismo de caracteres especiales
for i,page in enumerate(root.findall('{http://www.mediawiki.org/xml/export-0.10/}page')):
    for p in page:    
        if p.tag == "{http://www.mediawiki.org/xml/export-0.10/}revision":
            for x in p:
                if x.tag == "{http://www.mediawiki.org/xml/export-0.10/}text":                    
                    article_txt = x.text
                    if not article_txt == None:                                                
                        article_txt = article_txt[ : article_txt.find("==")]
                        article_txt = re.sub(r"{{.*}}","",article_txt)
                        article_txt = re.sub(r"\[\[File:.*\]\]","",article_txt)
                        article_txt = re.sub(r"\[\[Image:.*\]\]","",article_txt)
                        article_txt = re.sub(r"\n: \'\'.*","",article_txt)
                        article_txt = re.sub(r"\n!.*","",article_txt)
                        article_txt = re.sub(r"^:\'\'.*","",article_txt)
                        article_txt = re.sub(r"&nbsp","",article_txt)
                        article_txt = re.sub(r"http\S+","",article_txt)
                        article_txt = re.sub(r"\d+","",article_txt)   
                        article_txt = re.sub(r"\(.*\)","",article_txt)
                        article_txt = re.sub(r"Category:.*","",article_txt)
                        article_txt = re.sub(r"\| .*","",article_txt)
                        article_txt = re.sub(r"\n\|.*","",article_txt)
                        article_txt = re.sub(r"\n \|.*","",article_txt)
                        article_txt = re.sub(r".* \|\n","",article_txt)
                        article_txt = re.sub(r".*\|\n","",article_txt)
                        article_txt = re.sub(r"{{Infobox.*","",article_txt)
                        article_txt = re.sub(r"{{infobox.*","",article_txt)
                        article_txt = re.sub(r"{{taxobox.*","",article_txt)
                        article_txt = re.sub(r"{{Taxobox.*","",article_txt)
                        article_txt = re.sub(r"{{ Infobox.*","",article_txt)
                        article_txt = re.sub(r"{{ infobox.*","",article_txt)
                        article_txt = re.sub(r"{{ taxobox.*","",article_txt)
                        article_txt = re.sub(r"{{ Taxobox.*","",article_txt)
                        article_txt = re.sub(r"\* .*","",article_txt)
                        article_txt = re.sub(r"<.*>","",article_txt)
                        article_txt = re.sub(r"\n","",article_txt)  
                        article_txt = re.sub(r"\!|\"|\#|\$|\%|\&|\'|\(|\)|\*|\+|\,|\-|\.|\/|\:|\;|\<|\=|\>|\?|\@|\[|\\|\]|\^|\_|\`|\{|\||\}|\~"," ",article_txt)
                        article_txt = re.sub(r" +"," ",article_txt)
                        article_txt = article_txt.replace(u'\xa0', u' ')
                       
                        #Hacemos la excepción de solo archivos que contengan una longitud de más de 150 caracteres y los guardamos individualmente dentro del directorio indicado.
                        if not article_txt == None and not article_txt == "" and len(article_txt) > 150 and is_ascii(article_txt):
                            outfile = dir_path + str(i+1) +"_article.txt"
                            f = codecs.open(outfile, "w", "utf-8")
                            f.write(article_txt)
                            f.close()
                            #Se imprime en pantalla los parrafos unificados de cada archivo
                            print (article_txt)
                            print ('\n=================================================================\n')
                             
    