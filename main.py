from src import macros

def main():
    macros.save_to_json(macros.get_macros('банан 100гр и курица 100гр'))
    #print(get_macros('150 грам риса курица жаренная в соевом соусе 100 гр'))

if __name__ == '__main__':
    main()