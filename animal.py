from enum import Enum
from datetime import datetime
from typing import List, Optional, Dict, Any
import json
from pathlib import Path

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
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert animal instance to dictionary for serialization."""
        return {
            "class": self.__class__.__name__,
            "name": self.name,
            "species": self.species,
            "age_years": self.age_years,
            "energy": self.energy,
            "hunger": self.hunger,
            "health": self.health,
            "activity_state": self.activity_state.value,
            "last_fed": self.last_fed.isoformat() if self.last_fed else None,
            "favorite_foods": self.favorite_foods,
            "weight": self.weight
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Animal':
        """Create an animal instance from dictionary."""
        animal = cls(data["name"], data["species"], data["age_years"])
        animal.energy = data["energy"]
        animal.hunger = data["hunger"]
        animal.health = data["health"]
        animal.activity_state = ActivityState(data["activity_state"])
        animal.last_fed = datetime.fromisoformat(data["last_fed"]) if data["last_fed"] else None
        animal.favorite_foods = data["favorite_foods"]
        animal.weight = data["weight"]
        return animal
    
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
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert bird instance to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "wingspan": self.wingspan,
            "is_flying": self.is_flying
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Bird':
        """Create a bird instance from dictionary."""
        bird = super().from_dict(data)
        bird.wingspan = data["wingspan"]
        bird.is_flying = data["is_flying"]
        return bird
    
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

class Tucan(Bird):
    def __init__(self, name: str, age_years: int, vocabulary: List[str] = None):
        super().__init__(name, "Tucan", age_years, wingspan=20.0)
        self.vocabulary = vocabulary or []
        self.favorite_foods = ["seeds", "fruits", "nuts"]
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert tucan instance to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "vocabulary": self.vocabulary
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tucan':
        """Create a tucan instance from dictionary."""
        tucan = cls(data["name"], data["age_years"], data["vocabulary"])
        tucan.energy = data["energy"]
        tucan.hunger = data["hunger"]
        tucan.health = data["health"]
        tucan.activity_state = ActivityState(data["activity_state"])
        tucan.last_fed = datetime.fromisoformat(data["last_fed"]) if data["last_fed"] else None
        tucan.wingspan = data["wingspan"]
        tucan.is_flying = data["is_flying"]
        return tucan
    
    def speak(self, word: str) -> None:
        """Make the Tucan speak a word from its vocabulary."""
        if word in self.vocabulary:
            print(f"{self.name} says: {word}")
        else:
            print(f"{self.name} doesn't know how to say '{word}'")
            
    def learn_word(self, word: str) -> None:
        """Teach the Tucan a new word."""
        if word not in self.vocabulary:
            self.vocabulary.append(word)
            print(f"{self.name} learned to say '{word}'!")

class Eagle(Bird):
    def __init__(self, name: str, age_years: int):
        super().__init__(name, "Eagle", age_years, wingspan=200.0)
        self.favorite_foods = ["fish", "small mammals"]
        self.hunting_success_rate = 0.8
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert eagle instance to dictionary for serialization."""
        data = super().to_dict()
        data.update({
            "hunting_success_rate": self.hunting_success_rate
        })
        return data
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Eagle':
        """Create an eagle instance from dictionary."""
        eagle = cls(data["name"], data["age_years"])
        eagle.energy = data["energy"]
        eagle.hunger = data["hunger"]
        eagle.health = data["health"]
        eagle.activity_state = ActivityState(data["activity_state"])
        eagle.last_fed = datetime.fromisoformat(data["last_fed"]) if data["last_fed"] else None
        eagle.wingspan = data["wingspan"]
        eagle.is_flying = data["is_flying"]
        eagle.hunting_success_rate = data["hunting_success_rate"]
        return eagle
    
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

