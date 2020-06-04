# Importação
from datetime import date
import datetime
import holidays

# Todos o Feriádos Nacionais
visualizar_feriados_brasileiros = holidays.Brazil
#Escolhendo o Ano e Estado
data_atual = date.today()
estado = 'PB'

#Criando uma lista de feriados personalizado
feriados_brasil = holidays.HolidayBase()

#Adicionando dentro da lista personalizada todos os feriados nacionais e do estado selecionado
for date, name in sorted(visualizar_feriados_brasileiros(state=estado, years=data_atual.year).items()):
    feriados_brasil.append({date:name})

#Visualizando todos os feriados adicionados a lista personalizada
for date, name in sorted(feriados_brasil.items()):
    print(f"{date.strftime('%d/%m/%Y')}-{name}")
print("\n")


#Adicionando os finais de semana
a = datetime.datetime.today()
numdays = 365
dateList = []
for x in range (0, numdays):
    dateList.append(a + datetime.timedelta(days = x))

for date in sorted(dateList):
    if(date.date().isoweekday()==6):
        feriados_brasil.append({date.date():"Sábado"})
    elif(date.date().isoweekday()==7):
        feriados_brasil.append({date.date():"Domingo"})
#Adicionando algum feriado
dateds = datetime.date(2020,8,9)
feriados_brasil.append({dateds:'Meu Aniversário'})

#Visualizando todos os feriados e finais de semanas adicionado a lista
for date, name in sorted(feriados_brasil.items()):
    print(f"{date.strftime('%d/%m/%Y')}-{name}")
print("\n")







# #Adicionando os finais de semana
# a = datetime.datetime.today()
# numdays = 365
# dateList = []
# for x in range (0, numdays):
#     dateList.append(a + datetime.timedelta(days = x))
#
# for date in sorted(dateList):
#     if(date.date().isoweekday()==6):
#         print(date.date(),"-","Sábado")
#     elif(date.date().isoweekday()==7):
#         print(date.date(), "-", "Domingo")
