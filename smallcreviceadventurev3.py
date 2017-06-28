# Get functions
from functions import *

print("~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~")
print("~SMALL CREVICE ADVENTURE~~~~~~~~~~~~~_________~~~~~~~~~~~~~~~~~")
print("~VERSION BETA~~~~~~~~~~~~~~~~~~~~~~~/~~~~~~~~~\~~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|^^^^^^^^~|~~~~~~~~~~~~~~~~")
print("~2017~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~||        |~\~~~~~~~~~~~~~~")
print("~PYTHON VERSION~~~~~~~~~~~~~~~~~~~~/~|       |~|~~~~~~~~~~~~~~~")
print("~~~~~~~~~~~~CREATED BY ATTICUS BHAT AND LINUS SKUCAS~~~~~~~~~~~")
print("~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~o~")
import time
print("blimey! you have fallen into a small crevice! you see that the crevice spits into a left and right passage.")
cave_choice = getinput()

if cave_choice is "L" or cave_choice is"LEFT":
  print("you enter the left cave. the walls are slightly damp and there are numerous stalactites on the ceiling.")
  time.sleep(1)
  print("there is also a small pool in the middle of the room. the pool feeds to an underground river.")
  time.sleep(1)
  print("there is a small boat at the edge of the pool.")
  time.sleep(1)
  print("there is also another passage leading off to the left.")
  time.sleep(1)
  print("do you get in the boat, swim down the river, or take the passage?")
  river_choice =  getinput()

  if river_choice is "W" or river_choice is "WALK":
    print("you walk to the passage and start down it.")
    time.sleep(1)
    print("you come into a beautiful cavern containing a shimmering waterfall.")
    time.sleep(1)
    print("there is a large chasm at the far end of the room.")
    time.sleep(1)
    print("there is a rope bridge across the chasm at the far end of the cavern.")
    time.sleep(1)
    print("there is a skinny stone bridge leading across the chasm, much closer to you than the rope bridge, which looks pretty unsafe.")
    time.sleep(1)
    print("there is a river leading away from the pool under the waterfall, which leads into a dark passage.")
    time.sleep(1)
    print("do you take the rope bridge, the stone bridge, or the river tunnel?")
    waterfall_choice = getinput("put R for the rope bridge, S for the stone, or T for the river tunnel.")

    if waterfall_choice is "R" or waterfall_choice is "ROPE":
      print("you start across the rope bridge. it sways in the slight breeze blowing up from the chasm.")
      time.sleep(1)
      print("afler several minutes of careful crawling, you reach the other side of the chasm.")
      print("you see a passage leading up, a passage leading down, and a passage going straight.")
      print("do you take the upper passage, the lower passage, or the middle passage?")
      chasm_choice = getinput()

      if chasm_choice is "U" or chasm_choice is "UP":
        print("")

      elif chasm_choice is "L" or chasm_choice is "LOW":
        print("")

      elif chasm_choice is "M" or chasm_choice is "MIDDLE":
        print("")

    elif waterfall_choice is "S" or waterfall_choice is "STONE":
      print("you start walking across the stone bridge.")
      time.sleep(2)
      print("you see a glow deep in the chasm, lighting the sides of the walls.")
      time.sleep(1)
      print("you hear drumbeats deep, deep down in the chasm.")
      time.sleep(1)
      print("a shadowy figure appears at the far end of the bridge.")
      print("congradulations! you have found a balrog!!")
      print("the balrog instantly smashes you to pieces with his fire whip! you have died!")
      
    elif waterfall_choice is "T" or waterfall_choice is "TUNNEL":
      print("you start down the tunnel, which begins to slope up.")
      time.sleep(1)
      print("you find that your path is blocked by a large snake with many heads! the snake quickly devours you!")
      print("GAME OVER :(")

    else:
      print("you turn sideways and walk into the cave's wall. the impact causes a stalactite to fall on your head.")
      print("GAME OVER :(")


  elif river_choice is "B" or river_choice is "BOAT":
    print("you walk to the boat and hop in. the boat starts drifting into darkness.")
    time.sleep(1)
    print("you come into a large cavern containing many stalacitites.")
    print("there are diamonds here!")
    time.sleep(1)
    print("there is also a large dragon here!")
    time.sleep(1)
    print("the dragon quickly toasts you to a crisp!")
    print("GAME OVER!! YOU LOSE!! :(")

  elif river_choice is "S" or river_choice is "SWIM":
    print("you dive into the water, which is pleasantly warm, and swim into darkness.")
    time.sleep(1)
    print("suddenly, you are devoured by a hungry shark!")
    print("GAME OVER!! :(")
  else:
      print("you turn sideways and walk into the cave's wall. the impact causes a stalactite to fall on your head.")
      print("GAME OVER :(")

