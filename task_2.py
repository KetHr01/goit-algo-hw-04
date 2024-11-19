from pathlib import Path

def get_cats_info(path):
    cats = []
    try:
        if not isinstance(path, (Path, str)):
            raise TypeError("Invalid file path. Expected a string or Path object.")

        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()       
            if not data:
                return "The file is empty."     
            for d in data:
                one_cat = {}
                cat = d.split(',')
                one_cat['id'] = cat[0].strip()
                one_cat['name'] = cat[1].strip()
                one_cat['age'] = cat[2].strip()
                cats.append(one_cat)               
        return cats
    
    except FileNotFoundError:
        return "No such file"
    except TypeError as e:
        return str(e)

if __name__=='__main__':    
    cats_info = get_cats_info("cats.txt")
    print(cats_info)
 