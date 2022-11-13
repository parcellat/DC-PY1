import random
def get_random_password() -> str:
    l = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    return(random.sample(l, 8))
print(get_random_password())
