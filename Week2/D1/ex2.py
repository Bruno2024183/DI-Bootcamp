class Dog:
    def _init_(self, name, height):
        self.name = name
        self.height = height

def bark(self):
    print(f"{self.name} goes woof!")

def jump(self):
    jump_height = self.height * 2
    print(f"{self.name} jumps {jump_height} cm high!")

davids_dog = Dog("Rex", 50)
print(f"David's dog is named {david_dog.name} and is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()

sarahs_dog = Dog("Teacup", 20)
print(f"Sarah's dog is name {sarahs_dog.name} and is {sarahs_dog.height} csm tall")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    print(f"The bigger dog is {davids_dog.name}")
else:
    print(f"The bigger dog is {sarahs_dog.name}")
