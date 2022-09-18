from pydantic import BaseModel, validator, ValidationError
from typing import Literal, Optional, Union
import json


# Armor and weapon classes
class Armor(BaseModel):
    """Armor class"""
    name: str
    type: Literal['helmet', 'chestplate', 'leggings', 'boots', 'ring', 'pendant']
    description: Union[str, None] = None
    hp: Union[float, None] = None
    cc: Union[float, None] = None
    critdmg: Union[float, None] = None
    patk: Union[float, None] = None
    matk: Union[float, None] = None
    defense: Union[float, None] = None
    luck: Union[float, None] = None
    evasion: Union[float, None] = None
    mana: Union[float, None] = None

    @validator('name')
    def name_alpha(cls, v):
        assert v.isalpha(), 'Name must be only letters and spaces.'

        return v

    @validator('type', pre=True)
    def type_exists(cls, v):
        assert v is None, 'No type specified'

        return v

    @validator('type')
    def gender_valid(cls, v):
        assert v in ['helmet', 'chestplate', 'leggings', 'boots', 'ring', 'pendant'], 'Invalid type'

        return v


class Weapon(BaseModel):
    """Weapon class"""
    name: str
    type: Literal['sword', 'dagger', 'bow', 'crossbow', 'axe', 'gun', 'staff', 'wand', 'picatrix']
    description: Union[str, None] = None
    hp: Union[float, None] = None
    cc: Union[float, None] = None
    critdmg: Union[float, None] = None
    patk: Union[float, None] = None
    matk: Union[float, None] = None
    defense: Union[float, None] = None
    mana: Union[float, None] = None
    Element: Union[None, Literal['fire', 'water', 'earth', 'air', 'nature', 'radiant', 'shadow']] = None

    @validator('name')
    def name_alpha(cls, v):
        assert v.isalpha(), 'Name must be only letters and spaces.'

        return v

    @validator('type', pre=True)
    def type_exists(cls, v):
        assert v is None, 'No type specified'

        return v

    @validator('type')
    def gender_valid(cls, v):
        assert v in ['sword', 'dagger', 'bow', 'crossbow', 'axe', 'gun', 'staff', 'wand', 'picatrix'], 'Invalid type'

        return v


class Character(BaseModel):
    """Player class"""
    name: str
    gender: Literal['male', 'female']
    race: Literal['human', 'orc', 'elf', 'dwarf', 'goblin']
    hp: float
    level: int
    gold: int

    patk: float
    matk: float
    cc: float
    critdmg: float
    defense: float
    luck: float
    evasion: float
    mana: float

    helmet: Union[Armor, None] = None
    chestplate: Union[Armor, None] = None
    leggings: Union[Armor, None] = None
    boots: Union[Armor, None] = None
    ring: Union[Armor, None] = None
    pendant: Union[Armor, None] = None

    inventory: dict[str, Union[int, float]]
    cls: Literal['mage', 'warlock', 'warrior', 'rogue', 'paladin', 'monk', 'priest', 'hunter']

    @validator('name')
    def name_alpha(cls, v):
        assert v.isalpha(), 'Name must be only letters and spaces.'

        return v

    @validator('gender')
    def gender_valid(cls, v):
        assert v in ['male', 'female'], 'Invalid gender'

        return v

    @validator('race')
    def race_valid(cls, v):
        assert v in ['human', 'orc', 'elf', 'dwarf', 'goblin'], 'Invalid race'

        return v

    @validator('cls')
    def class_valid(cls, v):
        assert v in ['mage', 'warlock', 'warrior', 'rogue', 'paladin', 'monk', 'priest', 'hunter'], 'Invalid class'

        return v

    @validator('level', 'gold', 'patk', 'matk', 'cc', 'critdmg', 'defense', 'luck', 'evasion', 'mana')
    def valid_level(cls, v):
        assert v >= 0, 'Value must be 0 or higher.'

        return v


try:
    Neclo = Character.parse_obj(
        {'name': 'Josiah', 'gender': 'male', 'race': 'human', 'hp': 100, 'level': 0, 'gold': 10, 'patk': 5, 'matk': 5,
         'cc': 0.01, 'critdmg': 1.1, 'defense': 0.95, 'luck': 0, 'evasion': 0, 'mana': 100, 'helmet': None,
         'chestplate': None, 'leggings': None, 'boots': None, 'ring': None, 'pendant': None,
         'inventory': {}, 'cls': 'mage'})
except ValidationError as e:
    print(e)

info = json.dumps(Neclo.dict(), indent=4)
print(info)
