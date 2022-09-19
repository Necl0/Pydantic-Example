from __future__ import annotations
from pydantic import BaseModel, validator, ValidationError, confloat, conint, constr
from typing import Literal, Optional, Union


# Armor and weapon classes
class Armor(BaseModel):
    """Armor class"""
    name: str
    type: Literal['helmet', 'chestplate', 'leggings', 'boots', 'ring', 'pendant']
    description: Optional[str] = None
    hp: Optional[float] = None
    cc: Optional[float] = None
    critdmg: Optional[float] = None
    patk: Optional[float] = None
    matk: Optional[float] = None
    defense: Optional[float] = None
    luck: Optional[float] = None
    evasion: Optional[float] = None
    mana: Optional[float] = None

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
    description: Optional[str] = None
    hp: Optional[float] = None
    cc: Optional[float] = None
    critdmg: Optional[float] = None
    patk: Optional[float] = None
    matk: Optional[float] = None
    defense: Optional[float] = None
    mana: Optional[float] = None
    Element: Optional[Literal['fire', 'water', 'earth', 'air', 'nature', 'radiant', 'shadow']] = None

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
    name: constr(max_length=20)
    gender: Literal['male', 'female']
    race: Literal['human', 'orc', 'elf', 'dwarf', 'goblin']
    hp: confloat(gt=-1)
    level: conint(gt=-1)
    gold: confloat(gt=-1)

    patk: confloat(gt=-1)
    matk: confloat(gt=-1)
    cc: confloat(gt=-1)
    critdmg: confloat(gt=-1)
    defense: confloat(gt=-1)
    luck: confloat(gt=-1)
    evasion: confloat(gt=-1)
    mana: confloat(gt=-1)

    helmet: Optional[Armor] = None
    chestplate: Optional[Armor] = None
    leggings: Optional[Armor] = None
    boots: Optional[Armor] = None
    ring: Optional[Armor] = None
    pendant: Optional[Armor] = None

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


try:
    Neclo = Character.parse_obj(
        {'name': 'Josiah', 'gender': 'male', 'race': 'human', 'hp': 100, 'level': 0, 'gold': 10, 'patk': 5, 'matk': 5,
         'cc': 0.01, 'critdmg': 1.1, 'defense': 0.95, 'luck': 0, 'evasion': 0, 'mana': 100, 'helmet': None,
         'chestplate': None, 'leggings': None, 'boots': None, 'ring': None, 'pendant': None,
         'inventory': {}, 'cls': 'mage'})
except ValidationError as e:
    print(e)

