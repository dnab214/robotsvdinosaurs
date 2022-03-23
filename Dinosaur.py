from tkinter.font import names


class Dinosaur:
    def __init__(self):
        self.name = []
        self.attack_power = None
        self.health = None


def load_dinosaur_traits(dinosaur_name, attack_power_moves):
    dinosaur_name = ['brachiosaurus', 'apatosaurus', 'barosaurus']
    attack_power_moves = ['fire-breathing', 'transformation', 'airbending']
    user_input = input("Which breeed will you choose to fight?")
    print(f'I summon {dinosaur_name[1]} for the big battle!')
    print(f'{dinosaur_name[1]} will use {attack_power_moves[1]} to fight!')



    