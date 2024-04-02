import random

class AtaqueStrategy:
    def ejecutar(self):
        pass

# Todos los ataques con su respectiva clase
class Impactrueno(AtaqueStrategy):
    def ejecutar(self):
        return "Impactrueno"

    @property
    def daño(self):
        return 30

class Rayo(AtaqueStrategy):
    def ejecutar(self):
        return "Rayo"

    @property
    def daño(self):
        return 25

class AtaqueRapido(AtaqueStrategy):
    def ejecutar(self):
        return "Ataque Rápido"

    @property
    def daño(self):
        return 20

class Placaje(AtaqueStrategy):
    def ejecutar(self):
        return "Placaje"

    @property
    def daño(self):
        return 15

class Tacleada(AtaqueStrategy):
    def ejecutar(self):
        return "Tacleada"

    @property
    def daño(self):
        return 10

class Supersonico(AtaqueStrategy):
    def ejecutar(self):
        return "Supersónico"

    @property
    def daño(self):
        return 10

class Drenadoras(AtaqueStrategy):
    def ejecutar(self):
        return "Drenadoras"

    @property
    def daño(self):
        return 5

class Picotazo(AtaqueStrategy):
    def ejecutar(self):
        return "Picotazo"

    @property
    def daño(self):
        return 20

class Remolino(AtaqueStrategy):
    def ejecutar(self):
        return "Remolino"

    @property
    def daño(self):
        return 15

class Tornado(AtaqueStrategy):
    def ejecutar(self):
        return "Tornado"

    @property
    def daño(self):
        return 10

class LátigoCepa(AtaqueStrategy):
    def ejecutar(self):
        return "Látigo Cepa"

    @property
    def daño(self):
        return 25

class Somnífero(AtaqueStrategy):
    def ejecutar(self):
        return "Somnífero"

    @property
    def daño(self):
        return 20

class Lanzallamas(AtaqueStrategy):
    def ejecutar(self):
        return "Lanzallamas"

    @property
    def daño(self):
        return 30

class Gruñido(AtaqueStrategy):
    def ejecutar(self):
        return "Gruñido"

    @property
    def daño(self):
        return 10

class Arañazo(AtaqueStrategy):
    def ejecutar(self):
        return "Arañazo"

    @property
    def daño(self):
        return 15

class Ascuas(AtaqueStrategy):
    def ejecutar(self):
        return "Ascuas"

    @property
    def daño(self):
        return 20

class PistolaAgua(AtaqueStrategy):
    def ejecutar(self):
        return "Pistola Agua"

    @property
    def daño(self):
        return 25

class Burbuja(AtaqueStrategy):
    def ejecutar(self):
        return "Burbuja"

    @property
    def daño(self):
        return 20

class TajoCruzado(AtaqueStrategy):
    def ejecutar(self):
        return "Tajo Cruzado"

    @property
    def daño(self):
        return 25

class Hipercolmillo(AtaqueStrategy):
    def ejecutar(self):
        return "Hipercolmillo"

    @property
    def daño(self):
        return 30

class Lodo(AtaqueStrategy):
    def ejecutar(self):
        return "Lodo"

    @property
    def daño(self):
        return 25

class BombaLodo(AtaqueStrategy):
    def ejecutar(self):
        return "Bomba Lodo"

    @property
    def daño(self):
        return 20

class AtaqueAcido(AtaqueStrategy):
    def ejecutar(self):
        return "Ataque Ácido"

    @property
    def daño(self):
        return 25

class Infortunio(AtaqueStrategy):
    def ejecutar(self):
        return "Infortunio"

    @property
    def daño(self):
        return 15

class Hidropulso(AtaqueStrategy):
    def ejecutar(self):
        return "Hidropulso"

    @property
    def daño(self):
        return 30

class RayoBurbuja(AtaqueStrategy):
    def ejecutar(self):
        return "Rayo Burbuja"

    @property
    def daño(self):
        return 20
    
class GolpeCabeza(AtaqueStrategy):
    def ejecutar(self):
        return "Golpe Cabeza"
    
    @property
    def daño(self):
        return 10

# Define la clase Pokémon y sus respectivos ataques
class Pokemon:
    def __init__(self, nombre, ataques, salud_maxima=100):
        self.nombre = nombre
        self.ataques = ataques
        self.salud_maxima = salud_maxima
        self.salud_actual = salud_maxima

    def elegir_ataque(self):
        ataque = random.choice(self.ataques)
        return ataque

    def recibir_daño(self, daño):
        self.salud_actual -= daño
        if self.salud_actual < 0:
            self.salud_actual = 0

    def esta_vivo(self):
        return self.salud_actual > 0

    def esta_muerto(self):
        return not self.esta_vivo()

# Define la clase Pikachu
class Pikachu(Pokemon):
    def __init__(self):
        ataques = [Impactrueno(), Rayo(), AtaqueRapido(), Placaje()]
        super().__init__("Pikachu", ataques, salud_maxima=150)

# Define la clase Caterpie
class Caterpie(Pokemon):
    def __init__(self):
        ataques = [Placaje(), Tacleada(), Supersonico(), Drenadoras()]
        super().__init__("Caterpie", ataques, salud_maxima=100)

