import pytube

link = 'https://www.youtube.com/watch?v=G-jKlhaA1_k&ab_channel=Emanero'
youlink = pytube.YouTube(link)
title = str(youlink.title)+'.mp3'
print('Titulo: ', youlink.title)
print('Autor: ', youlink.author)
youlink.streams.filter(abr='160kbps', progressive=False).first().download(filename=title)
print('Descarga con exito de: ', link)