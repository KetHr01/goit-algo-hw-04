from pathlib import Path

def total_salary(path):
    try:
        if not isinstance(path, (Path, str)):
            raise TypeError("Invalid file path. Expected a string or Path object.")

        suma = 0
        with open(path, 'r', encoding='utf-8') as file:
            data = file.readlines()
            if len(data) == 0:
                raise ZeroDivisionError("File is empty, cannot calculate average salary.")
            
            for d in data:
                salary = d.split(',')
                suma += int(salary[1].strip())
                
        return suma, suma / len(data)
    
    except FileNotFoundError:
        return "No such file"
    except TypeError as e:
        return str(e)
    except ValueError:
        return "Invalid data format: salary must be an integer."
    except IndexError:
        return "Invalid data format: missing salary field in some rows."
    except ZeroDivisionError as e:
        return str(e)

if __name__=='__main__':
    result = total_salary("developers.txt")
    if isinstance(result, tuple): 
        total, average = result
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    else:
        print(result)

