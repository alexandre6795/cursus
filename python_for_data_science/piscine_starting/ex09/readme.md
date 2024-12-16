# ft_package
![License](https://img.shields.io/badge/license-MIT-blue)

## description
fonction for count string occurence in list

## installation
pip install your_path/dist/ft_package-0.0.1-py3-none-any.whl  
pip install your_path/dist/ft_package-0.0.1.tar.gz  

## exemple
from ft_package import count_in_list  
print(count_in_list.__doc__)  
print(count_in_list(["toto", "tata", "toto"], "toto"))  # output: 2  
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # output: 0  
