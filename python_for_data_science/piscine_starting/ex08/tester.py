from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm
print("my progress bar")
for elem in ft_tqdm(range(333)):
    sleep(0.005)
print()
print("tqdm progress bar")
for elem in tqdm(range(333)):
    sleep(0.005)
print()
