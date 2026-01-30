import json
from sys import argv


def main():
    file = open(argv[1]).read()
    replacer_json= open(argv[2]).read()
    
    replacer_dict = json.loads(replacer_json)

    for key in replacer_dict:
        file = file.replace(key, replacer_dict[key])

    print(file)
    
    
if __name__ == "__main__":
    main()
