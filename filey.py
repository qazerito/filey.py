import os,shutil

os.chdir('/home/alex/Downloads')
current = os.getcwd()

files = os.listdir(current)

class col:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'


print(col.OKGREEN,"[Filey] Filey File Organiser V3")

images = [".jpeg",".png",".jpg",".gif"]
text = [".doc",".txt",".pdf",".xlsx",".docx",".xls",".rtf"]
videos = [".mp4",".mkv"]
sounds = [".mp3",".wav",".m4a"]

for file in files:
    d = ""
    for ex in images:
        if file.endswith(ex):
            d = '/home/alex/Pictures'
            shutil.move(file,d)
            print(" [Filey]",file,">>",d)
            break

    for ex in text:
        if file.endswith(ex):
            d = '/home/alex/Documents/Text Files'
            shutil.move(file,d)
            print(" [Filey]",file,">>",d)
            break

    for ex in sounds:
        if file.endswith(ex):
            d = '/home/alex/Music'
            shutil.move(file,d)
            print(" [Filey]",file,">>",d)
            break

    for ex in videos:
        if file.endswith(ex):
            d = '/home/alex/Videos'
            shutil.move(file,d)
            print(" [Filey]",file,">>",d)
            break
            
print(col.OKGREEN,"[Filey] Completed Successfully")
