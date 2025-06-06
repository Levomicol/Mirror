import logging

#- Есть некий список слов перебрать его исключая повторяющиеся;
#- Прописать алгоритм поиска слов полиномов(т.е. читающихся одинаково с обеих сторон);
#- Вывести строки в консоль задом на перёд, строки-полиномы заменить строкой "полином".

logging.basicConfig(filename="gfg-log.log", filemode="w", level=logging.DEBUG, format="%(name)s → %(levelname)s: %(message)s")
logger = logging.getLogger()

FileOutputHandler = logging.FileHandler('Messages.log')

logger.addHandler(FileOutputHandler)

list1 = ["ото", "этот", "эта", "эту", "тот", "этот"]
s = list(set(list1))

for i in s:
    reversed_i = i[::-1]
    
    if i == reversed_i:
           print("Полином!")
    else:
          string = [i]
          for st in string:
             reversed_st = st[::-1]
             print(reversed_st)
             logger.debug(reversed_st)


