def get_cats_info(path:str) -> list[dict]:
    
    try :
        with open(path, 'r') as file :
            lines = file.readlines()
            
    except  (FileNotFoundError, OSError) as err :
        return f"An exception occurred: {type(err).__name__}"
    else :
        cats_info = []
        for line in lines:
            line = line.strip()
            cat_data = line.split(',')
            cat_dict = {'id': cat_data[0], 'name': cat_data[1], 'age': cat_data[2]}
            cats_info.append(cat_dict)
        return cats_info
    
    
