from pathlib import Path

#Absolute path
# C:\ProhramFiles\Microsoft
# /usr/local/bin
#Relative path
path = Path("SampleDirectory")
print(path.exists())

#path2=Path("emails")
#print(path2.mkdir())
#path2.rmdir();

path3=Path()
for file in path3.glob('*.py'):
    print(file)




