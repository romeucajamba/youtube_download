import pytube

# O link
url = str(input("Digite o link do vídeo: "))

# solicitação para a URL fornecida
conn = pytube.YouTube(url)

# Download
conn.streams.first().download()

print('Download', url)

