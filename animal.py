from enum import Enum
from datetime import datetime
from typing import List, Optional

class MoodState(Enum):
    HAPPY = "happy"
    NEUTRAL = "neutral"
    ANGRY = "angry"
    SLEEPY = "sleepy"

class Animal:
    def __init__(self, name: str, species: str, age: int):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = 50  # Scale 0-100
        self.thirst = 50  # Scale 0-100
        self.energy = 100  # Scale 0-100
        self.mood = MoodState.NEUTRAL
        self.last_fed: Optional[datetime] = None
        self.favorite_foods: List[str] = []
        self.weight = 0.0
        
    def feed(self, food: str, amount: float) -> bool:
        """Feed the animal with specified food and amount."""
        if self.hunger < 20:
            print(f"{self.name} is not hungry right now!")
            return False
            
        self.hunger = max(0, self.hunger - amount)
        self.energy += amount * 0.5
        self.weight += amount * 0.1
        self.last_fed = datetime.now()
        
        if food in self.favorite_foods:
            self.mood = MoodState.HAPPY
            print(f"{self.name} really enjoyed the {food}!")
        
        print(f"{self.name} has been fed {amount} of {food}")
        return True
        
    def drink(self, amount: float) -> None:
        """Give the animal water to drink."""
        self.thirst = max(0, self.thirst - amount)
        print(f"{self.name} drank some water. Thirst level: {self.thirst}")
        
    def sleep(self, hours: float) -> None:
        """Let the animal sleep for specified hours."""
        if self.energy >= 90:
            print(f"{self.name} is not tired!")
            return
            
        self.energy = min(100, self.energy + hours * 10)
        self.hunger += hours * 5
        self.thirst += hours * 3
        self.mood = MoodState.NEUTRAL
        print(f"{self.name} slept for {hours} hours. Energy level: {self.energy}")
        
    def play(self, duration: float) -> None:
        """Play with the animal for specified duration."""
        if self.energy < 20:
            print(f"{self.name} is too tired to play!")
            return
            
        self.energy = max(0, self.energy - duration * 10)
        self.hunger += duration * 5
        self.thirst += duration * 5
        self.mood = MoodState.HAPPY
        self.weight = max(0, self.weight - duration * 0.1)
        print(f"{self.name} played for {duration} hours! They're very happy!")
        
    def add_favorite_food(self, food: str) -> None:
        """Add a new favorite food for the animal."""
        if food not in self.favorite_foods:
            self.favorite_foods.append(food)
            
    def get_status(self) -> dict:
        """Return the current status of the animal."""
        return {
            "name": self.name,
            "species": self.species,
            "age": self.age,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "energy": self.energy,
            "mood": self.mood.value,
            "weight": self.weight,
            "last_fed": self.last_fed
        }

# Example usage
if __name__ == "__main__":
    lion = Animal("Leo", "Lion", 5)
    lion.add_favorite_food("meat")
    lion.feed("meat", 30)
    lion.drink(40)
    lion.play(2)
    lion.sleep(5)
    print(lion.get_status())
