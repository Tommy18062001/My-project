from sys import exit
from random import randint


class Scene(object):
    def enter(self):
        print("the scene is not yet figured. Subclass it and implement enter()")

        exit(1)


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print("\n --------------------")
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
    quips = [
        "You died. You kinda sucks at this",
        "You mom would be proud .....if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)


class CentralCorridor(Scene):
    def enter(self):
        print("The Gothons of planet percal # 25 have invaded your ship and destroyed")
        print("Your entire crew, you're the last surviving member and your last")
        print("mission is to get the neutron destruct bomb from the weapons armory.")
        print("put it in the bridge, blow the ship up after getting into an escape pod")
        print("\n")
        print("you re runnning down the central corridor to the weapons armory when ")
        print("a gothons jumps out, red scaly skin, dark grimy teeth, evil clown costume")
        print("flowing around his hate filled body. He is blocking the door to the armory")
        print("and about to pull the weapon to blast you")

        action = input(">  ")

        if action == "shoot!":
            print("Quick on the draw you yank out your blaster and fire it to the gothon.")
            print("His clown costum is flowing and moving around his body, which throws")
            print("off you aim. Your laser hits his costume but misses him entirely. This")
            print("ruins completely his brand new costume his mother bought him, which")
            print("make him fly into a rage and blast you repeatedly in the face until")
            print("you are dead. Then, he eats you.")

            return "death"

        elif action == "dodge!":
            print("Like a world class boxer you dodge, weave, slip and slide right")
            print("as the gothon's blaster cranks a laser past your head")
            print("in the middle of your artful dodge your foot slips and you")
            print("bang your head on the metal wall and pass out")
            print("You wake up shortly after only to die as the gothon stompos on")
            print("your head and eats you")

            return "death"

        elif action == "tell a joke":
            print("Lucky for you they made you learn gothon insults in the academy.")
            print("You tell the one gothon joke you know:")
            print("Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr.")
            print("The gothon stops, tries not to laugh, then busts out laughing and can't move")
            print("While he is laughing you run up and shoot him square in the head")
            print("putting him down, them jump through the weapon armory door")

            return "laser weapon armory"

        else:
            print("DOES NOT COMPUTE")

            return "central corridor"


class LazerWeaponArmory(Scene):
    def enter(self):
        print("You do a dive roll into the weapon armory, crouch and scan the room")
        print("for more gothon that might be hiding. it's dead quiet, too quiet")
        print(" you stand up and run to the far side of the room and find the")
        print("neutron bomb in its container. There is a keypad lock on the box")
        print("and you need the code to get the bomb out. If you get the code")
        print("wrong 10 times then the lock closes forever and you can't")
        print("get the bomb. The code is 3 digits.")

        code = "d%d%d%" % (randint(1, 9), randint(1, 9), randint(1, 9))
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("BZZZZZEDDD")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(" The container clicks open and the seal breaks, letting gas out")
            print("You grab the neutron bomb and run as fast as you can to the")
            print("bridge where you must place it in the right spot")

            return "the bridge"


class TheBridge(Scene):
    def enter(self):
        print("you burst onto the bridge with the neutron destruct bomb")
        print("under your arm and surprise 5 gothons who are trying to")
        print("take control of the ship. Each of them has an  even uglier")
        print("clown costume than the last. They haven't pulled their")
        print("weapons out yet, as theu see the active bomb under your ")
        print("arm and don't want to see it off")

        action = input("> ")

        if action == "throw the bomb":
            print("In a panic you throw the bomb at the group of gothons")
            print("and make a leap for the door. Rigth as you drop it a")
            print("Gothon shoots you right in the back killing you")
            print("as you die you see another frantically try to disarm")
            print("the bomb. You die knowing that they will probably blow up when")
            print("it goes off.")
            return "death"

        elif action == "slowly place the bomb":
            print("you point your blaster at the bomb under your arm")
            print("and  the gothons put their hands up and start to sweat")
            print("You inch backward to the door, open it, and then carefully")
            print("place the bomb on the floor, pointing your blaster at it.")
            print("You then jump back through the door, punch the close button")
            print("and blast the lock so the gothons can't get out")
            print("Now that the bomb is placed you run to the escape pod to")
            print("get off this tin can")
            return "escape pod"

        else:
            print("DOES NOT COMPUTE")
            return "the bridge"


class EscapePod(Scene):
    def enter(self):
        print("You rush  through the ship desperately trying to make it to")
        print("the escape pod before the whole ship explodes. It seems like")
        print("hardly any gothons are on the ship, so your is clear of")
        print("interference. you get to the chamber with the escape pods, and")
        print("now need to pick one to take. Some of them could be damaged")
        print("but don't have the time to look. There is 5 pods, which one")
        print("do you take")

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print("You jump into pod %s and hit the eject button." % guess)
            print("The pod escapes out into the void of space, then")
            print("implodes as the hull ruptures, crushing your body")
            print("into jam jelly")
            return "death"

        else:
            print("you jump into pod %s and hit the ejection button." % guess)
            print("the pod easily slides out into space heading to")
            print("the planet below. As it flies to the planet, you look")
            print("back and see your ship implode then explode like a")
            print("bright star, taking out the gothon ship at the same")
            print("time. You won!!")

            return "finished"


class Map(object):

    scenes = {
        "central_corridor": CentralCorridor(),
        "laser_weapon_armory": LazerWeaponArmory(),
        "the bridge": TheBridge(),
        "escape_pod": EscapePod(),
        "death": Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map("central corridor")

a_game = Engine(a_map)

a_game.play()