elif cave_choice is "R" or cave_choice is "RIGHT":
  print("you walk into the right passage. it begins to slope downward.")
  time.sleep(1)
  print("you see a rope ladder leading down into a dark pit.")
  time.sleep(1)
  print("there is also a passage leading to the left.")
  time.sleep(1)
  print("do you climb down or keep walking?")
  pit_choice = getinput("put C to climb or W to  walk.")

  if pit_choice is "C" or pit_choice is "CLIMB":
    print("you climb down the ladder and into darkness.")
    time.sleep(1)

  elif pit_choice is "W" or pit_choice is "WALK":
    print("you start walking down the left passage. it slopes down at a 53-degree angle.")
    time.sleep(1)
    print("you come into a beautiful cavern containing a shimmering waterfall.")
    time.sleep(1)
    print("there is a large chasm at the far end of the room.")
    time.sleep(1)
    print("there is a rope bridge across the chasm at the far end of the cavern.")
    time.sleep(1)
    print("there is a skinny stone bridge leading across the chasm, much closer to you than the rope bridge, which looks pretty unsafe.")
    time.sleep(1)
    print("there is a river leading away from the pool under the waterfall, which leads into a dark passage.")
    time.sleep(1)
    print("do you take the rope bridge, the stone bridge, or the river tunnel?")
    waterfall_choice = getinput("put R for the rope bridge, S for the stone, or T for the river tunnel.")

    if waterfall_choice is "R" or waterfall_choice is "ROPE":
      print("you start across the rope bridge. it sways in the slight breeze blowing up from the chasm.")
      time.sleep(1)
      print("afler several minutes of careful crawling, you reach the other side of the chasm.")
      print("you see a passage leading up, a passage leading down, and a passage going straight.")
      print("do you take the upper passage, the lower passage, or the middle passage?")
      chasm_choice = getinput()

      if chasm_choice is "U" or chasm_choice is "UP":
        print("you walk up the upper passage.")
        time.sleep(1)
        print("there is a dwarf in the room with you!")
        print("he throws an axe at you!")
        print("he misses, and the axe magically flies back to his hand,")
        print("he runs back through the passage from whence he came.")

      elif chasm_choice is "L" or chasm_choice is "LOW":
        print("")

      elif chasm_choice is "M" or chasm_choice is "MIDDLE":
        print("")

    elif waterfall_choice is "S" or waterfall_choice is "STONE":
      print("you start walking across the stone bridge.")
      time.sleep(2)
      print("you see a glow deep in the chasm, lighting the sides of the walls.")
      time.sleep(1)
      print("you hear drumbeats deep, deep down in the chasm.")
      time.sleep(1)
      print("a shadowy figure appears at the far end of the bridge.")
      print("congradulations! you have found a balrog!!")
      print("the balrog instantly smashes you to pieces with his fire whip! you have died!")
      
    elif waterfall_choice is "T" or waterfall_choice is "TUNNEL":
      print("you start down the tunnel, which begins to slope up.")
      time.sleep(1)
      print("you find that your path is blocked by a large snake with many heads! the snake quickly devours you!")
      print("GAME OVER :(")

    else:
      print("you turn sideways and walk into the cave's wall. the impact causes a stalactite to fall on your head.")
      print("GAME OVER :(")


  else:
    print("you turn sideways and walk into the cave's wall. the impact causes a stalactite to fall on your head.")
    print("GAME OVER :(")

else:
    print("you turn sideways and walk into the cave's wall. the impact causes a stalactite to fall on your head.")
    print("GAME OVER :(")