# Define la clase Pidgeotto
class Pidgeotto(Pokemon):
    def __init__(self):
        ataques = [Picotazo(), Remolino(), Tornado(), AtaqueRapido()]
        super().__init__("Pidgeotto", ataques, salud_maxima=120)

# Define la clase Bulbasaur
class Bulbasaur(Pokemon):
    def __init__(self):
        ataques = [LátigoCepa(), Drenadoras(), Placaje(), Somnífero()]
        super().__init__("Bulbasaur", ataques, salud_maxima=130)

# Define la clase Charmander
class Charmander(Pokemon):
    def __init__(self):
        ataques = [Lanzallamas(), Gruñido(), Arañazo(), Ascuas()]
        super().__init__("Charmander", ataques, salud_maxima=140)

# Define la clase Squirtle
class Squirtle(Pokemon):
    def __init__(self):
        ataques = [PistolaAgua(), Burbuja(), AtaqueRapido(), Placaje()]
        super().__init__("Squirtle", ataques, salud_maxima=130)

# Define la clase Krabby
class Krabby(Pokemon):
    def __init__(self):
        ataques = [Burbuja(), RayoBurbuja(), Placaje(), TajoCruzado()]
        super().__init__("Krabby", ataques, salud_maxima=120)

# Define la clase Raticate
class Raticate(Pokemon):
    def __init__(self):
        ataques = [Hipercolmillo(), AtaqueRapido(), Placaje(), GolpeCabeza()]
        super().__init__("Raticate", ataques, salud_maxima=140)

# Define la clase Muk
class Muk(Pokemon):
    def __init__(self):
        ataques = [Lodo(), BombaLodo(), AtaqueAcido(), Infortunio()]
        super().__init__("Muk", ataques, salud_maxima=160)

# Define la clase Kingler
class Kingler(Pokemon):
    def __init__(self):
        ataques = [Hidropulso(), RayoBurbuja(), Rayo(), Placaje()]
        super().__init__("Kingler", ataques, salud_maxima=150)

class EquipoPokemon:
    def __init__(self):
        self.pokemones = []

    def agregar_pokemon(self, pokemon):
        if len(self.pokemones) < 3:
            self.pokemones.append(pokemon)
        else:
            print("No se pueden agregar más de 3 pokemones al equipo.")

    def elegir_pokemon(self):
        return random.choice(self.pokemones)

class BatallaPokemon:
    def __init__(self, equipo1, equipo2):
        self.equipo1 = equipo1
        self.equipo2 = equipo2

    def iniciar_batalla(self):
        while any(pokemon.esta_vivo() for pokemon in self.equipo1.pokemones) and any(pokemon.esta_vivo() for pokemon in self.equipo2.pokemones):
            pokemon_equipo1 = self.equipo1.elegir_pokemon()
            pokemon_equipo2 = self.equipo2.elegir_pokemon()

            while pokemon_equipo1.esta_vivo() and pokemon_equipo2.esta_vivo():
                ataque_pokemon1 = pokemon_equipo1.elegir_ataque()
                ataque_pokemon2 = pokemon_equipo2.elegir_ataque()

                # Pokémon 1 ataca a Pokémon 2
                daño_pokemon2 = ataque_pokemon1.daño
                pokemon_equipo2.recibir_daño(daño_pokemon2)
                print(f"{pokemon_equipo1.nombre} usa {ataque_pokemon1.ejecutar()} y causa {daño_pokemon2} de daño a {pokemon_equipo2.nombre}. Vida restante: {pokemon_equipo2.salud_actual}")

                # Verificar si el Pokémon 2 ha sido derrotado
                if not pokemon_equipo2.esta_vivo():
                    print(f"{pokemon_equipo2.nombre} ha sido derrotado.")

                # Pokémon 2 ataca a Pokémon 1
                if pokemon_equipo2.esta_vivo():
                    daño_pokemon1 = ataque_pokemon2.daño
                    pokemon_equipo1.recibir_daño(daño_pokemon1)
                    print(f"{pokemon_equipo2.nombre} usa {ataque_pokemon2.ejecutar()} y causa {daño_pokemon1} de daño a {pokemon_equipo1.nombre}. Vida restante: {pokemon_equipo1.salud_actual}")

                    # Verificar si el Pokémon 1 ha sido derrotado
                    if not pokemon_equipo1.esta_vivo():
                        print(f"{pokemon_equipo1.nombre} ha sido derrotado.")

        if any(pokemon.esta_vivo() for pokemon in self.equipo1.pokemones):
            print("¡El equipo 1 ha ganado la batalla!")
        else:
            print("¡El equipo 2 ha ganado la batalla!")


# Creamos dos equipos de Pokémon
equipo_pokemon1 = EquipoPokemon()
equipo_pokemon1.agregar_pokemon(Pikachu())
equipo_pokemon1.agregar_pokemon(Bulbasaur())
equipo_pokemon1.agregar_pokemon(Charmander())

equipo_pokemon2 = EquipoPokemon()
equipo_pokemon2.agregar_pokemon(Squirtle())
equipo_pokemon2.agregar_pokemon(Krabby())
equipo_pokemon2.agregar_pokemon(Raticate())

# Iniciamos la batalla entre los equipos
batalla = BatallaPokemon(equipo_pokemon1, equipo_pokemon2)
batalla.iniciar_batalla()