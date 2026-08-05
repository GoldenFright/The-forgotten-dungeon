import time


import textwrap
import random as rn
import pygame
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
list = ["Sword", "Defence", "Cutlass", "Gold", "Diamond ore", "Petrol", "Coal", "Diamond", "Time capsule",
        "Earthworm", "Stone", "Lost key", "Ore tracker", "Katana", "Info scroll", "Iron ore", "Gold ore", "Iron",
        "Ore tracker scroll", "Smelt scroll", "Use scroll", "Fishing rod", "Pickaxe", "Cod", "Salmon", "Tuna",
        "Boot", "Gun", "Shrimp", "Piranha", "Catfish", "Stingray", "Toothed whale", "Great white", "Shark tooth", "Shovel"]
value = [400, 250, 1000, 400, 0, 400, 550, 1500, 10000, 150, 100, 6000, 12000, 3500, 1000, 0, 0, 250, 0, 600, 800,
         2000, 6000, 250, 200, 320, 50, 0, 350, 1000, 350, 1100, 5000, 7000, 500, 1500]
rarity = ["Common", "Epic", "Epic", "Epic", "Epic", "Rare", "Rare", "Legendary", "Mythic", "Common",
          "Common", "Mythic", "Mythic", "Legendary", "Epic", "Rare", "Rare", "Epic", "Mythic", "Epic", "Epic",
          "Epic", "Mythic", "Common", "Rare", "Epic", "Common", "Legendary", "Epic", "Epic", "Rare", "Epic", "Legendary",
          "Legendary", "Epic", "Mythic"]
info = ["Can be used in combat. 3 of this can upgrade to a Cutlass", "UNKNOWN FUNCTION",
        "Can be used in combat. 4 of these can upgrade to a Katana", "It is a highly valueable Ore",
        "It is the unpure form of diamond. Can be smelted into Diamond", "It is a highly valuable liquid", "It is a mineral",
        "It is a very highly valuable Resource.",
        "This can be used to travel back in time and find the same item you found last",
        "It is just an insect. It can be used as bait", "It is just a stone", "It's a key but to where you don't know",
        "When mining increases the drop of ores.",
        "Can be used in comabat. Strongest weapon in the game",
        "Use /scroll or /read for infos of other scrolls.", "Can be smelted into Iron", "Can be smelted into Gold",
        "It is a mineral", "Use /scroll or /read to read this", "Use /scroll or /read to read this",
        "Use /scroll or /read to read this", "This allows the player to use /fish", "This allows the user to use /mine",
        "It is just a fish. It is edible", "It is just a fish. It is edible", "It is just a fish. It is edible",
        "It is just a boot you encountered while fishing", "It is a gun. Pew Pew. Can be used in combat",
        "This can not be eaten but is a good bait", "It is a fish that bites, OUCH! It isn't edible but sell for a handsome amount of money",
        "It is an edible fish", "It snaps its tale with brute force. ANHH! It is not edible",
        "It is a whale but of a smaller kind. Not edible but sell for a LOT!",
        "It is the top contenders in sharks! Very big. If you catch one of these consider yourself lucky. Obviously not edible",
        "Its is an evidence of the sharks' presence but doesn't mean much. A lovely relic to flex", "Allows you to dig"]
loc = ["/grind", "/grind", "/grind", "/mine", "/mine", "/mine", "/mine", "/mine", "/dig", "/dig", "/dig and /mine",
       "/dig", "/dig", "upgrading cutlass", "/dig", "/mine", "/mine", "/mine", "!@#$@#?", "/dig", "/dig and /mine",
       "/shop or /buy", "/shop or /buy", "/fish", "/fish", "/fish", "/fish", "/shop", "/fish", "/fish", "/fish", "/fish",
       "/fish", "/fish", "/fish", "/shop"]
color = {
    "Common": (78, 81, 128),
    "Rare": (67, 189, 40),
    "Epic": (173, 47, 152),
    "Legendary": (181, 148, 16),
    "Mythic": (168, 27, 27)
}

try:
    file = open("data.txt", "r+")
except FileNotFoundError:
    file = open("data.txt", "w+")
    shld = "10" * len(list)
    file.write(f"{shld}\n1500\n0\n0\n0\n0.0")
    st = 0
else:
    st = 1


file.seek(0)
mode = 0
inventory = file.readlines()
balance = str(inventory[1])
balance = int(balance[:-1])
of = (inventory[2])
of = int(of[:-1])
ore = inventory[3]
ore = int(ore[:-1])
state = inventory[4]
state = int(state[:-1])
exp_time = inventory[5]
exp_time = (float(exp_time[:-1]))
inventory = str(inventory[0])
inventory = (inventory[:-1])
true = ""
ld = 0
inv = []
running = True
_ = 0
while _ < len(inventory):
    for x in range(int(inventory[_])):
        _ += 1
        true += inventory[_]
    inv.append(int(true))
    _ += 1
    true = ""

price = 0

for i in range(len(list)):
    inv.append(int(inventory[i]))

i = 1
nahi = 0

def add(item, *u):
    u = str(u)
    u = str(u[2:])
    u = str(u[:-3])
    if len(item) > 2:
        item = str(item)
    else:
        item = " ".join(item)
    for _ in range(len(list)):
        if item == list[_]:
            inv[_] += int(u)


def remove(item, *u):
    u = str(u)
    u = str(u[1:])
    u = str(u[:-2])
    if len(item) > 2:
        item = str(item)
    else:
        item = " ".join(item)
    item.capitalize()
    for _ in range(len(list)):
        if item == list[_]:
            inv[_] -= int(u)
if st == 0:
    print(f"Welcome to the Gooner game by GoldenFright use /help to find out more\nbtw ur starting with 1500"
          f"🪙 coins!")
else:
    print(f"You have a total of {balance} 🪙 coins from your last save point\nUse /inv to see your inventory")

