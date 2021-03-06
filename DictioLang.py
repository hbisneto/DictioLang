## DictioLang

from translate import Translator
from datetime import date

AnoAtual = date.today().year
SoftwareName = "DictioLang"
Version = "1.0"
CopyrightName = "Heitor Bisneto."
Idioma = []

print("="*80)
print(f'[{SoftwareName}] - Em Execução...')
print("="*80)
print("Nome:", SoftwareName)
print("Versão:", Version)
print("Criado por:", CopyrightName)

if AnoAtual == 2021:
    print("Copyright ©", AnoAtual, "|", CopyrightName, "All rights reserved.")
else:
    print("Copyright © 2021 -", AnoAtual, "|", CopyrightName, "All rights reserved.")
print()

def App():
    print("="*80)
    print(f'[{SoftwareName}] - Menu de Idiomas')
    print("="*80)
    MeuTexto = str(input(">> Digite o texto que gostaria de traduzir: "))
    print("="*80)
    print(f'>> 1. Português')
    print(f'>> 2. Ingles')
    print(f'>> 3. Espanhol')
    print(f'>> 4. Francês')
    print(f'>> 5. Italiano')
    print(f'>> 6. Alemão')
    print(f'>> 7. Romeno')
    FromInt = int(input(">> Digite o número da opção que condiz com o texto inserido: "))

    if FromInt == 1:
        Idioma.append("Portuguese")
    elif FromInt == 2:
        Idioma.append("English")
    elif FromInt == 3:
        Idioma.append("Spanish")
    elif FromInt == 4:
        Idioma.append("French")
    elif FromInt == 5:
        Idioma.append("Italian")
    elif FromInt == 6:
        Idioma.append("German")
    elif FromInt == 7:
        Idioma.append("Romanian")
    else:
        print(">> Idioma não disponível")

    print()
    print("="*80)
    print(f'[{SoftwareName}] - Traduzir para...')
    print("="*80)
    print(f'>> 1. Português')
    print(f'>> 2. Ingles')
    print(f'>> 3. Espanhol')
    print(f'>> 4. Francês')
    print(f'>> 5. Italiano')
    print(f'>> 6. Alemão')
    print(f'>> 7. Romeno')
    ToInt = int(input(">> O texto será traduzido para: "))

    if ToInt == 1:
        Idioma.append("Portuguese")
    elif ToInt == 2:
        Idioma.append("English")
    elif ToInt == 3:
        Idioma.append("Spanish")
    elif ToInt == 4:
        Idioma.append("French")
    elif ToInt == 5:
        Idioma.append("Italian")
    elif ToInt == 6:
        Idioma.append("German")
    elif ToInt == 7:
        Idioma.append("Romanian")
    else:
        print(">> Idioma não disponível")
        
    Process = Translator(from_lang = Idioma[0], to_lang = Idioma[1])
    Resposta = Process.translate(MeuTexto)
    print()
    print(f'>> Texto Traduzido: {Resposta}')
    print()
    print()
    print('>> Digite "App()" para executar o programa novamente')
    print('>> Caso esteja usando o "Terminal", digite "Python3 MyTranslator.py" para executar o programa novamente')

App()
