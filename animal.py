from enum import Enum
from datetime import datetime
from typing import List, Optional

class ActivityState(Enum):
    SLEEPING = "sleeping"
    ACTIVE = "active"
    EATING = "eating"
    RESTING = "resting"

class Animal:
    def __init__(self, name: str, species: str, age_years: int):
        self.name = name
        self.species = species
        self.age_years = age_years
        self.energy = 50  # Scale 0-100
        self.hunger = 50  # Scale 0-100
        self.health = 100  # Scale 0-100
        self.activity_state = ActivityState.RESTING
        self.last_fed: Optional[datetime] = None
        self.favorite_foods: List[str] = []
        self.weight = 0.0
        
    def feed(self, amount: float) -> bool:
        """Feed the animal."""
        if self.hunger < 20:
            print(f"{self.name} is not hungry right now!")
            return False
            
        self.hunger = max(0, self.hunger - amount)
        self.energy = min(100, self.energy + amount * 0.2)
        self.last_fed = datetime.now()
        
        if self.energy > 80:
            self.activity_state = ActivityState.ACTIVE
            print(f"{self.name} is now active and playful!")
        
        print(f"{self.name} has been fed {amount} units of food")
        return True
        
    def exercise(self, intensity: float) -> None:
        """Exercise the animal to maintain health."""
        self.energy = max(0, self.energy - intensity)
        self.weight = max(0, self.weight - intensity * 0.1)
        print(f"{self.name} exercised. Energy level: {self.energy}")
        
    def sleep(self) -> None:
        """Let the animal sleep to recover energy."""
        if self.energy > 80:
            print(f"{self.name} is not tired enough to sleep!")
            return
            
        self.activity_state = ActivityState.SLEEPING
        self.energy = min(100, self.energy + 30)
        print(f"{self.name} is sleeping soundly")
        
    def add_favorite_food(self, food: str) -> None:
        """Add a favorite food for the animal."""
        if food not in self.favorite_foods:
            self.favorite_foods.append(food)
            print(f"{self.name} now likes {food}")
            
    def check_health(self) -> None:
        """Check the animal's health status."""
        if self.health < 50:
            print(f"Warning: {self.name} needs medical attention!")
        elif self.energy < 20:
            print(f"Warning: {self.name} is very tired!")
        elif self.hunger > 80:
            print(f"Warning: {self.name} is very hungry!")
        else:
            print(f"{self.name} is in good health!")

class Bird(Animal):
    def __init__(self, name: str, species: str, age_years: int, wingspan: float):
        super().__init__(name, species, age_years)
        self.wingspan = wingspan
        self.is_flying = False
        
    def fly(self) -> None:
        """Make the bird fly."""
        if self.energy < 20:
            print(f"{self.name} is too tired to fly!")
            return
        
        self.is_flying = True
        self.energy = max(0, self.energy - 10)
        print(f"{self.name} is now flying!")
        
    def land(self) -> None:
        """Make the bird land."""
        if not self.is_flying:
            print(f"{self.name} is already on the ground!")
            return
            
        self.is_flying = False
        print(f"{self.name} has landed safely.")

class Parrot(Bird):
    def __init__(self, name: str, age_years: int, vocabulary: List[str] = None):
        super().__init__(name, "Parrot", age_years, wingspan=20.0)
        self.vocabulary = vocabulary or []
        self.favorite_foods = ["seeds", "fruits", "nuts"]
        
    def speak(self, word: str) -> None:
        """Make the parrot speak a word from its vocabulary."""
        if word in self.vocabulary:
            print(f"{self.name} says: {word}")
        else:
            print(f"{self.name} doesn't know how to say '{word}'")
            
    def learn_word(self, word: str) -> None:
        """Teach the parrot a new word."""
        if word not in self.vocabulary:
            self.vocabulary.append(word)
            print(f"{self.name} learned to say '{word}'!")

class Eagle(Bird):
    def __init__(self, name: str, age_years: int):
        super().__init__(name, "Eagle", age_years, wingspan=200.0)
        self.favorite_foods = ["fish", "small mammals"]
        self.hunting_success_rate = 0.8
        
    def hunt(self) -> bool:
        """Make the eagle hunt for prey."""
        if self.energy < 30:
            print(f"{self.name} is too tired to hunt!")
            return False
            
        import random
        success = random.random() < self.hunting_success_rate
        
        if success:
            self.hunger = max(0, self.hunger - 30)
            self.energy = max(0, self.energy - 20)
            print(f"{self.name} successfully caught prey!")
        else:
            self.energy = max(0, self.energy - 15)
            print(f"{self.name}'s hunt was unsuccessful.")
            
        return success

# Example usage
if __name__ == "__main__":
    pet = Animal("Max", "Dog", 3)
    pet.add_favorite_food("meat")
    pet.feed(30)
    pet.exercise(20)
    pet.sleep()
    pet.check_health()

    parrot = Parrot("Polly", 5)
    parrot.speak("Hello")
    parrot.learn_word("Hello")
    parrot.speak("Hello")
    parrot.fly()
    parrot.land()

    eagle = Eagle("Eddie", 10)
    eagle.hunt()
    eagle.fly()
    eagle.land()
