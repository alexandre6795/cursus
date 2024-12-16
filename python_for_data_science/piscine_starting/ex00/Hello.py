# list list chainees et modifiable
# tulpe est non modifiable et ordonné
# set est non ordonné mais modifiable
# dict est basé sur une clé et une valeur

ft_list = ["Hello", "tata"]
ft_tuple = ("Hello", "toto")
ft_set = {"Hello", "titi"}
ft_dict = {"Hello": "tutu"}

ft_list[ft_list.index("tata")] = "World"
ft_tuple = ("Hello", "France")
ft_set = {"Hello", "Mulhouse"}
ft_dict["Hello"] = "42Mulhouse"

print(ft_list, "\n", ft_tuple, "\n", ft_set, "\n", ft_dict)
