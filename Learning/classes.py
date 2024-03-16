class Dog:
    """Model of a dog"""
    
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate dog sitting in response to command"""
        print(f"{self.name} is now sitting...")
    
    def roll_over(self):
        """Simultae dog rolling over in response to command"""
        print(f"{self.name} is now rolling over...")

my_dog = Dog("Jonsie", 7)
neighbors_dog = Dog("Scruffy", 1)

print(f"My dog {my_dog.name} is {my_dog.age} years old.")
print(f"My neighbors dog {neighbors_dog.name} is {neighbors_dog.age} years old.")
