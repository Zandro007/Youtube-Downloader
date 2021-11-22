from pytube import Youtube

# Digite o link do video e o local p/ arquivo

link = input('Digite o link do video: ') 
arquivo = input('Local de armazenamento do arquivo: ') 
yt = Youtube(link)

# Mostra detalhes do video video

print('Titulo: ', yt.title) 
print('Numero de visualizações:'yt.views) 
print('Tamanho do video: ', yt.lenght, "segundos") 
print('Avaliação do video: ', yt.rating)

# Melhor resolução de video

ys = yt.streams.get_highest_resolution()

# Download

print('Baixando.....') yt.donwload(arquivo) print('Dowload concluido com sucesso!!')