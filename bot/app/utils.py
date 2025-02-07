import os 
def get_index(day_path: str, time_path: str) -> int:
    # Если папка существует, то возвращаем последний индекс + 1
    # Если папки нет, то возвращаем 0 и создаём дир с временем сообщения()


    full_path = f"bot/data/{day_path}/{time_path}/"
    if not os.path.isdir(f"bot/data/{day_path}/"):
        os.mkdir(f"bot/data/{day_path}")

    # print(os.path.isdir(full_path))
    

    if os.path.isdir(full_path) and os.listdir(full_path): #TODO WHY IT RETURNS [] WHAT THE FUCK
        # print(f"listdir ----> {os.listdir(full_path)}")
        # print(max([int(s.split(".")[0]) for s in os.listdir(full_path)]))
        #print(max([int(s.split(".")[0]) for s in os.listdir(full_path)])+1)
        return max([int(s.split(".")[0]) for s in os.listdir(full_path)])+1
            
    else:
        os.mkdir(full_path)
        return 0

