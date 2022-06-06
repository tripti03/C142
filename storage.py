import csv
allmovies=[]

with open("final.csv",encoding="utf8")as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]

likemovie2=[]
notlikemovie=[]
didnot=[]