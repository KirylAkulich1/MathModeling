import time


def get_middle_interval(number:int,interval_length:int)->int:
    number_str:str = str(number)
    number_len:int = len(number_str)
    middle_index= number_len//2
    interval_start = number_str[middle_index - interval_length//2: middle_index]
    interval_end = number_str[middle_index: middle_index +interval_length//2+ interval_length % 2]
    return int(interval_start + interval_end)

def middle_square_generator(seed:int)->int:
    interval_length:int = len(str(seed))
    previous_value= seed
    while True:
        next_value = get_middle_interval(previous_value**2,interval_length)
        yield next_value
        previous_value = next_value

if __name__=="__main__":
    seed_str = str(time.time()).replace('.','')[-8:]
    seed= int(seed_str)
    print(seed)



