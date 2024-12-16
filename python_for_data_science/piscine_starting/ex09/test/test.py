from ft_package import count_in_list
from ft_package import *
print(count_in_list.__doc__)
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0
