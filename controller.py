import menu
import rational
import complex
import UI
from time import sleep
import log

def BaseFunction():
    menuOut = menu.Menu()
    while True:
        try:
            if menuOut == 1:
                expression = UI.expRatio()
                result = rational.BaseFunction(expression)
                UI.result(expression, result)
                answer = expression + " = " + str(result)
                array = log.ReadData()
                array.append(answer)
                log.SaveData(array)
            elif menuOut == 2:
                expression = UI.expComplex()
                result = complex.BaseFunction(expression)
                UI.result(expression, result)
                answer = expression + " = " + str(result)
                array = log.ReadData()
                array.append(answer)
                log.SaveData(array)
            elif menuOut == 3:
                if log.ReadData() == []: UI.LogEmptyMsg()
                else:
                    UI.LogOutMsg()
                    UI.PrintLog()
            else:
                UI.ByeBye()
                sleep(1)
            break
        except: UI.expError()