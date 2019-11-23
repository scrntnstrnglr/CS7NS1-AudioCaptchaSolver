def numbersAreTogether(text):
    for i in range(0,len(text)-1):
        if text[i].isdigit() and text[i+1].isdigit():
            return True
    return False
    
print(numbersAreTogether('999'))
