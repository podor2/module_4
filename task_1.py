def total_salary(path: str) -> list[float]:
    
    total_salary = 0
    avarage_salary = 0
    try:
        with open(path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                workers_salary = float((line.split(','))[1])
                total_salary += workers_salary
            avarage_salary = total_salary / len(lines)
    except (FileNotFoundError, OSError):
        print (f'Dear user, an Error occured, please check if path is correct')
    return total_salary, avarage_salary


