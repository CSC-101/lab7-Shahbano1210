from typing import Optional

# Task 1
def str_to_float(input:str)-> Optional[float]: #takes in an input str and returns a converted float
    try:
        return float(input)
    except ValueError:
        return None
