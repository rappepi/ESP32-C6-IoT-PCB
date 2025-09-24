import os
path = os.path.dirname(__file__)
while(True):
    LCSC_ID = input("ID composant LCSC : ")
    try:
        os.system(rf'easyeda2kicad --full --lcsc_id {LCSC_ID} --overwrite --output "{path}\Library\Projet_Puissance"')
    except Exception as exception:
        print(exception)
    print('\n' + '-'*100 + '\n')