if ore != 0:
    smelted = min(
        int((time.time() - exp_time) / 6),
        inv[ore],
        inv[list.index("Coal")] * 9
    )
    if smelted > 0:
        remove(list[ore], smelted)
        add(list[ore].split(" ")[0], str(smelted))
        remove("Coal", (smelted + 8) // 9)
        exp_time += smelted * 6
while True:
    command = input("Enter a command : ")

    if "earn" in command:
        possible = [0, 230, 102, 304, 99, 0, 500, 0, 211]
        choice = rn.choice(possible)
        balance = balance + choice
        print("you earned", choice, "🪙 coins!")
    elif "grind" in command:
        possible = [420, "Nothing LoL", 290, 32, 0, "Nothing. Well done!", "Nothing. Better Luck Next Time",
                    204, "1 Sword", "1 Defence", "Nothing. But make sure to support our art dev immeteor_❤️", 1095, "1 Cutlass", "Nothing, what are the odds??", 92, 400,
                    "2 Sword", "1 Shovel", "1 Shovel", "1 Pickaxe", "1 Fishing rod", "1 Gun"]
        choice = rn.choice(possible)
        try:
            choice = int(choice)
        except ValueError:
            if "Nothing" not in choice:
                c = choice.split(" ")


                for _ in range(len(list)):
                    if c[1:] == list[_].split(" "):
                        if inv[_] == 0:

                            pygame.init()
                            running = True
                            screen = pygame.display.set_mode((300, 400))
                            clock = pygame.time.Clock()
                            scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
                            scroll = pygame.transform.scale(scroll, (300, 400))
                            sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
                            font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)

                            try:
                                icon = sheet.subsurface((_ * 32, 0, 32, 32))
                            except ValueError:
                                icon = sheet.subsurface((0, 0, 1, 1))
                            else:
                                icon = pygame.transform.scale(icon, (100, 100))
                            running = True
                            while running:

                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        running = False

                                screen.blit(scroll, (0, 0))
                                pygame.draw.rect(
                                    screen,
                                    (70, 45, 25),
                                    (90, 140, 120, 120)
                                )
                                screen.blit(icon, (100, 150))
                                txt = font.render(
                                    "You found a",
                                    True,
                                    (60, 30, 20)
                                )
                                screen.blit(txt, (40, 80))
                                txt = font.render(
                                    "New Item!",
                                    True,
                                    (60, 30, 20)
                                )
                                screen.blit(txt, (60, 110))
                                txt = font.render(
                                    str(list[_]),
                                    True,
                                    (60, 30, 20)
                                )
                                screen.blit(txt, ((300 - len(list[_]) * 20) / 2, 270))

                                pygame.display.update()
                                clock.tick(60)

                            pygame.quit()
                print("you found","x", choice)
                add(c[1:], c[0])
            else:
                print("you grinded", choice)
        else:
            balance = balance + choice
            print("you grinded", choice, "🪙 Coins")
    elif "mine" in command:
        if inv[list.index("Pickaxe")] > 0:
            if of == 0:
                possible = ["Nothing. But make sure to support our art dev immeteor_❤️", "4 Iron ore", "4 Gold ore", "4 Iron ore",
                            "1 Use scroll", "5 Coal", "10 Petrol", "15 Petrol", "5 Coal", "2 Diamond ore", "2 Diamond ore",
                            "Nothing. But make sure to support our art dev immeteor_❤️", "Nothing. But make sure to support our art dev immeteor_❤️",
                            "6 Gold ore", "8 Iron ore", "8 Gold ore", "6 Iron ore", "1 Diamond", "3 Gold", "4 Iron", "2 Iron ore",
                            "Nothing! LoL", "Nothing haha", "Nothing! You return empty handed", "Nothing! what are the odds??", "Nothing",
                            "Nothing. But make sure to support our art dev immeteor_❤️", "Nothing. But make sure to support our art dev immeteor_❤️",
                            "Nothing haha", "Nothing but always buy me a coffee", "Nothing but subscribe to my channel www.youtube.com/@goldenfright",
                            "Nothing lmao", "Nothing", "Nothing, at this point try something else", "Nothing hahaha", "Nothing", "Nothing"]
            else:
                possible = ["Dungeon"]
                of -= 1
            choice = rn.choice(possible)
            try:
                int(choice)
            except ValueError:
                if "Nothing" not in choice:
                    if inv[18] == 2 and choice == "Ore tracker scroll":
                        choice = "Dungeon"
                    if "Dungeon" != choice:
                        c = choice.split(" ")
                        add(c[1:], c[0])
                        print("you found", choice)
                    else:
                        st = 0
                        print("As you enter the depths of the mine; you spot some metal Bars!'It might be beacause of the"
                              " Ore tracker!', you think to yourself.")
                        fr = input("What will you do? Investigate(1) or Leave(0) : ")
                        if fr == "1" or "vest" in fr:
                            print("You go closer to the bars and tug them with all your force to realise it is locked!")
                            while True:
                                if inv[11] > 0:
                                    if st == 0:
                                        g = input(f"You then remember of the {inv[11]} Lost keys with you. Would you"
                                                  f"like to check if they work? : ")
                                    else:
                                        g = input(f"That key didn't work you think maybe the other one could."
                                                  f"Would you like to check if they work : ")
                                    if g == "1" or g == "yes":
                                        remove("Lost key", 1)
                                        if rn.randint(1, 5) == 3:
                                            print("The key slides in and you twist it... The lock opens with a Bang!"
                                                  "that echoes around the mine. You head inside...")
                                            time.sleep(2)
                                            wrapped = textwrap.wrap("Let me explain this to you now. You are entering the Dungeon. You will have to fight enemies in here."
                                                                    "Fighting is turn based you will be given moves according to the weapoons in your inventory."
                                                                    "You are going to have 3 turns, in each turn you can either attack, move or eat. You enemies have 2 turns each"
                                                                    " So you should maintain your distance. You have a total of 20 health, the same as each of your enemies."
                                                                    "Your enemies have to be on the same position as you to attack you. They deal 4 damage per hit."
                                                                    "Try not to die and good luck", 80)
                                            for line in wrapped:
                                                print(line)
                                                time.sleep(3)
                                            pygame.init()
                                            pygame.mixer.init()
                                            click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
                                            window = pygame.display.set_mode((64 * 6, 64 * 6))
                                            ofx = 32
                                            ofy = ofx
                                            px = 32 * 6
                                            py = px
                                            pat = 0
                                            health = 20
                                            enemies = [[3, 0, 20], [0, 0, 20], [6, 0, 20]]
                                            BG = (30, 20, 15)
                                            clock = pygame.time.Clock()
                                            turn = 3
                                            LIGHT = (10, 10, 10)
                                            DARK = (0, 0, 0)
                                            dir = 0
                                            ld = 0
                                            PLAYER = (200, 60, 60)
                                            running = True
                                            font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 12)
                                            h = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
                                            mode = "play"
                                            dash = 0
                                            target = pygame.image.load(resource_path("assets/target.png")).convert_alpha()
                                            lock = pygame.image.load(resource_path("assets/lock.png")).convert_alpha()
                                            slash = pygame.image.load(resource_path("assets/slash.png")).convert_alpha()
                                            slashes = [slash.subsurface((0, 0, 192, 64)), slash.subsurface((192, 0, 192, 64)), slash.subsurface((384, 0, 192, 64))]
                                            slash = pygame.image.load(resource_path("assets/dslash.png")).convert_alpha()
                                            dslashes = [slash.subsurface((0, 0, 128, 128)), slash.subsurface((128, 0, 128, 128)), slash.subsurface((256, 0, 128, 128))]
                                            pat_name = ["Jab", "Slash", "Dash"]
                                            scroll = pygame.transform.scale(pygame.image.load(resource_path("assets/scroll.png")).convert_alpha(), (64 * 6, 64 * 6))
                                            nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
                                            left = nav.subsurface((10, 0, 10, 10))
                                            left = pygame.transform.scale(left, (50, 50))
                                            sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
                                            diag_offsets = {
                                                -45: [-16, 32],
                                                -135: [-32, -16],
                                                -225: [16, -32],
                                                -315: [32, 16],
                                            }
                                            pygame.mixer.music.load(resource_path("assets/sounds/bgm.wav"))
                                            pygame.mixer.music.set_volume(0.4)
                                            pygame.mixer.music.play(-1)
                                            while running:

                                                if mode == "play":
                                                    need = [0, 2, 13]
                                                    if turn == 0:
                                                        for enemy in enemies:
                                                            if round(enemy[2]) > 0:
                                                                time.sleep(0.2)
                                                                for o in range(2):
                                                                    if round(enemy[1]) > 3:
                                                                        for i in range(8):
                                                                            time.sleep(0.01)

                                                                            for row in range(7):
                                                                                for col in range(7):
                                                                                    cem = LIGHT if (
                                                                                                               row + col) % 2 == ld else DARK

                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        cem,
                                                                                        (col * 64 - ofx,
                                                                                         row * 64 - ofy,
                                                                                         64,
                                                                                         64)
                                                                                    )

                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        PLAYER,
                                                                                        (px - 64 // 4,
                                                                                         py - 64 // 4,
                                                                                         64 // 2,
                                                                                         64 // 2)
                                                                                    )

                                                                                    for q in enemies:
                                                                                        if q[2] > 0:
                                                                                            pygame.draw.rect(
                                                                                                window,
                                                                                                (0, 255, 0),
                                                                                                (q[0] * 64 - 16,
                                                                                                 q[1] * 64 - 16,
                                                                                                 32,
                                                                                                 32)
                                                                                            )

                                                                            enemy[1] -= 1 / 8
                                                                            pygame.display.update()

                                                                    elif round(enemy[1]) < 3:

                                                                        for i in range(8):
                                                                            time.sleep(0.01)

                                                                            for row in range(7):
                                                                                for col in range(7):
                                                                                    cem = LIGHT if (
                                                                                                               row + col) % 2 == ld else DARK

                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        cem,
                                                                                        (col * 64 - ofx,
                                                                                         row * 64 - ofy,
                                                                                         64,
                                                                                         64)
                                                                                    )

                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        PLAYER,
                                                                                        (px - 64 // 4,
                                                                                         py - 64 // 4,
                                                                                         64 // 2,
                                                                                         64 // 2)
                                                                                    )

                                                                                    for q in enemies:
                                                                                        if q[2] > 0:
                                                                                            pygame.draw.rect(
                                                                                                window,
                                                                                                (0, 255, 0),
                                                                                                (q[0] * 64 - 16,
                                                                                                 q[1] * 64 - 16,
                                                                                                 32,
                                                                                                 32)
                                                                                            )

                                                                            enemy[1] += 1 / 8
                                                                            pygame.display.update()

                                                                    else:

                                                                        if round(enemy[0]) > 3:

                                                                            for i in range(8):
                                                                                time.sleep(0.01)

                                                                                for row in range(7):
                                                                                    for col in range(7):
                                                                                        cem = LIGHT if (
                                                                                                                   row + col) % 2 == ld else DARK

                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            cem,
                                                                                            (col * 64 - ofx,
                                                                                             row * 64 - ofy,
                                                                                             64,
                                                                                             64)
                                                                                        )

                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            PLAYER,
                                                                                            (px - 64 // 4,
                                                                                             py - 64 // 4,
                                                                                             64 // 2,
                                                                                             64 // 2)
                                                                                        )

                                                                                        for q in enemies:
                                                                                            if q[2] > 0:
                                                                                                pygame.draw.rect(
                                                                                                    window,
                                                                                                    (0, 255, 0),
                                                                                                    (q[0] * 64 - 16,
                                                                                                     q[1] * 64 - 16,
                                                                                                     32,
                                                                                                     32)
                                                                                                )

                                                                                enemy[0] -= 1 / 8
                                                                                pygame.display.update()

                                                                        elif round(enemy[0]) < 3:

                                                                            for i in range(8):
                                                                                time.sleep(0.01)

                                                                                for row in range(7):
                                                                                    for col in range(7):
                                                                                        cem = LIGHT if (
                                                                                                                   row + col) % 2 == ld else DARK

                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            cem,
                                                                                            (col * 64 - ofx,
                                                                                             row * 64 - ofy,
                                                                                             64,
                                                                                             64)
                                                                                        )

                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            PLAYER,
                                                                                            (px - 64 // 4,
                                                                                             py - 64 // 4,
                                                                                             64 // 2,
                                                                                             64 // 2)
                                                                                        )

                                                                                        for q in enemies:
                                                                                            if q[2] > 0:
                                                                                                pygame.draw.rect(
                                                                                                    window,
                                                                                                    (0, 255, 0),
                                                                                                    (q[0] * 64 - 16,
                                                                                                     q[1] * 64 - 16,
                                                                                                     32,
                                                                                                     32)
                                                                                                )

                                                                                enemy[0] += 1 / 8
                                                                                pygame.display.update()

                                                                        else:

                                                                            health -= 4

                                                                            desc = font.render(
                                                                                "-4",
                                                                                True,
                                                                                (168, 27, 27)
                                                                            )

                                                                            window.blit(
                                                                                desc,
                                                                                (3 * 64 - 16, 3 * 64 + 16)
                                                                            )

                                                                            pygame.display.update()
                                                                            time.sleep(0.1)
                                                        turn = 3

                                                    for event in pygame.event.get():

                                                        if event.type == pygame.QUIT:
                                                            running = False
                                                        if turn >0:
                                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                                cacel = True
                                                                mx, my = pygame.mouse.get_pos()
                                                                for rec in rects:
                                                                    if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                                                        click.play()
                                                                        if rects.index(rec) < 3:
                                                                            for x in range(rects.index(rec), len(need)):
                                                                                if inv[need[x]] >= 1:
                                                                                    pat = rects.index(rec) + 1
                                                                                    break
                                                                        else:
                                                                            if rects.index(rec) == 4:
                                                                                if inv[list.index("Gun")] != 0:
                                                                                    pat == 4
                                                                            elif rects.index(rec) == 5:
                                                                                mode =0
                                                                                pygame.mixer.Sound(resource_path(
                                                                                    "assets/sounds/open.wav")).play()


                                                                mx = (mx + 32)// 64
                                                                my = (my + 32) // 64
                                                                if pat == 2:
                                                                    atk = [[[2, 2], [3, 2], [4, 2]], [[3, 2], [4, 2], [4, 3]], [[4, 2], [4, 3], [4, 4]], [[4, 3], [4, 4], [3, 4]],
                                                                           [[4, 4], [3, 4], [2, 4]], [[3, 4], [2, 4], [2, 3]], [[2, 4], [2, 3], [2, 2]], [[2, 3], [2, 2], [3, 2]],
                                                                            ]
                                                                    if turn > 0:
                                                                        for dam in atk:
                                                                            if dam[1][0] == mx and dam[1][1] == my:
                                                                                dir = -atk.index(dam) * 45
                                                                                atk = dam
                                                                                cacel = False
                                                                elif pat == 1:
                                                                    atk = [[[3, 2]], [[4, 2]], [[4, 3]], [[4, 4]], [[3, 4]], [[2, 4]], [[2, 3]], [[2, 2]]]
                                                                    for dam in atk:
                                                                        if dam[0][0] == mx and dam[0][1] == my:
                                                                            dir = -atk.index(dam) * 45
                                                                            atk = dam
                                                                            cacel = False
                                                                elif pat == 3:
                                                                    atk = [[[3, 2], [3, 1]], [[4, 3], [5, 3]], [[2, 3], [1, 3]], [[3, 4], [3, 5]]]
                                                                    for dam in atk:
                                                                        for q in dam:
                                                                            if q[0] == mx and q[1] == my:
                                                                                cacel = False
                                                                                if atk.index(dam) % 2 == 0:
                                                                                    dir = 90
                                                                                else:
                                                                                    dir = 0
                                                                                if atk.index([dam[0], dam[1]]) == 0:
                                                                                    dash = "up"
                                                                                elif atk.index([dam[0], dam[1]]) == 1:
                                                                                    dash = "right"
                                                                                elif atk.index([dam[0], dam[1]]) == 2:
                                                                                    dash = "left"
                                                                                else:
                                                                                    dash = "down"
                                                                                atk = [[3, 3], dam[0], dam[1]]
                                                                elif pat == 4:
                                                                    atk= [[[3, 2], [3, 1], [3, 0]], [[2, 3], [1, 3], [0, 3]], [[3, 4], [3, 5], [3, 6]], [[4, 3], [5, 3], [6, 3]]]
                                                                    for dam in atk:
                                                                        for q in dam:
                                                                            if q[0] == mx and q[1] == my:
                                                                                cacel = False
                                                                                if atk.index(dam) % 2 == 0:
                                                                                    dash = "v"
                                                                                else:
                                                                                    dash = "h"
                                                                                atk = dam

                                                                if not cacel:
                                                                    turn -= 1
                                                                    for enemy in enemies:
                                                                        for i, dam in enumerate(atk):
                                                                            if enemy[2] > 0:
                                                                                if round(enemy[0]) == dam[0] and round(enemy[1]) == dam[1]:
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        (255, 0, 0),
                                                                                        (enemy[0] * 64 - 16, enemy[1] * 64 -16, 32, 32)
                                                                                    )

                                                                                    if pat == 2:
                                                                                        enemy[2] -= 3
                                                                                        desc = font.render(
                                                                                            "-3",
                                                                                            True,
                                                                                            (255, 255, 255)
                                                                                        )
                                                                                        window.blit(desc, (
                                                                                            enemy[0] * 64 - 16,
                                                                                            enemy[1] * 64 - 8))
                                                                                    elif pat == 1:
                                                                                        enemy[2] -= 5
                                                                                        desc = font.render(
                                                                                            "-5",
                                                                                            True,
                                                                                            (255, 255, 255)
                                                                                        )
                                                                                        window.blit(desc, (
                                                                                            enemy[0] * 64 - 16,
                                                                                            enemy[1] * 64 - 8))
                                                                                    elif pat == 3:
                                                                                        enemy[2] -=4
                                                                                        desc = font.render(
                                                                                            "-4",
                                                                                            True,
                                                                                            (255, 255, 255)
                                                                                        )
                                                                                        window.blit(desc, (
                                                                                            enemy[0] * 64 - 16,
                                                                                            enemy[1] * 64 - 8))
                                                                                    elif pat == 4:
                                                                                        enemy[2] -=3
                                                                                        desc = font.render(
                                                                                            "-3",
                                                                                            True,
                                                                                            (255, 255, 255)
                                                                                        )
                                                                                        window.blit(desc, (
                                                                                            enemy[0] * 64 - 16,
                                                                                            enemy[1] * 64 - 8))
                                                                            if pat != 4:

                                                                                if str(dir)[-1] == "0":
                                                                                    img = pygame.transform.rotate(
                                                                                    slashes[atk.index(dam)], dir)
                                                                                    try:
                                                                                        imgr = img.get_rect(center=(
                                                                                            (atk[1][0] * 64), (atk[1][1] * 64)))
                                                                                    except IndexError:
                                                                                        imgr = img.get_rect(center=(
                                                                                            (atk[0][0] * 64), (atk[0][1] * 64)))
                                                                                else:
                                                                                    img = pygame.transform.rotate(dslashes[atk.index(dam)], dir + 45)
                                                                                    try:
                                                                                        imgr = img.get_rect(center=(
                                                                                            (atk[1][0] * 64 + diag_offsets[dir][0]), (atk[1][1] * 64 + diag_offsets[dir][1])))
                                                                                    except IndexError:
                                                                                        imgr = img.get_rect(center=(
                                                                                            (atk[0][0] * 64 + diag_offsets[dir][0]), (atk[0][1] * 64 + diag_offsets[dir][1])))
                                                                                if pat == 1:

                                                                                    for frame in range(3):
                                                                                        img = pygame.transform.rotate(
                                                                                            slashes[frame],
                                                                                            dir
                                                                                        )
                                                                                        img = pygame.transform.scale(img, (64, 64))

                                                                                        imgr = img.get_rect(
                                                                                            center=(atk[0][0] * 64,
                                                                                                    atk[0][1] * 64)
                                                                                        )

                                                                                        window.blit(img, imgr)
                                                                                        pygame.display.update()
                                                                                        time.sleep(0.01)


                                                                                window.blit(img, imgr)

                                                                            else:
                                                                                if dash == "v":
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        (255, 255, 255),
                                                                                        (dam[0] * 64, dam[1] * 64, 8, 64)
                                                                                    )
                                                                                else:
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        (255, 255, 255),
                                                                                        (dam[0] * 64, dam[1] * 64, 64, 8)
                                                                                    )




                                                                            pygame.display.update()
                                                                            time.sleep(0.02)
                                                                    if pat == 3:
                                                                        if dash == "up":
                                                                            for i in range(16):
                                                                                time.sleep(0.001)
                                                                                ofy -= 8
                                                                                for row in range(7):
                                                                                    for col in range(7):
                                                                                        cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                        pygame.draw.rect(window, cem,
                                                                                                         (col * 64 - ofx,
                                                                                                          row * 64 - ofy,
                                                                                                          64, 64))
                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            PLAYER,
                                                                                            (px - 64 // 4, py - 64 // 4,
                                                                                             64 // 2, 64 // 2)
                                                                                        )
                                                                                        for enemy in enemies:
                                                                                            if enemy[2] > 0:
                                                                                                pygame.draw.rect(
                                                                                                    window,
                                                                                                    (0, 255, 0),
                                                                                                    (enemy[0] * 64 - 16,
                                                                                                     enemy[1] * 64 - 16, 32,
                                                                                                     32)
                                                                                                )
                                                                                            enemy[1] += 1 / 392
                                                                                        pygame.display.update()
                                                                        elif dash == "left":
                                                                            for i in range(16):
                                                                                time.sleep(0.001)
                                                                                ofx -= 8
                                                                                for row in range(7):
                                                                                    for col in range(7):
                                                                                        cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                        pygame.draw.rect(window, cem,
                                                                                                         (col * 64 - ofx,
                                                                                                          row * 64 - ofy,
                                                                                                          64, 64))
                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            PLAYER,
                                                                                            (px - 64 // 4, py - 64 // 4,
                                                                                             64 // 2, 64 // 2)
                                                                                        )
                                                                                        for enemy in enemies:
                                                                                            if enemy[2] > 0:
                                                                                                pygame.draw.rect(
                                                                                                    window,
                                                                                                    (0, 255, 0),
                                                                                                    (enemy[0] * 64 - 16,
                                                                                                     enemy[1] * 64 - 16, 32,
                                                                                                     32)
                                                                                                )
                                                                                            enemy[0] += 1 / 392
                                                                                        pygame.display.update()
                                                                        elif dash == "right":
                                                                            for i in range(16):
                                                                                time.sleep(0.001)
                                                                                ofx += 8
                                                                                for row in range(7):
                                                                                    for col in range(7):
                                                                                        cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                        pygame.draw.rect(window, cem,
                                                                                                         (col * 64 - ofx,
                                                                                                          row * 64 - ofy,
                                                                                                          64, 64))
                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            PLAYER,
                                                                                            (px - 64 // 4, py - 64 // 4,
                                                                                             64 // 2, 64 // 2)
                                                                                        )
                                                                                        for enemy in enemies:
                                                                                            if enemy[2] > 0:
                                                                                                pygame.draw.rect(
                                                                                                    window,
                                                                                                    (0, 255, 0),
                                                                                                    (enemy[0] * 64 - 16,
                                                                                                     enemy[1] * 64 - 16, 32,
                                                                                                     32)
                                                                                                )
                                                                                            enemy[0] -= 1 / 392
                                                                                        pygame.display.update()
                                                                        elif dash == "down":
                                                                            for i in range(16):
                                                                                time.sleep(0.01)
                                                                                ofy += 8
                                                                                for row in range(7):
                                                                                    for col in range(7):
                                                                                        cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                        pygame.draw.rect(window, cem,
                                                                                                         (col * 64 - ofx,
                                                                                                          row * 64 - ofy,
                                                                                                          64, 64))
                                                                                        pygame.draw.rect(
                                                                                            window,
                                                                                            PLAYER,
                                                                                            (px - 64 // 4, py - 64 // 4,
                                                                                             64 // 2, 64 // 2)
                                                                                        )
                                                                                        for enemy in enemies:
                                                                                            if enemy[2] > 0:
                                                                                                pygame.draw.rect(
                                                                                                    window,
                                                                                                    (0, 255, 0),
                                                                                                    (enemy[0] * 64 - 16,
                                                                                                     enemy[1] * 64 - 16, 32,
                                                                                                     32)
                                                                                                )
                                                                                            enemy[1] -= 1 / 392
                                                                                        pygame.display.update()
                                                                        dash = 0
                                                                        ofx = 32
                                                                        ofy = 32
                                                                    time.sleep(0.1)


                                                            if event.type == pygame.KEYDOWN:
                                                                if event.key == pygame.K_1:
                                                                    for i in need:
                                                                        if inv[i] >= 1:
                                                                            pat = 1
                                                                if event.key == pygame.K_2:
                                                                    for i in range(1, len(need)):
                                                                        if inv[need[i]] >= 1:
                                                                            pat = 2
                                                                if event.key == pygame.K_3:
                                                                    for i in range(2, len(need)):
                                                                        if inv[need[i]] >= 1:
                                                                            pat = 3
                                                                if event.key == pygame.K_5:
                                                                    if inv[list.index("Gun")] != 0:
                                                                        pat = 4
                                                                if event.key == pygame.K_6:
                                                                    mode = 0
                                                                    pygame.mixer.Sound(
                                                                        resource_path("assets/sounds/open.wav")).play()



                                                                if event.key == pygame.K_w:
                                                                    if turn > 0:
                                                                        turn -= 1
                                                                        for i in range(8):
                                                                            time.sleep(0.01)
                                                                            ofy -= 8
                                                                            for row in range(7):
                                                                                for col in range(7):
                                                                                    cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                    pygame.draw.rect(window, cem,
                                                                                                     (col * 64 - ofx, row * 64 - ofy,
                                                                                                      64, 64))
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        PLAYER,
                                                                                        (px - 64 // 4, py - 64 // 4, 64 // 2, 64 // 2)
                                                                                    )
                                                                                    for enemy in enemies:
                                                                                        if enemy[2] > 0:
                                                                                            pygame.draw.rect(
                                                                                                window,
                                                                                                (0, 255, 0),
                                                                                                (enemy[0] * 64 -16, enemy[1] * 64 -16, 32, 32)
                                                                                            )
                                                                                        enemy[1] += 1/392
                                                                                    pygame.display.update()
                                                                        if ld == 0:
                                                                            ld = 1
                                                                        else:
                                                                            ld = 0
                                                                        ofy = 32
                                                                elif event.key == pygame.K_s:
                                                                    if turn > 0:
                                                                        turn -= 1
                                                                        for i in range(8):
                                                                            time.sleep(0.01)
                                                                            ofy += 8
                                                                            for row in range(7):
                                                                                for col in range(7):
                                                                                    cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                    pygame.draw.rect(window, cem,
                                                                                                     (col * 64 - ofx, row * 64 - ofy,
                                                                                                      64, 64))
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        PLAYER,
                                                                                        (px - 64 // 4, py - 64 // 4, 64 // 2, 64 // 2)
                                                                                    )
                                                                                    for enemy in enemies:
                                                                                        if enemy[2] > 0:
                                                                                            pygame.draw.rect(
                                                                                                window,
                                                                                                (0, 255, 0),
                                                                                                (enemy[0] * 64 -16, enemy[1] * 64 -16, 32, 32)
                                                                                            )
                                                                                        enemy[1] -= 1 / 392
                                                                                    pygame.display.update()
                                                                        if ld == 0:
                                                                            ld = 1
                                                                        else:
                                                                            ld = 0
                                                                        ofy = 32
                                                                elif event.key == pygame.K_a:
                                                                    if turn > 0:
                                                                        turn -= 1
                                                                        for i in range(8):
                                                                            time.sleep(0.01)
                                                                            ofx -= 8
                                                                            for row in range(7):
                                                                                for col in range(7):
                                                                                    cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                    pygame.draw.rect(window, cem,
                                                                                                     (col * 64 - ofx, row * 64 - ofy,
                                                                                                      64, 64))
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        PLAYER,
                                                                                        (px - 64 // 4, py - 64 // 4, 64 // 2, 64 // 2)
                                                                                    )
                                                                                    for enemy in enemies:
                                                                                        if enemy[2] > 0:
                                                                                            pygame.draw.rect(
                                                                                                window,
                                                                                                (0, 255, 0),
                                                                                                (enemy[0] * 64 -16, enemy[1] * 64 -16, 32, 32)
                                                                                            )
                                                                                        enemy[0] += 1 / 392
                                                                                    pygame.display.update()
                                                                        if ld == 0:
                                                                            ld = 1
                                                                        else:
                                                                            ld = 0
                                                                        ofx = 32
                                                                elif event.key == pygame.K_d:
                                                                    if turn > 0:
                                                                        turn -= 1
                                                                        for i in range(8):
                                                                            time.sleep(0.01)
                                                                            ofx += 8
                                                                            for row in range(7):
                                                                                for col in range(7):
                                                                                    cem = LIGHT if (row + col) % 2 == ld else DARK
                                                                                    pygame.draw.rect(window, cem,
                                                                                                     (col * 64 - ofx, row * 64 - ofy,
                                                                                                      64, 64))
                                                                                    pygame.draw.rect(
                                                                                        window,
                                                                                        PLAYER,
                                                                                        (px - 64 // 4, py - 64 // 4, 64 // 2, 64 // 2)
                                                                                    )
                                                                                    for enemy in enemies:
                                                                                        if enemy[2] > 0:
                                                                                            pygame.draw.rect(
                                                                                                window,
                                                                                                (0, 255, 0),
                                                                                                (enemy[0] * 64 -16, enemy[1] * 64 -16, 32, 32)
                                                                                            )
                                                                                        enemy[0] -= 1 / 392
                                                                                    pygame.display.update()
                                                                        if ld == 0:
                                                                            ld = 1
                                                                        else:
                                                                            ld = 0
                                                                        ofx = 32


                                                    window.fill(BG)
                                                    atk = []
                                                    rects = []
                                                    mx, my = pygame.mouse.get_pos()
                                                    mx, my = (mx + 32)// 64, (my + 32)// 64
                                                    for row in range(7):
                                                        for col in range(7):
                                                            cem = LIGHT if (row + col) % 2 == ld else DARK
                                                            pygame.draw.rect(window, cem, (col * 64 - ofx, row * 64 - ofy,
                                                                                           64, 64))
                                                    if pat == 2:
                                                        atk = [[[2, 2], [3, 2], [4, 2]], [[4, 2], [4, 3], [4, 4]],
                                                               [[4, 4], [3, 4], [2, 4]], [[2, 4], [2, 3], [2, 2]],
                                                               [[2, 3], [2, 2], [3, 2]],
                                                               [[3, 2], [4, 2], [4, 3]], [[4, 3], [4, 4], [3, 4]],
                                                               [[3, 4], [2, 4], [2, 3]]]
                                                        for dam in atk:
                                                            if dam[1][0] == mx and dam[1][1] == my:
                                                                atk = dam
                                                    elif pat == 1:
                                                        atk = [[[2, 2]], [[3, 2]], [[4, 2]], [[4, 3]], [[4, 4]], [[3, 4]], [[2, 4]], [[2, 3]]]
                                                        for dam in atk:
                                                            if dam[0][0] == mx and dam[0][1] == my:
                                                                atk = dam
                                                    elif pat == 3:
                                                        atk = [[[3, 2], [3, 1]], [[4, 3], [5, 3]], [[2, 3], [1, 3]],
                                                               [[3, 4], [3, 5]]]
                                                        for dam in atk:
                                                            for q in dam:
                                                                if q[0] == mx and q[1] == my:
                                                                    atk = [[3, 3], dam[0], dam[1]]
                                                    elif pat == 4:
                                                        atk = [[[3, 2], [3, 1], [3, 0]], [[2, 3], [1, 3], [0, 3]],
                                                               [[3, 4], [3, 5], [3, 6]], [[4, 3], [5, 3], [6, 3]]]

                                                        for dam in atk:
                                                            for q in dam:
                                                                if q[0] == mx and q[1] == my:
                                                                    atk = dam
                                                                    try:
                                                                        targetimg = pygame.transform.rotate(targetimg, 5)
                                                                    except NameError:
                                                                        targetimg = pygame.transform.rotate(target, 5)
                                                                    targetr = targetimg.get_rect(center=((mx * 64), (my * 64)))
                                                                    window.blit(targetimg, targetr)
                                                    for dam in atk:
                                                        try:
                                                            int(dam[0])
                                                        except TypeError:
                                                            break
                                                        else:
                                                            trans = pygame.Surface((64, 64), pygame.SRCALPHA)
                                                            trans.fill((168, 27, 27, 100))
                                                            window.blit(trans, ((dam[0] - 1) * 64 + 32, (dam[1] - 1) * 64 + 32))
                                                    pygame.draw.rect(
                                                        window,
                                                        PLAYER,
                                                        (px - 64 // 4, py - 64 // 4, 64 // 2, 64 // 2)
                                                    )
                                                    x = 0

                                                    for enemy in enemies:
                                                        if enemy[2] > 0:
                                                            pygame.draw.rect(
                                                                window,
                                                                (0, 255, 0),
                                                                (enemy[0] * 64 - 16, enemy[1] * 64 - 16, 32, 32)
                                                            )
                                                        else:
                                                            x += 1
                                                    if x == len(enemies):
                                                        time.sleep(2)
                                                        running = False
                                                        print("\n\n\nYou have beaten the game! This game was made by GoldenFright\n"
                                                              "Shoutout to immeteor_ for the artwork❤️ This game would have been incomplete without you\n"
                                                              "But don't worry you probably have not 100% the game. I'll tell you what to do to 100% the game\n"
                                                              f"Have atleast 10 of each item in the game. There are a total of {len(list)} items in the game.\n"
                                                              f"Use these commands if you haven't /smelt, /scroll or /read, /smelt, /use, /earn, /fish, /upgrade, /sell, /shop or /buy")

                                                    pygame.draw.rect(
                                                        window,
                                                        (170, 172, 171),
                                                        (3 * 64 - 36, 3 * 64 -32, 80, 10)
                                                    )
                                                    if health > 10:
                                                        hth = (0, 255, 0)
                                                    else:
                                                        hth= (255, 0, 0)
                                                    pygame.draw.rect(
                                                        window,
                                                        hth,
                                                        (3 * 64 - 36, 3 * 64 - 32, health * 4, 10)
                                                    )
                                                    desc = h.render(
                                                        str(health),
                                                        True,
                                                        (0, 0, 0)
                                                    )
                                                    x = 36
                                                    for i in range(3):
                                                        if pat != i + 1:
                                                            pygame.draw.rect(
                                                                window,
                                                                (70, 45, 25),
                                                                (x, 350, 100, 30)
                                                            )
                                                        else:
                                                            pygame.draw.rect(
                                                                window,
                                                                (60, 30, 20),
                                                                (x, 350, 100, 30)
                                                            )
                                                        rects.append([x, 350, x+100, 380])

                                                        txt = h.render(
                                                            f"{i + 1}",
                                                            True,
                                                            (255, 255, 255)
                                                        )
                                                        window.blit(txt, (x, 355))
                                                        txt = font.render(
                                                            f"{pat_name[i]}",
                                                            True,
                                                            (255, 255, 255)
                                                        )
                                                        window.blit(txt, ((100 - len(pat_name[i]) * 12) / 2 + x, 360))
                                                        for q in range(i, len(need)):
                                                            if inv[need[q]] >= 1:
                                                                lck = 0
                                                                break
                                                            else:
                                                                lck = 1
                                                        if lck == 1:
                                                            window.blit(lock, (x+40, 350))

                                                        x += 110
                                                    x = 36
                                                    for i in ["WASD", "Gun", "Eat"]:
                                                        if i == "Gun" and pat == 4:
                                                            pygame.draw.rect(
                                                                window,
                                                                (60, 30, 20),
                                                                (x, 310, 100, 30)
                                                            )
                                                        else:
                                                            pygame.draw.rect(
                                                                window,
                                                                (70,45,25),
                                                                (x, 310, 100, 30)
                                                            )
                                                        txt = h.render(
                                                            str(["WASD", "Gun", "Eat"].index(i) + 4),
                                                            True,
                                                            (255, 255, 255)
                                                        )
                                                        window.blit(txt, (x, 315))
                                                        txt = font.render(
                                                            i,
                                                            True,
                                                            (255, 255, 255)
                                                        )
                                                        window.blit(txt, ((100 - len(i) * 12) / 2 + x, 320))
                                                        rects.append([x, 310, x + 100, 340])
                                                        x+= 110
                                                    if inv[list.index("Gun")] == 0:
                                                        window.blit(lock, (36 + 110 + 40, 310))

                                                    window.blit(desc, ((3 * 64 - 6), 3 * 64 - 32))
                                                    pygame.display.update()
                                                    clock.tick(60)
                                                    if health <= 0:
                                                        running = False
                                                        print("You died")
                                                else:
                                                    need = [23, 24, 25, 30]
                                                    window.blit(scroll, (0, 0))
                                                    rects = []
                                                    _ = need[mode * 9]
                                                    pygame.draw.rect(
                                                        window,
                                                        (70, 45, 25),
                                                        (40, 330, 50, 50)
                                                    )
                                                    window.blit(left, (40, 330))
                                                    if len(need) > mode * 9 + 9:
                                                        pr = 3
                                                        lst = 3
                                                    else:
                                                        if (len(need) - mode * 9) % 3 == 0:
                                                            pr = (len(need) - mode * 9) / 3
                                                            lst = 3
                                                        else:
                                                            pr = int(str((len(need) - mode * 9) / 3)[0]) + 1
                                                            lst = (len(need) - mode * 9) % 3
                                                    try:
                                                        icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                                    except ValueError:
                                                        icon = sheet.subsurface((0, 0, 1, 1))
                                                    else:
                                                        icon = pygame.transform.scale(icon, (80, 80))
                                                    y = 50
                                                    for i in range(int(pr)):
                                                        x = 36
                                                        if i == pr - 1:
                                                            q = lst
                                                        else:
                                                            q = 3
                                                        for o in range(int(q)):
                                                            pygame.draw.rect(
                                                                window,
                                                                (70, 45, 25),
                                                                (x, y, 100, 100),
                                                                border_radius=10
                                                            )
                                                            window.blit(icon, (x + 10, y + 10))
                                                            rects.append([x, y, x + 100, y + 100])
                                                            txt = h.render(
                                                                list[_],
                                                                True,
                                                                (255, 255, 255)
                                                            )
                                                            window.blit(txt, (x + 5, y + 5))
                                                            txt = font.render(
                                                                f"x{inv[_]}",
                                                                True,
                                                                (255, 255, 255)
                                                            )
                                                            window.blit(txt, (x + 90 - len(str(inv[_])) * 20, y + 80))
                                                            x += 110
                                                            try:
                                                                _ = need[need.index(_) + 1]
                                                            except IndexError:
                                                                pass
                                                            try:
                                                                icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                                            except ValueError:
                                                                icon = sheet.subsurface((0, 0, 1, 1))
                                                            else:
                                                                icon = pygame.transform.scale(icon, (80, 80))

                                                        y += 110
                                                    for event in pygame.event.get():
                                                        if event.type == pygame.MOUSEBUTTONDOWN:
                                                            mx, my = pygame.mouse.get_pos()
                                                            for rec in rects:
                                                                if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                                                    if inv[need[rects.index(rec)]] > 0:
                                                                        inv[need[rects.index(rec)]] -= 1
                                                                        health += 1
                                                                        mode = "play"
                                                                        turn -= 1
                                                            if 40 < mx < 90 and 330 < my < 380:
                                                                mode = "play"
                                                    pygame.display.update()
                                                    clock.tick(60)

                                            pygame.quit()
                                            break
                                        else:
                                            st = 1
                                            if rn.randint(1, 2) == 1:
                                                print("The key slides in but it doesn't turn maybe it isn't "
                                                      "meant for this lock")
                                            else:
                                                print("The key doesn't fit")
                                    else:
                                        print("You leave the place and return empty handed")
                                        break
                                else:
                                    print("Realising there is nothing you can do, you leave the place empty handed")
                                    break
                        else:
                            print("You leave the place as it is but comeback empty handed")


                else:

                    print("you found", choice)
            else:
                balance = balance + choice
                print("you grinded", choice, "🪙 Coins")
        else:
            print("As much as I know☝️🤓️... I don't think you can mine with your bare hands. You need a pickaxe for that")
    elif "dig" in command:
        if inv[35] > 0:
            possible = ["1 Time capsule", "Nothing haha", "4 Earthworm", "Nothing, Bruh", "1 Time capsule", "13 Stone",
                        "7 Stone", "1 Lost key", "Nothing haha", "Nothing. Better Luck Next Time", 690, 211, 10,
                        25, 34, 64, 80, 100, "1 Ore tracker", "1 Info scroll", "1 Info scroll", "1 Use scroll", "1 Use scroll",
                        "1 Smelt scroll", "1 Smelt scroll", "6 Earthworm", "3 Earthworm", "1 Earthworm"]
            choice = rn.choice(possible)
            try:
                int(choice)
            except ValueError:
                if "Nothing" not in choice:
                    c = choice.split(" ")
                    for _ in range(len(list)):
                        if c[1:] == list[_].split(" "):
                            if inv[_] == 0:

                                pygame.init()
                                running = True
                                screen = pygame.display.set_mode((300, 400))
                                clock = pygame.time.Clock()
                                scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
                                scroll = pygame.transform.scale(scroll, (300, 400))
                                sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
                                font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)

                                try:
                                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                except ValueError:
                                    icon = sheet.subsurface((0, 0, 1, 1))
                                else:
                                    icon = pygame.transform.scale(icon, (100, 100))
                                running = True
                                while running:

                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            running = False

                                    screen.blit(scroll, (0, 0))
                                    pygame.draw.rect(
                                        screen,
                                        (70, 45, 25),
                                        (90, 140, 120, 120)
                                    )
                                    screen.blit(icon, (100, 150))
                                    txt = font.render(
                                        "You found a",
                                        True,
                                        (60, 30, 20)
                                    )
                                    screen.blit(txt, (40, 80))
                                    txt = font.render(
                                        "New Item!",
                                        True,
                                        (60, 30, 20)
                                    )
                                    screen.blit(txt, (60, 110))
                                    txt = font.render(
                                        str(list[_]),
                                        True,
                                        (60, 30, 20)
                                    )
                                    screen.blit(txt, ((300 - len(list[_]) * 20) / 2, 270))

                                    pygame.display.update()
                                    clock.tick(60)

                                pygame.quit()
                    add(c[1:], c[0])
                    print("you found", choice)
                else:
                    print("you found", choice)
            else:
                balance = balance + choice
                print("you digged up", choice, "🪙 Coins")
        else:
            print("You need shovel for ts(┬┬﹏┬┬)")

    elif "bal" in command:
        print("You have a total of", balance, " 🪙 Coins")
    elif "sell" in command:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
        click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
        screen = pygame.display.set_mode((500, 600))
        clock = pygame.time.Clock()
        scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
        scroll = pygame.transform.scale(scroll, (500, 600))
        sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
        mode = 0
        _ = 0
        font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
        ttl = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 35)
        name = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
        coin = pygame.image.load(resource_path("assets/coins.png")).convert_alpha()
        nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
        plus = nav.subsurface((0, 0, 10, 10))
        plus = pygame.transform.scale(plus, (30, 30))
        left = nav.subsurface((10, 0, 10, 10))
        left = pygame.transform.scale(left, (30, 30))
        right = nav.subsurface((20, 0, 10, 10))
        right = pygame.transform.scale(right, (30, 30))
        minus = nav.subsurface((30, 0, 10, 10))
        minus = pygame.transform.scale(minus, (30, 30))
        running = True
        need = []
        for _ in range(len(list)):
            if inv[_] > 0:
                need.append(_)
        while running:
            screen.blit(scroll, (0, 0))
            if mode != "amt":
                rects = []
                _ = need[mode * 9]
                if len(need) > mode * 9 + 9:
                    pr = 3
                    lst = 3
                else:
                    if (len(need) - mode * 9) % 3 == 0:
                        pr = (len(need) - mode * 9) / 3
                        lst = 3
                    else:
                        pr = int(str((len(need) - mode * 9) / 3)[0]) + 1
                        lst = (len(need) - mode * 9) % 3
                try:
                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                except ValueError:
                    icon = sheet.subsurface((0, 0, 1, 1))
                else:
                    icon = pygame.transform.scale(icon, (100, 100))
                y = 100
                for i in range(int(pr)):
                    x = 60
                    if i == pr - 1:
                        q = lst
                    else:
                        q = 3
                    for o in range(int(q)):
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (x, y, 120, 120),
                            border_radius=10
                        )
                        screen.blit(icon, (x + 10, y + 10))
                        rects.append([x, y, x + 120, y + 120])
                        txt = name.render(
                            list[_],
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, (x + 5, y + 5))
                        txt = font.render(
                            f"x{inv[_]}",
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, (x + 100 - len(str(inv[_])) * 20, y + 100))
                        x += 130
                        _ += 1
                        while inv[_] == 0:
                            _ += 1
                        try:
                            icon = sheet.subsurface((_ * 32, 0, 32, 32))
                        except ValueError:
                            icon = sheet.subsurface((0, 0, 1, 1))
                        else:
                            icon = pygame.transform.scale(icon, (100, 100))

                    y += 130
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (310, 490, 50, 30),
                )
                screen.blit(right, (320, 490))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (170, 490, 50, 30),
                )
                screen.blit(left, (180, 490))
                val = ttl.render(
                    str(mode + 1),
                    True,
                    (50, 30, 20)
                )
                screen.blit(val, (250, 490))
            else:
                txt = font.render(
                    "How many do you want",
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (50, 80))
                txt = font.render(
                    "to sell?",
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (150, 110))
                txt = ttl.render(
                    str(amt),
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (240, 300))
                screen.blit(icon, (240, 150))
                if amt > 1:
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (180, 300, 30, 30)
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (172, 172, 172),
                        (180, 300, 30, 30)
                    )
                screen.blit(minus, (180, 300))
                if inv[_] != amt:
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (310, 300, 30, 30)
                    )
                else:
                    pygame.draw.rect(
                        screen,
                        (172, 172, 172),
                        (310, 300, 30, 30)
                    )
                screen.blit(plus, (310, 300))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (300, 470, 130, 30)
                )
                txt = font.render(
                    "Confirm",
                    True,
                    (67, 189, 40)
                )
                screen.blit(txt, (305, 480))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (70, 470, 130, 30)
                )
                txt = font.render(
                    "Cancel",
                    True,
                    (168, 27, 27)
                )
                screen.blit(txt, (75, 480))
                txt = ttl.render(
                    str(value[_] * amt),
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (140, 380))
                screen.blit(coin, (160 + len(str(value[_] * amt)) * 35, 380))
                txt = font.render(
                    f"x{inv[_]}",
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (350, 200))
                txt = font.render(
                    "You have",
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (50, 210))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (360, 300, 20 + len(str(inv[_])) * 20, 30)
                )
                txt = font.render(
                    str(inv[_]),
                    True,
                    (255, 255, 255)
                )
                screen.blit(txt, (370, 305))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (120, 300, 40, 30)
                )
                txt = font.render(
                    "1",
                    True,
                    (255, 255, 255)
                )
                screen.blit(txt, (130, 305))

            pygame.display.update()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mode != "amt":
                        for rec in rects:
                            if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                _ = need[rects.index(rec) + mode * 9]
                                mode = "amt"
                                amt = 1
                                click.play()
                                try:
                                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                except ValueError:
                                    icon = sheet.subsurface((0, 0, 1, 1))
                                else:
                                    icon = pygame.transform.scale(icon, (100, 100))
                        if 170 < mx < 220 and 490 < my < 520:
                            if mode > 0:
                                mode -= 1
                        if 310 < mx < 360 and 490 < my < 520:
                            if len(need) > mode * 9 + 9:
                                mode += 1
                    else:
                        if 360 < mx < 420 and 300 < my < 330:
                            amt = inv[_]
                        if 120 < mx < 160 and 300 < my < 330:
                            amt = 1
                        if 310 < mx < 340 and 300 < my < 330:
                            if inv[_] > amt:
                                amt += 1
                        if 180 < mx < 210 and 300 < my < 330:
                            if amt > 1:
                                amt -= 1
                        if 70 < mx < 200 and 470 < my < 500:
                            mode = 0
                        if 300 < mx < 430 and 470 < my < 500:
                            if inv[_] >= amt:
                                balance += value[_] * amt
                                remove(list[_], amt)
                                running = False
                                print(f"You sold {amt}x {list[_]} for {amt * value[_]} 🪙 coins")
        pygame.quit()

    elif "inv" in command:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
        screen = pygame.display.set_mode((500, 600))
        clock = pygame.time.Clock()
        scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
        scroll = pygame.transform.scale(scroll, (500, 600))
        sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
        font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
        smoll = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
        thicc = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 30)
        nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
        left = nav.subsurface((10, 0, 10, 10))
        left = pygame.transform.scale(left, (30, 30))
        right = nav.subsurface((20, 0, 10, 10))
        right = pygame.transform.scale(right, (30, 30))
        mode = 0
        running = True
        need = []
        for _ in range(len(list)):
            if inv[_] > 0:
                need.append(_)
        while running:
            screen.blit(scroll, (0, 0))
            _ = need[mode * 9]
            try:
                icon = sheet.subsurface((_ * 32, 0, 32, 32))
            except ValueError:
                icon = sheet.subsurface((0, 0, 1, 1))
            else:
                pass
            icon = pygame.transform.scale(icon, (100, 100))
            if len(need) >= mode * 9 + 9:
                pr = 3
                lst = 3
            else:
                if (len(need) - mode * 9) % 3 == 0:
                    pr = (len(need) - mode * 9) / 3
                    lst = 3
                else:
                    pr = int(str((len(need) - mode * 9) / 3)[0]) + 1
                    lst = (len(need) - mode * 9) % 3
            y = 90
            for v in range(int(pr)):
                x = 60
                if v == int(pr) - 1:
                    q = lst
                else:
                    q = 3
                for h in range(q):
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (x, y, 120, 120)
                    )
                    screen.blit(icon, (x + 10, y + 10))
                    txt = font.render(
                        f"x{inv[_]}",
                        True,
                        (255, 255, 255)
                    )
                    screen.blit(txt, (x + 100 - len(str(inv[_])) * 20, y + 100))
                    txt = smoll.render(
                        str(list[_]),
                        True,
                        (255, 255, 255)
                    )
                    screen.blit(txt, (x + 5, y + 5))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (150, 490, 50, 30)
                    )
                    screen.blit(left, (160, 490))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (300, 490, 50, 30)
                    )
                    screen.blit(right, (310, 490))
                    txt = thicc.render(
                        str(mode + 1),
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (235, 490))
                    x += 130
                    _ += 1
                    while inv[_] == 0:
                        _ += 1
                    try:
                        icon = sheet.subsurface((_ * 32, 0, 32, 32))
                    except ValueError:
                        icon = sheet.subsurface((0, 0, 1, 1))
                    else:
                        pass
                    icon = pygame.transform.scale(icon, (100, 100))
                y += 130
            pygame.display.update()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if 150 < mx < 200 and 490 < my < 520:
                        if mode > 0:
                            mode -= 1
                    if 300 < mx < 350 and 490 < my < 520:
                        if len(need) > mode * 9 + 9:
                            mode += 1
        pygame.quit()


    elif "upg" in command:
        pygame.init()
        pygame.mixer.init()
        click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
        pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
        screen = pygame.display.set_mode((500, 600))
        clock = pygame.time.Clock()
        scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
        scroll = pygame.transform.scale(scroll, (500, 600))
        coin = pygame.image.load(resource_path("assets/coins.png")).convert_alpha()
        font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
        nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
        plus = nav.subsurface((0, 0, 10, 10))
        plus = pygame.transform.scale(plus, (30, 30))
        left = nav.subsurface((10, 0, 10, 10))
        left = pygame.transform.scale(left, (30, 30))
        right = nav.subsurface((20, 0, 10, 10))
        right = pygame.transform.scale(right, (80, 80))
        minus = nav.subsurface((30, 0, 10, 10))
        minus = pygame.transform.scale(minus, (30, 30))
        sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
        sword = sheet.subsurface((0, 0, 32, 32))
        sword = pygame.transform.scale(sword, (100, 100))
        black_sword = sword.copy()
        black_sword.fill((0, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
        need = [0, 2, 13]
        cutlass = sheet.subsurface(need[1] * 32, 0, 32, 32)
        cutlass = pygame.transform.scale(cutlass, (100, 100))
        black_cutlass = cutlass.copy()
        black_cutlass.fill((0, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
        katana = sheet.subsurface((need[2] * 32, 0, 32, 32))
        katana = pygame.transform.scale(katana, (100, 100))
        black_katana = katana.copy()
        black_katana.fill((0, 0, 0, 255), special_flags=pygame.BLEND_RGBA_MULT)
        mode = 0
        running = True
        while running:
            screen.blit(scroll, (0, 0))
            if mode != "upg":
                rects = []

                _ = need[mode * 6]
                try:
                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                except ValueError:
                    icon = sheet.subsurface((0, 0, 1, 1))
                else:
                    pass
                icon = pygame.transform.scale(icon, (100, 100))
                if len(need) >= mode * 6 + 6:
                    pr = 2
                    lst = 3
                else:
                    if (len(need) - mode * 6) % 3 == 0:
                        pr = (len(need) - mode * 6) / 3
                        lst = 3
                    else:
                        pr = int(str((len(need) - mode * 6) / 3)[0]) + 1
                        lst = (len(need) - mode * 6) % 3
                y = 150
                for v in range(int(pr)):
                    x = 60
                    if v == int(pr) - 1:
                        q = lst
                    else:
                        q = 3
                    for h in range(q):
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (x, y, 120, 120)
                        )
                        screen.blit(icon, (x + 10, y + 10))
                        rects.append([x, y, x+120, y+120])
                        x += 130
                        try:
                            _ = need[int(need.index(_)) + 1]
                        except IndexError:
                            pass
                        try:
                            icon = sheet.subsurface((_ * 32, 0, 32, 32))
                        except ValueError:
                            icon = sheet.subsurface((0, 0, 1, 1))
                        else:
                            pass
                        icon = pygame.transform.scale(icon, (100, 100))

                    y += 200

                txt = font.render(
                    "What do you want to",
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (60, 90))
                txt = font.render(
                    "Upgrade to : ",
                    True,
                    (60, 30, 20)
                )
                screen.blit(txt, (150, 110))
            else:
                y = 100
                if list[_] == "Cutlass":
                    for i in range(3):
                        if inv[need[0]] >= i + 1:
                            screen.blit(sword, (100, y))
                        else:
                            screen.blit(black_sword, (100, y))
                            screen.blit(plus, (150, y + 50))
                        y += 120
                    if inv[need[0]] >= 3:
                        screen.blit(cutlass, (320, 250))

                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (300, 390, 140, 30)
                        )
                        txt = font.render(
                            "Confirm",
                            True,
                            (0, 255, 0)
                        )
                        screen.blit(txt, (310, 395))
                    else:
                        screen.blit(black_cutlass, (320, 250))
                elif list[_] == "Katana":
                    for i in range(3):
                        if inv[need[1]] >= i + 1:
                            screen.blit(cutlass, (100, y))

                        else:
                            screen.blit(black_cutlass, (100, y))
                            screen.blit(plus, (150, y + 50))
                        y += 120
                    if inv[need[1]] >= 3:
                        screen.blit(katana, (320, 250))
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (300, 390, 140, 30)
                        )
                        txt = font.render(
                            "Confirm",
                            True,
                            (0, 255, 0)
                        )
                        screen.blit(txt, (310, 395))
                    else:
                        screen.blit(black_katana, (320, 250))
                screen.blit(right, (210, 260))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mode != "upg":
                        for rec in rects:
                            if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                click.play()
                                _ = need[rects.index(rec)]
                                mode = "upg"
                    else:
                        if 300 < mx < 440 and 390 < my < 420:
                            if list[_] == "Cutlass":
                                if inv[0] >= 3:
                                    remove("Sword", 3)
                                    add("Cutlass", "1")
                                    running = False
                                    print("You upgraded 3 Swords to 1 Cutlass")
                            if list[_] == "Katana":
                                if inv[need[1]] >= 3:
                                    remove("Cutlass", 3)
                                    add("Katana", "1")
                                    running = False
                                    print("You upgraded 3 Cutlasses to 1 Katana")

            pygame.display.update()
            clock.tick(60)
        pygame.quit()

    elif "help" in command:
        print(
            "There are a few commands you can use :- \n/grind           --> Gives you tools and weapons \n/mine            --> You dive into the depth of a cave to find "
            "ores and minerals (requires a pickaxe)\n/dig             -->You dig up someone's backyard! But it may give some .... Items (requires a shovel)\n/sell            --> Sell"
            " Items in your inventory \n/balance         --> Lets you check how much money you have \n/inv             --> shows your inventory"
            "\n/shop or /buy    --> Allows you to buy a set list of items (requires info scrolls)\n/fish            --> You to find fishes in the ocean (requires a fishing rod)\n"
            "/scroll or /read --> You read the scrolls you have\n/info           --> Gives infos of items (requires info scroll to turn page)")
    elif "use" in command:
        if inv[20] > 0:
            p = 0
            if inv[8] > 0:
                print(f"You have {inv[8]} Time capsules")
            else:
                print("You don't have any Time Capsules")
                p += 1
            if inv[12] > 0:
                print(f"You have {inv[12]} Ore trackers")
            else:
                print("You don't have any Ore trackers")
                p += 1
            if p == 2:
                print("You don't have a usable item!")
            else:
                sell = input("What do you want to use? : ")
                amt = (input("How much do you want to use? : "))
                if amt.isnumeric():
                    amt = int(amt)
                else:
                    print("You gay bro? Type a number")
                    amt = int(input("How much do you want to use? : "))
                if "re" in sell:
                    if input(f"Are you sure you want to use {amt} Ore trackers to get better ores when mining? : ") == "yes" \
                            and inv[12] >= amt:
                        remove("Ore tracker", amt)
                        of += 3 * amt
                    else:
                        print("Don't worry the item wasn't used")
                elif "cap" in sell or "ime" in sell:
                    if input(
                            f"Are you sure you want to use {amt} Time capsules to get the last item(not money) you got? : ") == "yes" \
                            and inv[8] >= amt:
                        remove("Time capsule", amt)
                        for _ in range(amt):
                            try:
                                add(c[1:], c[0])
                            except NameError:
                                add("Time capsule", "1")
                                print("You have to find something now to get it again. use /help for commands")
                            else:
                                print(f"You used the time capsule to revert time and got {int(c[0])} {c[1:]}")
                    else:
                        print("Don't worry the item wasn't used / You don't have it")
                else:
                    print("Bro what is that? Use /use again")
        else:
            print("You need a use scroll for that")
    elif "info" in command:
        mode = 0
        if inv[14] > 0:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
            click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
            running = True
            screen = pygame.display.set_mode((500, 600))
            clock = pygame.time.Clock()
            scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
            scroll = pygame.transform.scale(scroll, (500, 600))
            sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
            font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 22)
            desc = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 18)
            ifo = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 18)
            name = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
            nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
            left = nav.subsurface((10, 0, 10, 10))
            left = pygame.transform.scale(left, (30, 30))
            right = nav.subsurface((20, 0, 10, 10))
            right = pygame.transform.scale(right, (30, 30))

            coin = pygame.image.load(resource_path("assets/coins.png")).convert_alpha()
            while running:
                if mode != "info":
                    rects = []
                    _ = 9 * mode


                    try:
                        icon = sheet.subsurface((_ * 32, 0, 32, 32))
                    except ValueError:
                        icon = sheet.subsurface((0, 0, 1, 1))
                    else:
                        icon = pygame.transform.scale(icon, (100, 100))
                    if len(list) > mode * 9 + 9:
                        pr = 3
                        lst = 3
                    else:
                        if (len(list) - mode * 9) % 3 == 0:
                            pr = (len(list) - mode * 9) / 3
                            lst = 3
                        else:
                            pr = int(str((len(list) - mode * 9) / 3)[0]) + 1
                            lst = (len(list) - mode * 9) % 3
                    y = 100
                    for i in range(int(pr)):
                        x = 60
                        if i == pr - 1:
                            q = lst
                        else:
                            q = 3
                        for o in range(int(q)):
                            pygame.draw.rect(
                                screen,
                                (70, 45, 25),
                                (x, y, 120, 120),
                                border_radius=10
                            )
                            screen.blit(icon, (x + 10, y + 10))
                            rects.append([x, y, x + 120, y + 120])
                            txt = name.render(
                                list[_],
                                True,
                                (255, 255, 255)
                            )
                            screen.blit(txt, (x+5, y+5))
                            x += 130
                            _ += 1
                            try:
                                icon = sheet.subsurface((_ * 32, 0, 32, 32))
                            except ValueError:
                                icon = sheet.subsurface((0, 0, 1, 1))
                            else:
                                icon = pygame.transform.scale(icon, (100, 100))

                        y += 130
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (300, 490, 50, 30),
                    )
                    screen.blit(right, (310, 490))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (200, 490, 50, 30),
                    )
                    screen.blit(left, (210, 490))
                    val = font.render(
                        str(mode + 1),
                        True,
                        (50, 30, 20)
                    )
                    screen.blit(val, (265, 490))
                    pygame.display.update()


                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if mode != "info":
                            mx, my = pygame.mouse.get_pos()
                            if 300 < mx < 350 and 490 < 520:
                                if inv[14] > mode + 1 and mode * 9 + 1 <= len(list):
                                    mode += 1
                            if 200 < mx < 250 and 490 < 520 and mode > 0:
                                mode -= 1
                            for rec in rects:
                                if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                    click.play()
                                    _ = mode * 9 + rects.index(rec)
                                    mode = "info"
                                    sell = list[_]
                                    wrapped = textwrap.wrap(f"{info[_]}. This can be found by using {loc[_]}", width=20)
                                    try:
                                        icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                    except ValueError:
                                        icon = sheet.subsurface((0, 0, 1, 1))
                                    else:
                                        icon = pygame.transform.scale(icon, (100, 100))


                screen.blit(scroll, (0, 0))
                if mode == "info":
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (70, 90, 120, 120),
                        border_radius=10
                    )
                    screen.blit(icon, (80, 100))
                    title = font.render(
                        sell.capitalize(),
                        True,
                        (60, 30, 20)
                    )

                    screen.blit(title, (200, 130))
                    rty = desc.render(
                        rarity[_],
                        True,
                        color[rarity[_]]
                    )
                    y = 230
                    screen.blit(rty, (240, 180))
                    for line in wrapped:
                        det = ifo.render(
                            line,
                            True,
                            (60, 30, 20)
                        )
                        screen.blit(det, (55, y))
                        y += 30
                    val = ifo.render(
                        f"Sell value : {value[_]}",
                        True,
                        (60, 30, 20),
                    )
                    screen.blit(val, (50, 500))
                    screen.blit(coin, (380, 490))
                if mode == "info":
                    pygame.display.update()

                clock.tick(60)

            pygame.quit()

        else:
            print("You need info scrolls to get info about items")

    elif "melt" in command:
        if inv[19] > 0:
            pygame.init()
            pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
            pygame.mixer.init()
            click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
            screen = pygame.display.set_mode((500, 600))
            need = []
            for _ in list:
                if "ore" in _:
                    need.append(list.index(_))
            if ore != 0:
                smelted = min(
                    int((time.time() - exp_time) / 6),
                    inv[ore],
                    inv[list.index("Coal")] * 9
                )
                if smelted > 0:
                    remove(list[ore], smelted)
                    add(list[ore].split(" ")[0],str(smelted))
                    remove("Coal",(smelted + 8) // 9)
                    exp_time += smelted * 6
            clock = pygame.time.Clock()
            scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
            scroll = pygame.transform.scale(scroll, (500, 600))
            sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
            mode = 0
            _ = 0
            font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
            ttl = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 35)
            name = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
            coin = pygame.image.load(resource_path("assets/coins.png")).convert_alpha()
            nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
            fire = pygame.image.load(resource_path("assets/fire.png")).convert_alpha()
            plus = nav.subsurface((0, 0, 10, 10))
            plus = pygame.transform.scale(plus, (30, 30))
            left = nav.subsurface((10, 0, 10, 10))
            left = pygame.transform.scale(left, (30, 30))
            right = nav.subsurface((20, 0, 10, 10))
            right = pygame.transform.scale(right, (30, 30))
            minus = nav.subsurface((30, 0, 10, 10))
            minus = pygame.transform.scale(minus, (30, 30))
            running = True
            while running:
                screen.blit(scroll, (0, 0))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (190, 240, 120, 120),
                    border_radius = 10
                )
                if ore != 0:
                    screen.blit(pygame.transform.scale(sheet.subsurface((ore * 32, 0, 32, 32)), (100, 100)), (200, 250))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (190, 400, 120, 120),
                    border_radius=10
                )
                screen.blit(pygame.transform.scale(sheet.subsurface((list.index("Coal") * 32, 0, 32, 32)), (100, 100)), (200, 410))
                txt = font.render(
                    f"x{inv[list.index('Coal')]}",
                    True,
                    (255, 255, 255)
                )
                screen.blit(txt, (300 - len(str(inv[list.index('Coal')])) * 20, 510))
                icon = fire.subsurface(((9 - state) * 32, 0, 32, 32))
                icon = pygame.transform.scale(icon, (100, 100))
                screen.blit(icon, (90, 320))
                if state > 0 and time.time() >= exp_time:
                    if inv[ore] > 0:
                        remove(list[ore], 1)
                        add(list[ore].split(" ")[0], "1")
                        state -= 1
                        exp_time = time.time() + 3
                        if state == 0 and inv[list.index("Coal")] > 0:
                            state = 9
                            remove("Coal", 1)
                rects = []
                _ = need[mode * 9]
                if len(need) > mode * 9 + 9:
                    pr = 3
                    lst = 3
                else:
                    if (len(need) - mode * 9) % 3 == 0:
                        pr = (len(need) - mode * 9) / 3
                        lst = 3
                    else:
                        pr = int(str((len(need) - mode * 9) / 3)[0]) + 1
                        lst = (len(need) - mode * 9) % 3
                try:
                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                except ValueError:
                    icon = sheet.subsurface((0, 0, 1, 1))
                else:
                    icon = pygame.transform.scale(icon, (100, 100))
                y = 100
                for i in range(int(pr)):
                    x = 60
                    if i == pr - 1:
                        q = lst
                    else:
                        q = 3
                    for o in range(int(q)):
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (x, y, 120, 120),
                            border_radius=10
                        )
                        screen.blit(icon, (x + 10, y + 10))
                        rects.append([x, y, x + 120, y + 120])
                        txt = name.render(
                            list[_],
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, (x + 5, y + 5))
                        txt = font.render(
                            f"x{inv[_]}",
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, ((x + 80) - len(str(inv[list.index('Coal')])) * 20, y + 100))
                        x += 130
                        try:
                            _ = need[need.index(_) + 1]
                        except IndexError:
                            pass
                        try:
                            icon = sheet.subsurface((_ * 32, 0, 32, 32))
                        except ValueError:
                            icon = sheet.subsurface((0, 0, 1, 1))
                        else:
                            icon = pygame.transform.scale(icon, (100, 100))

                    y += 130
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        for rec in rects:
                            if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                click.play()
                                ore = need[mode * 6 + rects.index(rec)]
                                if inv[list.index("Coal")] > 0:
                                    exp_time = time.time() + 3
                                    if state == 0:
                                        state = 9
                                        remove("Coal", 1)
                pygame.display.update()
                clock.tick(60)
            pygame.quit()

        else:
            print("You need a smelt scroll for that")
    elif "scroll" in command or "read" in command:
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
        click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
        screen = pygame.display.set_mode((500, 600))
        clock = pygame.time.Clock()
        scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
        scroll = pygame.transform.scale(scroll, (500, 600))
        sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
        mode = 0
        _ = 0
        font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
        ttl = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 35)
        name = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
        coin = pygame.image.load(resource_path("assets/coins.png")).convert_alpha()
        nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
        plus = nav.subsurface((0, 0, 10, 10))
        plus = pygame.transform.scale(plus, (30, 30))
        left = nav.subsurface((10, 0, 10, 10))
        left = pygame.transform.scale(left, (30, 30))
        right = nav.subsurface((20, 0, 10, 10))
        right = pygame.transform.scale(right, (30, 30))
        minus = nav.subsurface((30, 0, 10, 10))
        minus = pygame.transform.scale(minus, (30, 30))
        running = True
        need = []
        for _ in range(len(list)):
            if "scroll" in list[_] and inv[_] > 0:
                need.append(_)
        if len(need) != 0:
            running = True
        else:
            print("You don't have any scrolls to read")
        while running:
            screen.blit(scroll, (0, 0))
            if mode != "read":
                rects = []
                _ = need[mode * 9]
                if len(need) > mode * 9 + 9:
                    pr = 3
                    lst = 3
                else:
                    if (len(need) - mode * 9) % 3 == 0:
                        pr = (len(need) - mode * 9) / 3
                        lst = 3
                    else:
                        pr = int(str((len(need) - mode * 9) / 3)[0]) + 1
                        lst = (len(need) - mode * 9) % 3
                try:
                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                except ValueError:
                    icon = sheet.subsurface((0, 0, 1, 1))
                else:
                    icon = pygame.transform.scale(icon, (100, 100))
                y = 100
                for i in range(int(pr)):
                    x = 60
                    if i == pr - 1:
                        q = lst
                    else:
                        q = 3
                    for o in range(int(q)):
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (x, y, 120, 120),
                            border_radius=10
                        )
                        screen.blit(icon, (x + 10, y + 10))
                        rects.append([x, y, x + 120, y + 120])
                        txt = name.render(
                            list[_],
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, (x+5, y+5))
                        try:
                            _ = need[need.index(_) + 1]
                        except IndexError:
                            pass
                        try:
                            icon = sheet.subsurface((_ * 32, 0, 32, 32))
                        except ValueError:
                            icon = sheet.subsurface((0, 0, 1, 1))
                        else:
                            icon = pygame.transform.scale(icon, (100, 100))
                        x += 130
                    y += 130

            else:
                try:
                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                except ValueError:
                    icon = sheet.subsurface((0, 0, 1, 1))
                else:
                    icon = pygame.transform.scale(icon, (100, 100))
                pygame.draw.rect(
                    screen,
                    (70,45,25),
                    (60, 100, 120, 120),
                    border_radius=10
                )
                screen.blit(icon, (65, 110))
                wrapped = textwrap.wrap(list[_], 9)
                y = 100
                for line in wrapped:
                    txt = ttl.render(
                        line,
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (200, y))
                    y += 40
                txt = font.render(
                    rarity[_],
                    True,
                    color[rarity[_]]
                )
                screen.blit(txt, (420 - len(rarity[_] * 20), 200 + (len(list[_].split(" ")) - 2) * 25))
                if list[_] != "Ore tracker scroll":
                    wrapped = textwrap.wrap(f"This scroll allow you to use the /{list[_].split(' ')[0]} command", 20)
                else:
                    wrapped = textwrap.wrap(f"There lies a dungeon in the depth of the mines but the only way to get there is by the powers of the Ore Tracker.", 20)
                y = 250
                for line in wrapped:
                    txt = font.render(
                        line,
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (70, y))
                    y += 30
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    if mode != "read":
                        for rec in rects:
                            if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                click.play()
                                _ = need[rects.index(rec)]
                                mode = "read"
            pygame.display.update()
            clock.tick(60)
        pygame.quit()



    elif "buy" in command or "shop" in command:
        if inv[list.index("Info scroll")] > 0:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
            click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
            need = [6, 8, 9, 11, 12, 21, 35, 22, 23, 24, 25, 28, 30]
            screen = pygame.display.set_mode((500, 600))
            clock = pygame.time.Clock()
            scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
            scroll = pygame.transform.scale(scroll, (500, 600))
            sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
            mode = 0
            _ = 0
            font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
            ttl = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 35)
            name = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
            coin = pygame.image.load(resource_path("assets/coins.png")).convert_alpha()
            nav = pygame.image.load(resource_path("assets/nav.png")).convert_alpha()
            plus = nav.subsurface((0, 0, 10, 10))
            plus = pygame.transform.scale(plus, (30, 30))
            left = nav.subsurface((10, 0, 10, 10))
            left = pygame.transform.scale(left, (30, 30))
            right = nav.subsurface((20, 0, 10, 10))
            right = pygame.transform.scale(right, (30, 30))
            minus = nav.subsurface((30, 0, 10, 10))
            minus = pygame.transform.scale(minus, (30, 30))
            running = True
            while running:
                screen.blit(scroll, (0, 0))
                if mode != "amt":
                    rects = []
                    _ = need[mode * 6]
                    try:
                        icon = sheet.subsurface((_ * 32, 0, 32, 32))
                    except ValueError:
                        icon = sheet.subsurface((0, 0, 1, 1))
                    else:
                        icon = pygame.transform.scale(icon, (100, 100))
                    if len(need) >= mode * 6 + 6:
                        pr = 3
                        lst = 2
                    else:
                        if (len(need) - mode * 6) % 2 == 0:
                            pr = (len(need) - mode * 6) / 2
                            lst = 2
                        else:
                            pr = int(str((len(need) - mode * 6) / 2)[0]) + 1
                            lst = (len(need) - mode * 6) % 2
                    y = 90
                    for v in range(int(pr)):
                        x = 100
                        if v == int(pr) - 1:
                            q = lst
                        else:
                            q = 2
                        for h in range(q):
                            pygame.draw.rect(
                                screen,
                                (70, 45, 25),
                                (x, y, 120, 120),
                                border_radius=10
                            )
                            screen.blit(icon, (x + 10, y + 10))
                            rects.append([x, y, x + 120, y + 120])
                            txt = name.render(
                                list[_],
                                True,
                                (255, 255, 255)
                            )
                            screen.blit(txt, (x+5, y+5))
                            x += 190
                            try:
                                _ = need[need.index(_) + 1]
                            except IndexError:
                                pass
                            try:
                                icon = sheet.subsurface((_ * 32, 0, 32, 32))
                            except ValueError:
                                icon = sheet.subsurface((0, 0, 1, 1))
                            else:
                                icon = pygame.transform.scale(icon, (100, 100))

                        y += 130
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (310, 490, 50, 30),
                    )
                    screen.blit(right, (320, 490))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (170, 490, 50, 30),
                    )
                    screen.blit(left, (180, 490))
                    val = ttl.render(
                        str(mode + 1),
                        True,
                        (50, 30, 20)
                    )
                    screen.blit(val, (250, 490))
                else:
                    txt = font.render(
                        "How many do you want",
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (50, 80))
                    txt = font.render(
                        "to buy?",
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (150, 110))
                    txt = ttl.render(
                        str(amt),
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (240, 300))
                    screen.blit(icon, (240, 150))
                    if amt > 0:
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (180, 300, 30, 30)
                        )
                    else:
                        pygame.draw.rect(
                            screen,
                            (172, 172, 172),
                            (180, 300, 30, 30)
                        )
                    screen.blit(minus, (180, 300))
                    if balance > int((amt + 1) * value[_] * 5 / 4):
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (310, 300, 30, 30)
                        )
                    else:
                        pygame.draw.rect(
                            screen,
                            (172, 172, 172),
                            (310, 300, 30, 30)
                        )
                    screen.blit(plus, (310, 300))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (300, 470, 130, 30)
                    )
                    txt = font.render(
                        "Confirm",
                        True,
                        (67, 189, 40)
                    )
                    screen.blit(txt, (305, 480))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (70, 470, 130, 30)
                    )
                    txt = font.render(
                        "Cancel",
                        True,
                        (168, 27, 27)
                    )
                    screen.blit(txt, (75, 480))
                    txt = ttl.render(
                        str(int(amt * value[_] * 5 / 4)),
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (140, 380))
                    screen.blit(coin, (160 + len(str(value[_] * amt)) * 35, 380))
                    txt = font.render(
                        f"{balance}",
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(coin, (350 + len(str(value[_] * amt)) * 20, 190))
                    screen.blit(txt, (350, 200))
                    txt = font.render(
                        "You have",
                        True,
                        (60, 30, 20)
                    )
                    screen.blit(txt, (50, 210))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (360, 300, 60, 30)
                    )
                    txt = font.render(
                        "+10",
                        True,
                        (255, 255, 255)
                    )
                    screen.blit(txt, (360, 305))
                    pygame.draw.rect(
                        screen,
                        (70, 45, 25),
                        (120, 300, 40, 30)
                    )
                    txt = font.render(
                        "1",
                        True,
                        (255, 255, 255)
                    )
                    screen.blit(txt, (130, 305))

                pygame.display.update()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        if mode != "amt":
                            for rec in rects:
                                if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                    _ = need[mode * 6 +rects.index(rec)]
                                    click.play()
                                    mode = "amt"
                                    amt = 0
                                    try:
                                        icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                    except ValueError:
                                        icon = sheet.subsurface((0, 0, 1, 1))
                                    else:
                                        icon = pygame.transform.scale(icon, (100, 100))
                            if 170 < mx < 220 and 490 < my < 520:
                                if mode > 0:
                                    mode -= 1
                            if 310 < mx < 360 and 490 < my < 520:
                                if len(need) > mode * 6 + 6 and inv[list.index("Info scroll")] > mode + 1:
                                    mode += 1
                        else:
                            if 360 < mx < 420 and 300 < my < 330:
                                if balance > int((amt + 10) * value[_] * 5 / 4):
                                    amt += 10
                            if 120 < mx < 160 and 300 < my < 330:
                                amt = 0
                            if 310 < mx < 340 and 300 < my < 330:
                                if balance > int((amt + 1) * value[_] * 5 / 4):
                                    amt += 1
                            if 180 < mx < 210 and 300 < my < 330:
                                if amt > 0:
                                    amt -= 1
                            if 70 < mx < 200 and 470 < my < 500:
                                mode = 0
                            if 300 < mx < 430 and 470 < my < 500:
                                if value[_] != 0:
                                    balance -= int(amt * value[_] * 5 / 4)
                                    add(list[_], str(amt))
                                    running = False
                                    print(f"You bought {amt}x {list[_]} for {int(amt * value[_] * 5 / 4)} 🪙 coins")
            pygame.quit()
        else:
            print("You need info scrolls to buy as well")
    elif "fi" in command:
        if inv[21] > 0:
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.Sound(resource_path("assets/sounds/open.wav")).play()
            click = pygame.mixer.Sound(resource_path("assets/sounds/select.wav"))
            screen = pygame.display.set_mode((500, 600))
            clock = pygame.time.Clock()
            scroll = pygame.image.load(resource_path("assets/scroll.png")).convert_alpha()
            scroll = pygame.transform.scale(scroll, (500, 600))
            need = [list.index("Earthworm"), 28, 23, 24, 25, 30]
            font = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 20)
            sheet = pygame.image.load(resource_path("assets/Sheet.png")).convert_alpha()
            name = pygame.font.Font(resource_path("assets/PressStart2P-Regular.ttf"), 10)
            mode = 0
            running = True
            while running:
                _ = need[0]
                rects = []
                screen.blit(scroll, (0, 0))
                pygame.draw.rect(
                    screen,
                    (70, 45, 25),
                    (170, 495, 150, 30)
                )
                txt = font.render(
                    "Nothing",
                    True,
                    (255, 255, 255)
                )
                screen.blit(txt, (175, 500))

                try:
                    icon = sheet.subsurface((_ * 32, 0, 32, 32))
                except ValueError:
                    icon = sheet.subsurface((0, 0, 1, 1))
                else:
                    pass
                icon = pygame.transform.scale(icon, (100, 100))
                if len(need) >= mode * 9 + 9:
                    pr = 3
                    lst = 3
                else:
                    if (len(need) - mode * 9) % 3 == 0:
                        pr = (len(need) - mode * 9) / 3
                        lst = 3
                    else:
                        pr = int(str((len(need) - mode * 9) / 3)[0]) + 1
                        lst = (len(need) - mode * 9) % 3
                y = 90
                for v in range(int(pr)):
                    x = 60
                    if v == int(pr) - 1:
                        q = lst
                    else:
                        q = 3
                    for h in range(q):
                        pygame.draw.rect(
                            screen,
                            (70, 45, 25),
                            (x, y, 120, 120)
                        )
                        screen.blit(icon, (x+10, y+10))
                        txt = name.render(
                            list[_],
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, (x+5, y+5))
                        txt = font.render(
                            f"x{inv[_]}",
                            True,
                            (255, 255, 255)
                        )
                        screen.blit(txt, (x + 100 - len(str(inv[_])) * 20, y + 100))

                        try:
                            _ = need[need.index(_) + 1]
                        except IndexError:
                            pass
                        try:
                            icon = sheet.subsurface((_ * 32, 0, 32, 32))
                        except ValueError:
                            icon = sheet.subsurface((0, 0, 1, 1))
                        else:
                            icon = pygame.transform.scale(icon, (100, 100))
                        rects.append([x, y, x + 120, y + 120])
                        x += 130
                    y += 130
                pygame.display.update()
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mx, my = pygame.mouse.get_pos()
                        for rec in rects:
                            if rec[0] < mx < rec[2] and rec[1] < my < rec[3]:
                                click.play()
                                _ = need[rects.index(rec)]
                                running = False
                                possible = "no"
                                if inv[_] > 0:
                                    remove(list[_], 1)
                                    if list[_] == "Earthworm":
                                        possible = ["1 Salmon", "1 Salmon", "1 Cod", "1 Cod", "1 Tuna", "Nothing! But make sure to support our art dev immeteor_❤️", "1 Lost key",
                                                    "1 Catfish", "1 Shrimp"]
                                    elif list[_] in ["Salmon", "Cod", "Catfish"]:
                                        possible = ["Nothing! But make sure to support our art dev immeteor_❤️", "1 Lost key", "1 Piranha", "1 Piranha", "1 Piranha", "1 Toothed whale",
                                                    "1 Great white", "1 Piranha", "Nothing! But make sure to support our art dev immeteor_❤️ LoL", "Nothing Lmao", "1 Stingray", "1 Stingray", "2 Lost key",
                                                    "1 Shark tooth", "1 Shark tooth"]
                                    elif list[_] == "Tuna":
                                        possible = ["Nothing! But make sure to support our art dev immeteor_❤️", "1 Lost key", "1 Lost key", "1 Great white", "1 Toothed whale", "1 Toothed whale",
                                                    "Nothing! But make sure to support our art dev immeteor_❤️ You didn't even see movement", "2 Shark tooth", "1 Shark tooth", "1 Shark tooth", "1 Stingray",
                                                    "1 Stingray", "1 Stingray"]
                                    elif list[_] == "Shrimp":
                                        possible = ["1 Salmon", "1 Salmon", "1 Cod", "1 Cod", "1 Tuna", "Nothing! But make sure to support our art dev immeteor_❤️", "1 Lost key",
                                                    "1 Catfish", "1 Stingray", "1 Tuna", "1 Catfish", "1 Stingray"]
                                else:
                                    print("You don't have that")
                                    possible = "no"
                        if 170 < mx < 320 and 495 < my < 525:
                            click.play()
                            possible = ["1 Shark tooth", "1 Boot", "1 Boot", "1 Shrimp", "1 Cod", "1 Salmon", "Nothing! But make sure to support our art dev immeteor_❤️ haha",
                                        "Nothing. But make sure to support our art dev immeteor_❤️", "Nothing but remember to support our art dev immeteor_❤️"]
                            running = False


            pygame.quit()
            try:
                choice = rn.choice(possible)
            except NameError:
                pass
            else:
                if possible != "no":
                    try:
                        choice = int(choice)
                    except ValueError:
                        if "Nothing" not in choice:
                            c = choice.split(" ")
                            for _ in range(len(list)):
                                if c[1:] == list[_].split(" "):
                                    if inv[_] == 0:

                                        pygame.init()
                                        running = True
                                        screen = pygame.display.set_mode((300, 400))
                                        clock = pygame.time.Clock()
                                        scroll = pygame.image.load(
                                            resource_path("assets/scroll.png")).convert_alpha()
                                        scroll = pygame.transform.scale(scroll, (300, 400))
                                        sheet = pygame.image.load(
                                            resource_path("assets/Sheet.png")).convert_alpha()
                                        font = pygame.font.Font(
                                            resource_path("assets/PressStart2P-Regular.ttf"), 20)

                                        try:
                                            icon = sheet.subsurface((_ * 32, 0, 32, 32))
                                        except ValueError:
                                            icon = sheet.subsurface((0, 0, 1, 1))
                                        else:
                                            icon = pygame.transform.scale(icon, (100, 100))
                                        running = True
                                        while running:

                                            for event in pygame.event.get():
                                                if event.type == pygame.QUIT:
                                                    running = False

                                            screen.blit(scroll, (0, 0))
                                            pygame.draw.rect(
                                                screen,
                                                (70, 45, 25),
                                                (90, 140, 120, 120)
                                            )
                                            screen.blit(icon, (100, 150))
                                            txt = font.render(
                                                "You found a",
                                                True,
                                                (60, 30, 20)
                                            )
                                            screen.blit(txt, (40, 80))
                                            txt = font.render(
                                                "New Item!",
                                                True,
                                                (60, 30, 20)
                                            )
                                            screen.blit(txt, (60, 110))
                                            txt = font.render(
                                                str(list[_]),
                                                True,
                                                (60, 30, 20)
                                            )
                                            screen.blit(txt, ((300 - len(list[_]) * 20) / 2, 270))

                                            pygame.display.update()
                                            clock.tick(60)

                                        pygame.quit()
                            print("you fished", "x", choice)
                            add(c[1:], c[0])
                        else:
                            print("you fished", choice)
                    else:
                        balance = balance + choice
                        print("you fished", choice, "🪙 Coins")
        else:
            print("Bro thinks he is him🥀 You ain't catching no fish without no fishing rod.")

    else:
        print("Use /help . That is not a command")

    file.seek(0)
    file.truncate()
    for _ in range(len(list)):
        file.write(str(len(str(inv[_]))) + str(inv[_]))
    file.write(f"\n{str(balance)}")
    file.write(f"\n{str(of)}")
    try:
        file.write(f"\n{ore}")
    except NameError:
        pass
    else:
        file.write(f"\n{state}")
        if exp_time == 0:
            file.write(f"\n0.0")
        else:
            file.write(f"\n{exp_time}")
    file.flush()
# pyinstaller --onefile --add-data "assets;assets" main.py