class Zoo:
    def __init__(self, name: str):
        self.name = name
        self.animals: List[Animal] = []
        self.feeding_schedule: Dict[str, datetime] = {}
        
    def to_dict(self) -> Dict[str, Any]:
        """Convert zoo instance to dictionary for serialization."""
        return {
            "name": self.name,
            "animals": [animal.to_dict() for animal in self.animals],
            "feeding_schedule": {
                name: time.isoformat() 
                for name, time in self.feeding_schedule.items()
            }
        }
        
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Zoo':
        """Create a zoo instance from dictionary."""
        zoo = cls(data["name"])
        
        # Create appropriate animal instances based on class
        for animal_data in data["animals"]:
            animal_class = globals()[animal_data["class"]]
            animal = animal_class.from_dict(animal_data)
            zoo.animals.append(animal)
            
        # Restore feeding schedule
        zoo.feeding_schedule = {
            name: datetime.fromisoformat(time)
            for name, time in data["feeding_schedule"].items()
        }
        
        return zoo
        
    def save_to_file(self, filepath: str) -> None:
        """Save zoo state to a JSON file."""
        data = self.to_dict()
        
        # Ensure directory exists
        Path(filepath).parent.mkdir(parents=True, exist_ok=True)
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Zoo state saved to {filepath}")
        
    @classmethod
    def load_from_file(cls, filepath: str) -> 'Zoo':
        """Load zoo state from a JSON file."""
        with open(filepath, 'r') as f:
            data = json.load(f)
        zoo = cls.from_dict(data)
        print(f"Zoo state loaded from {filepath}")
        return zoo
    
    def add_animal(self, animal: Animal) -> None:
        """Add a new animal to the zoo."""
        self.animals.append(animal)
        print(f"{animal.name} the {animal.species} has been added to {self.name}")
        
    def remove_animal(self, animal: Animal) -> bool:
        """Remove an animal from the zoo."""
        if animal in self.animals:
            self.animals.remove(animal)
            print(f"{animal.name} has been removed from {self.name}")
            return True
        print(f"{animal.name} is not in {self.name}")
        return False
        
    def feed_all_animals(self, amount: float = 30.0) -> None:
        """Feed all animals in the zoo."""
        for animal in self.animals:
            animal.feed(amount)
            self.feeding_schedule[animal.name] = datetime.now()
            
    def check_animals_health(self) -> None:
        """Check health status of all animals."""
        for animal in self.animals:
            animal.check_health()
            
    def get_animals_by_species(self, species: str) -> List[Animal]:
        """Get all animals of a specific species."""
        return [animal for animal in self.animals if animal.species == species]
        
    def get_hungry_animals(self) -> List[Animal]:
        """Get list of animals that need feeding (hunger > 70)."""
        return [animal for animal in self.animals if animal.hunger > 70]
        
    def exercise_all_animals(self, intensity: float = 10.0) -> None:
        """Exercise all animals with given intensity."""
        for animal in self.animals:
            animal.exercise(intensity)
            
    def daily_report(self) -> str:
        """Generate a daily report of all animals' status."""
        report = f"\nDaily Report for {self.name}\n"
        report += "=" * 40 + "\n"
        
        for animal in self.animals:
            report += f"\nName: {animal.name} ({animal.species})"
            report += f"\nAge: {animal.age_years} years"
            report += f"\nHealth: {animal.health}%"
            report += f"\nHunger: {animal.hunger}%"
            report += f"\nEnergy: {animal.energy}%"
            report += f"\nState: {animal.activity_state.value}"
            report += "\n" + "-" * 30
            
        return report

# Example usage
if __name__ == "__main__":
    pet = Animal("Max", "Dog", 3)
    pet.add_favorite_food("meat")
    pet.feed(30)
    pet.exercise(20)
    pet.sleep()
    pet.check_health()

    tucan = Tucan("Polly", 5)
    tucan.speak("Hello")
    tucan.learn_word("Hello")
    tucan.speak("Hello")
    tucan.fly()
    tucan.land()

    eagle = Eagle("Eddie", 10)
    eagle.hunt()
    eagle.fly()
    eagle.land()

    zoo = Zoo("Wildlife Paradise")
    
    # Create and add animals
    tucan = Tucan("Polly", 5)
    eagle = Eagle("Eddie", 10)
    
    zoo.add_animal(tucan)
    zoo.add_animal(eagle)
    
    # Test zoo operations
    zoo.feed_all_animals()
    zoo.check_animals_health()
    zoo.exercise_all_animals()
    
    # Save zoo state
    zoo.save_to_file("zoo_state.json")
    
    # Load zoo state
    loaded_zoo = Zoo.load_from_file("zoo_state.json")
    print(loaded_zoo.daily_report())
