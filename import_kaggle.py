import json
import zipfile
import os



api_token = {"username":"davidsanchezcalle","key":"808d7b5385b3285eb256b2161df70724"}

##Contectar a Kaggle

with open("C:/Users/a0197/.kaggle/kaggle.json","w") as file:
    json.dump(api_token, file)

location = "C:/pparcial/dataset"


##Validar que la carpeta exista

if not os.path.exists(location):
    ##Si no existe se crea
    os.mkdir(location)
else:
    ##SI la carpeta existe, borrar el contenido
    for root, dirs, files in os.walk(location, topdown=False):
        for name in files:
            os.remove(os.path.join(root,name))  ##eliminos los archivos
        for name in dirs:
            os.rmdir(os.path.join(root, name))  ##Eliminar las carpetas

##Descargar dataser de Kaggle
            
os.system("kaggle datasets download -d henryshan/starbucks -p C:/pparcial/dataset")


##Descomprimir el archiv
os.chdir(location)
for file in os.listdir():
    zip_ref = zipfile.ZipFile(file,"r")
    zip_ref.extractall()
    zip_ref.close()
    