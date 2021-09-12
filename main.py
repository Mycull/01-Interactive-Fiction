import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"

world = {
  "uuid": "9BD60891-83E8-4CCF-9ED1-A98D881D79CF",
  "name": "Rare Art Museum Heist",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631411109825,
  "passages": [
    {
      "name": "South of Museum",
      "tags": "",
      "id": "1",
      "text": "You are getting ready to steal some expensive art from the Green Moss Museum. You patiently waited several meters away from the museum. Your mission is to steal one treasure from each of the exhibits and steal enough to pay back your debt to the mafia.\n\n[[Continue->Entrance of Museum]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "Entrance of Museum",
          "original": "[[Continue->Entrance of Museum]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are getting ready to steal some expensive art from the Green Moss Museum. You patiently waited several meters away from the museum. Your mission is to steal once treasure from each of the exhibits and steal enough to pay back your debt to the mafia."
    },
    {
      "name": "Entrance of Museum",
      "tags": "",
      "id": "2",
      "text": "You sneak up to the Entrance of the Museum. The sign reads \"Green Moss Museum\" and there is a guard standing outside of the entrance, what will you do?\n\n[[ATTACK->Ending 1]]\n[[DISTRACTION->Inside of Museum]]\n[[WAIT->Inside of Museum]]",
      "links": [
        {
          "linkText": "ATTACK",
          "passageName": "Ending 1",
          "original": "[[ATTACK->Ending 1]]"
        },
        {
          "linkText": "DISTRACTION",
          "passageName": "Inside of Museum",
          "original": "[[DISTRACTION->Inside of Museum]]"
        },
        {
          "linkText": "WAIT",
          "passageName": "Inside of Museum",
          "original": "[[WAIT->Inside of Museum]]"
        }
      ],
      "hooks": [],
      "cleanText": "You sneak up to the Entrance of the Museum. The sign reads \"Green Moss Museum\" and there is a guard standing outside of the entrance, what will you do?"
    },
    {
      "name": "Ending 1",
      "tags": "",
      "id": "3",
      "text": "You run up to the guard in an attempt to take him out, but you are too far away from him to begin with and they pull out their gun and shoot you several times. You fall to the floor and bleed out. GAME OVER!\n\n[[TRY AGAIN->Entrance of Museum]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "Entrance of Museum",
          "original": "[[TRY AGAIN->Entrance of Museum]]"
        }
      ],
      "hooks": [],
      "cleanText": "You run up to the guard in an attempt to take him out, but you are too far away from him to begin with and they pull out their gun and shoot you several times. You fall to the floor and bleed out. GAME OVER!"
    },
    {
      "name": "Inside of Museum",
      "tags": "",
      "id": "4",
      "text": "You are inside of the museum, you glance all around to see beautiful art pieces and sculptures on display. There are three hallways in front of you, which hallway do you choose?\n\n[[SCIENCE HALL->Science Hall]]\n[[EGYPTIAN HALL->Egyptian Hall]]\n[[RENAISSANCE HALL->Renaissance Hall]]",
      "links": [
        {
          "linkText": "SCIENCE HALL",
          "passageName": "Science Hall",
          "original": "[[SCIENCE HALL->Science Hall]]"
        },
        {
          "linkText": "EGYPTIAN HALL",
          "passageName": "Egyptian Hall",
          "original": "[[EGYPTIAN HALL->Egyptian Hall]]"
        },
        {
          "linkText": "RENAISSANCE HALL",
          "passageName": "Renaissance Hall",
          "original": "[[RENAISSANCE HALL->Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You are inside of the museum, you glance all around to see beautiful art pieces and sculptures on display. There are three hallways in front of you, which hallway do you choose?"
    },
    {
      "name": "Science Hall",
      "tags": "",
      "id": "5",
      "text": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?\n\n[[PARKOUR ON DISPLAYS->Ending 2]]\n[[DISGUISE AS ROBOT->Science Security Room]]",
      "links": [
        {
          "linkText": "PARKOUR ON DISPLAYS",
          "passageName": "Ending 2",
          "original": "[[PARKOUR ON DISPLAYS->Ending 2]]"
        },
        {
          "linkText": "DISGUISE AS ROBOT",
          "passageName": "Science Security Room",
          "original": "[[DISGUISE AS ROBOT->Science Security Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?"
    },
    {
      "name": "Egyptian Hall",
      "tags": "",
      "id": "6",
      "text": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?\n\n[[FIND THE SOURCE->Pharaoh's Room]]\n[[LEAVE->Ending 3]]",
      "links": [
        {
          "linkText": "FIND THE SOURCE",
          "passageName": "Pharaoh's Room",
          "original": "[[FIND THE SOURCE->Pharaoh's Room]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Ending 3",
          "original": "[[LEAVE->Ending 3]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?"
    },
    {
      "name": "Renaissance Hall",
      "tags": "",
      "id": "7",
      "text": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?\n\n[[HELP THE KING->King's Request]]\n[[DON'T HELP->King's Punishment]]",
      "links": [
        {
          "linkText": "HELP THE KING",
          "passageName": "King's Request",
          "original": "[[HELP THE KING->King's Request]]"
        },
        {
          "linkText": "DON'T HELP",
          "passageName": "King's Punishment",
          "original": "[[DON'T HELP->King's Punishment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?"
    },
    {
      "name": "Ending 2",
      "tags": "",
      "id": "8",
      "text": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!\n\n[[TRY AGAIN->Science Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "Science Hall",
          "original": "[[TRY AGAIN->Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!"
    },
    {
      "name": "Science Security Room",
      "tags": "",
      "id": "9",
      "text": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?\n\n[[EXPERIMENTAL ORBITAL BEAM RAYGUN->Experiment Raygun]]\n[[SKULL OF NEIL ARMSTRONG->Skull of Neil]]\n[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->Ghost Punching Gloves]]",
      "links": [
        {
          "linkText": "EXPERIMENTAL ORBITAL BEAM RAYGUN",
          "passageName": "Experiment Raygun",
          "original": "[[EXPERIMENTAL ORBITAL BEAM RAYGUN->Experiment Raygun]]"
        },
        {
          "linkText": "SKULL OF NEIL ARMSTRONG",
          "passageName": "Skull of Neil",
          "original": "[[SKULL OF NEIL ARMSTRONG->Skull of Neil]]"
        },
        {
          "linkText": "BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS",
          "passageName": "Ghost Punching Gloves",
          "original": "[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->Ghost Punching Gloves]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?"
    },
    {
      "name": "Experiment Raygun",
      "tags": "",
      "id": "10",
      "text": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall\n\n[[CONTINUE->(S)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(S)Main Hall",
          "original": "[[CONTINUE->(S)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall"
    },
    {
      "name": "Skull of Neil",
      "tags": "",
      "id": "11",
      "text": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall.\n\n[[CONTINUE->(S)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(S)Main Hall",
          "original": "[[CONTINUE->(S)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall."
    },
    {
      "name": "Ghost Punching Gloves",
      "tags": "",
      "id": "12",
      "text": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall.\n\n[[CONTINUE->(S)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(S)Main Hall",
          "original": "[[CONTINUE->(S)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall."
    },
    {
      "name": "(S)Main Hall",
      "tags": "",
      "id": "13",
      "text": "You have two more halls left to explore.\n\n[[EGYPTIAN HALL->(S)Egyptian Hall]]\n[[RENAISANCE HALL->(S)Renaissance Hall]]",
      "links": [
        {
          "linkText": "EGYPTIAN HALL",
          "passageName": "(S)Egyptian Hall",
          "original": "[[EGYPTIAN HALL->(S)Egyptian Hall]]"
        },
        {
          "linkText": "RENAISANCE HALL",
          "passageName": "(S)Renaissance Hall",
          "original": "[[RENAISANCE HALL->(S)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have two more halls left to explore."
    },
    {
      "name": "Pharaoh's Room",
      "tags": "",
      "id": "14",
      "text": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?\n\n[[TELL HIM YOU'RE HIS MOTHER->Mother]]\n[[BEAT HIM UP->WWE SMACKDOWN]]",
      "links": [
        {
          "linkText": "TELL HIM YOU'RE HIS MOTHER",
          "passageName": "Mother",
          "original": "[[TELL HIM YOU'RE HIS MOTHER->Mother]]"
        },
        {
          "linkText": "BEAT HIM UP",
          "passageName": "WWE SMACKDOWN",
          "original": "[[BEAT HIM UP->WWE SMACKDOWN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?"
    },
    {
      "name": "Ending 3",
      "tags": "",
      "id": "15",
      "text": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!\n\n[[TRY AGAIN->Egyptian Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "Egyptian Hall",
          "original": "[[TRY AGAIN->Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!"
    },
    {
      "name": "Mother",
      "tags": "",
      "id": "16",
      "text": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm.\n\n[[CONTINUE->Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "Pharaoh's Treasure",
          "original": "[[CONTINUE->Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm."
    },
    {
      "name": "WWE SMACKDOWN",
      "tags": "",
      "id": "17",
      "text": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm.\n\n[[Continue->Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "Pharaoh's Treasure",
          "original": "[[Continue->Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm."
    },
    {
      "name": "Pharaoh's Treasure",
      "tags": "",
      "id": "18",
      "text": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?\n\n[[24K SOLID GOLD ANKH WITH DIAMONDS->Ankh]]\n[[CURSED FINGER OF THE PHARAOH->Cursed Finger]]\n[[MAGIC STAFF THAT CAN MOVE SAND->Magic Staff]]",
      "links": [
        {
          "linkText": "24K SOLID GOLD ANKH WITH DIAMONDS",
          "passageName": "Ankh",
          "original": "[[24K SOLID GOLD ANKH WITH DIAMONDS->Ankh]]"
        },
        {
          "linkText": "CURSED FINGER OF THE PHARAOH",
          "passageName": "Cursed Finger",
          "original": "[[CURSED FINGER OF THE PHARAOH->Cursed Finger]]"
        },
        {
          "linkText": "MAGIC STAFF THAT CAN MOVE SAND",
          "passageName": "Magic Staff",
          "original": "[[MAGIC STAFF THAT CAN MOVE SAND->Magic Staff]]"
        }
      ],
      "hooks": [],
      "cleanText": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?"
    },
    {
      "name": "Ankh",
      "tags": "",
      "id": "19",
      "text": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(E)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(E)Main Hall",
          "original": "[[CONTINUE->(E)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "Cursed Finger",
      "tags": "",
      "id": "20",
      "text": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall.\n\n[[Continue->(E)Main Hall]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(E)Main Hall",
          "original": "[[Continue->(E)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "Magic Staff",
      "tags": "",
      "id": "21",
      "text": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(E)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(E)Main Hall",
          "original": "[[CONTINUE->(E)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(E)Main Hall",
      "tags": "",
      "id": "22",
      "text": "You have two more halls left to explore.\n\n[[SCIENCE HALL->(E)Science Hall]] \n[[RENAISANCE HALL->(E)Renaissance Hall]]",
      "links": [
        {
          "linkText": "SCIENCE HALL",
          "passageName": "(E)Science Hall",
          "original": "[[SCIENCE HALL->(E)Science Hall]]"
        },
        {
          "linkText": "RENAISANCE HALL",
          "passageName": "(E)Renaissance Hall",
          "original": "[[RENAISANCE HALL->(E)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have two more halls left to explore."
    },
    {
      "name": "(S)Egyptian Hall",
      "tags": "",
      "id": "23",
      "text": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?\n\n[[FIND THE SOURCE->(S)Pharaoh's Room]]\n[[LEAVE->(S)Ending 3]]",
      "links": [
        {
          "linkText": "FIND THE SOURCE",
          "passageName": "(S)Pharaoh's Room",
          "original": "[[FIND THE SOURCE->(S)Pharaoh's Room]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "(S)Ending 3",
          "original": "[[LEAVE->(S)Ending 3]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?"
    },
    {
      "name": "(S)Renaissance Hall",
      "tags": "",
      "id": "24",
      "text": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?\n\n[[HELP THE KING->(S)King's Request]]\n[[DON'T HELP->(S)King's Punishment]]",
      "links": [
        {
          "linkText": "HELP THE KING",
          "passageName": "(S)King's Request",
          "original": "[[HELP THE KING->(S)King's Request]]"
        },
        {
          "linkText": "DON'T HELP",
          "passageName": "(S)King's Punishment",
          "original": "[[DON'T HELP->(S)King's Punishment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?"
    },
    {
      "name": "(S)Pharaoh's Room",
      "tags": "",
      "id": "25",
      "text": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?\n\n[[TELL HIM YOU'RE HIS MOTHER->(S)Mother]]\n[[BEAT HIM UP->(S)WWE SMACKDOWN]]",
      "links": [
        {
          "linkText": "TELL HIM YOU'RE HIS MOTHER",
          "passageName": "(S)Mother",
          "original": "[[TELL HIM YOU'RE HIS MOTHER->(S)Mother]]"
        },
        {
          "linkText": "BEAT HIM UP",
          "passageName": "(S)WWE SMACKDOWN",
          "original": "[[BEAT HIM UP->(S)WWE SMACKDOWN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?"
    },
    {
      "name": "(S)Ending 3",
      "tags": "",
      "id": "26",
      "text": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!\n\n[[TRY AGAIN->(S)Egyptian Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(S)Egyptian Hall",
          "original": "[[TRY AGAIN->(S)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!"
    },
    {
      "name": "(S)Mother",
      "tags": "",
      "id": "27",
      "text": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm.\n\n[[CONTINUE->(S)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(S)Pharaoh's Treasure",
          "original": "[[CONTINUE->(S)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm."
    },
    {
      "name": "(S)WWE SMACKDOWN",
      "tags": "",
      "id": "28",
      "text": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm.\n\n[[Continue->(S)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(S)Pharaoh's Treasure",
          "original": "[[Continue->(S)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm."
    },
    {
      "name": "(S)Pharaoh's Treasure",
      "tags": "",
      "id": "29",
      "text": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?\n\n[[24K SOLID GOLD ANKH WITH DIAMONDS->(S)Ankh]]\n[[CURSED FINGER OF THE PHARAOH->(S)Cursed Finger]]\n[[MAGIC STAFF THAT CAN MOVE SAND->(S)Magic Staff]]",
      "links": [
        {
          "linkText": "24K SOLID GOLD ANKH WITH DIAMONDS",
          "passageName": "(S)Ankh",
          "original": "[[24K SOLID GOLD ANKH WITH DIAMONDS->(S)Ankh]]"
        },
        {
          "linkText": "CURSED FINGER OF THE PHARAOH",
          "passageName": "(S)Cursed Finger",
          "original": "[[CURSED FINGER OF THE PHARAOH->(S)Cursed Finger]]"
        },
        {
          "linkText": "MAGIC STAFF THAT CAN MOVE SAND",
          "passageName": "(S)Magic Staff",
          "original": "[[MAGIC STAFF THAT CAN MOVE SAND->(S)Magic Staff]]"
        }
      ],
      "hooks": [],
      "cleanText": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?"
    },
    {
      "name": "(S)Ankh",
      "tags": "",
      "id": "30",
      "text": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(SE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SE)Main Hall",
          "original": "[[CONTINUE->(SE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(S)Cursed Finger",
      "tags": "",
      "id": "31",
      "text": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall.\n\n[[Continue->(SE)Main Hall]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(SE)Main Hall",
          "original": "[[Continue->(SE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(S)Magic Staff",
      "tags": "",
      "id": "32",
      "text": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(SE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SE)Main Hall",
          "original": "[[CONTINUE->(SE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(SE)Main Hall",
      "tags": "",
      "id": "33",
      "text": "There is one hall left to explore.\n\n[[RENAISSANCE HALL->(SE)Renaissance Hall]]",
      "links": [
        {
          "linkText": "RENAISSANCE HALL",
          "passageName": "(SE)Renaissance Hall",
          "original": "[[RENAISSANCE HALL->(SE)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is one hall left to explore."
    },
    {
      "name": "(E)Science Hall",
      "tags": "",
      "id": "34",
      "text": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?\n\n[[PARKOUR ON DISPLAYS->(E)Ending 2]]\n[[DISGUISE AS ROBOT->(E)Science Security Room]]",
      "links": [
        {
          "linkText": "PARKOUR ON DISPLAYS",
          "passageName": "(E)Ending 2",
          "original": "[[PARKOUR ON DISPLAYS->(E)Ending 2]]"
        },
        {
          "linkText": "DISGUISE AS ROBOT",
          "passageName": "(E)Science Security Room",
          "original": "[[DISGUISE AS ROBOT->(E)Science Security Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?"
    },
    {
      "name": "(E)Renaissance Hall",
      "tags": "",
      "id": "35",
      "text": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?\n\n[[HELP THE KING->(E)King's Request]]\n[[DON'T HELP->(E)King's Punishment]]",
      "links": [
        {
          "linkText": "HELP THE KING",
          "passageName": "(E)King's Request",
          "original": "[[HELP THE KING->(E)King's Request]]"
        },
        {
          "linkText": "DON'T HELP",
          "passageName": "(E)King's Punishment",
          "original": "[[DON'T HELP->(E)King's Punishment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?"
    },
    {
      "name": "(E)Ending 2",
      "tags": "",
      "id": "36",
      "text": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!\n\n[[TRY AGAIN->(E)Science Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(E)Science Hall",
          "original": "[[TRY AGAIN->(E)Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!"
    },
    {
      "name": "(E)Science Security Room",
      "tags": "",
      "id": "37",
      "text": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?\n\n[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(E)Experiment Raygun]]\n[[SKULL OF NEIL ARMSTRONG->(E)Skull of Neil]]\n[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(E)Ghost Punching Gloves]]",
      "links": [
        {
          "linkText": "EXPERIMENTAL ORBITAL BEAM RAYGUN",
          "passageName": "(E)Experiment Raygun",
          "original": "[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(E)Experiment Raygun]]"
        },
        {
          "linkText": "SKULL OF NEIL ARMSTRONG",
          "passageName": "(E)Skull of Neil",
          "original": "[[SKULL OF NEIL ARMSTRONG->(E)Skull of Neil]]"
        },
        {
          "linkText": "BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS",
          "passageName": "(E)Ghost Punching Gloves",
          "original": "[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(E)Ghost Punching Gloves]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?"
    },
    {
      "name": "(E)Experiment Raygun",
      "tags": "",
      "id": "38",
      "text": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall\n\n[[CONTINUE->(ES)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ES)Main Hall",
          "original": "[[CONTINUE->(ES)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall"
    },
    {
      "name": "(E)Skull of Neil",
      "tags": "",
      "id": "39",
      "text": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall.\n\n[[CONTINUE->(ES)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ES)Main Hall",
          "original": "[[CONTINUE->(ES)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall."
    },
    {
      "name": "(E)Ghost Punching Gloves",
      "tags": "",
      "id": "40",
      "text": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall.\n\n[[CONTINUE->(ES)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ES)Main Hall",
          "original": "[[CONTINUE->(ES)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall."
    },
    {
      "name": "(ES)Main Hall",
      "tags": "",
      "id": "41",
      "text": "There is one hall left to explore.\n\n[[RENAISSANCE HALL->(ES)Renaissance Hall]]",
      "links": [
        {
          "linkText": "RENAISSANCE HALL",
          "passageName": "(ES)Renaissance Hall",
          "original": "[[RENAISSANCE HALL->(ES)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is one hall left to explore."
    },
    {
      "name": "King's Request",
      "tags": "",
      "id": "42",
      "text": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline.\n\n[[MARRY THE PRINCESS->Marriage]]\n[[DECLINE HIS OFFER->Ending 4]]",
      "links": [
        {
          "linkText": "MARRY THE PRINCESS",
          "passageName": "Marriage",
          "original": "[[MARRY THE PRINCESS->Marriage]]"
        },
        {
          "linkText": "DECLINE HIS OFFER",
          "passageName": "Ending 4",
          "original": "[[DECLINE HIS OFFER->Ending 4]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline."
    },
    {
      "name": "King's Punishment",
      "tags": "",
      "id": "43",
      "text": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever.\n\n[[MARRY HIS DAUGHTER->Marriage]]\n[[LIVE LIFE AS A PRISONER->Ending 5]]",
      "links": [
        {
          "linkText": "MARRY HIS DAUGHTER",
          "passageName": "Marriage",
          "original": "[[MARRY HIS DAUGHTER->Marriage]]"
        },
        {
          "linkText": "LIVE LIFE AS A PRISONER",
          "passageName": "Ending 5",
          "original": "[[LIVE LIFE AS A PRISONER->Ending 5]]"
        }
      ],
      "hooks": [],
      "cleanText": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever."
    },
    {
      "name": "Marriage",
      "tags": "",
      "id": "44",
      "text": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around.\n\n[[TAKE A DRINK->Ending 6]]\n[[TRY TO FIND THE TREASURE ROOM->King's Treasure]]",
      "links": [
        {
          "linkText": "TAKE A DRINK",
          "passageName": "Ending 6",
          "original": "[[TAKE A DRINK->Ending 6]]"
        },
        {
          "linkText": "TRY TO FIND THE TREASURE ROOM",
          "passageName": "King's Treasure",
          "original": "[[TRY TO FIND THE TREASURE ROOM->King's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around."
    },
    {
      "name": "Ending 4",
      "tags": "",
      "id": "45",
      "text": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!\n\n[[TRY AGAIN->Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "Renaissance Hall",
          "original": "[[TRY AGAIN->Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!"
    },
    {
      "name": "Ending 5",
      "tags": "",
      "id": "46",
      "text": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!\n\n[[TRY AGAIN->Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "Renaissance Hall",
          "original": "[[TRY AGAIN->Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!"
    },
    {
      "name": "Ending 6",
      "tags": "",
      "id": "47",
      "text": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!\n\n[[TRY AGAIN->Marriage]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "Marriage",
          "original": "[[TRY AGAIN->Marriage]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!"
    },
    {
      "name": "King's Treasure",
      "tags": "",
      "id": "48",
      "text": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in.\n\n[[THE KING'S SWORD->King's Sword]]\n[[CROWN WITH GIGANTIC GEM->Crown]]\n[[CAPE WITH PORTAL FOR INFINITE STORAGE->Cape]]",
      "links": [
        {
          "linkText": "THE KING'S SWORD",
          "passageName": "King's Sword",
          "original": "[[THE KING'S SWORD->King's Sword]]"
        },
        {
          "linkText": "CROWN WITH GIGANTIC GEM",
          "passageName": "Crown",
          "original": "[[CROWN WITH GIGANTIC GEM->Crown]]"
        },
        {
          "linkText": "CAPE WITH PORTAL FOR INFINITE STORAGE",
          "passageName": "Cape",
          "original": "[[CAPE WITH PORTAL FOR INFINITE STORAGE->Cape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in."
    },
    {
      "name": "King's Sword",
      "tags": "",
      "id": "49",
      "text": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(R)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(R)Main Hall",
          "original": "[[CONTINUE->(R)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "Crown",
      "tags": "",
      "id": "50",
      "text": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(R)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(R)Main Hall",
          "original": "[[CONTINUE->(R)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "Cape",
      "tags": "",
      "id": "51",
      "text": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(R)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(R)Main Hall",
          "original": "[[CONTINUE->(R)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(R)Main Hall",
      "tags": "",
      "id": "52",
      "text": "You have two more halls left to explore.\n\n[[SCIENCE HALL->(R)Science Hall]] \n[[EGYPTIAN HALL->(R)Egyptian Hall]]",
      "links": [
        {
          "linkText": "SCIENCE HALL",
          "passageName": "(R)Science Hall",
          "original": "[[SCIENCE HALL->(R)Science Hall]]"
        },
        {
          "linkText": "EGYPTIAN HALL",
          "passageName": "(R)Egyptian Hall",
          "original": "[[EGYPTIAN HALL->(R)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have two more halls left to explore."
    },
    {
      "name": "(R)Science Hall",
      "tags": "",
      "id": "53",
      "text": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?\n\n[[PARKOUR ON DISPLAYS->(R)Ending 2]]\n[[DISGUISE AS ROBOT->(R)Science Security Room]]",
      "links": [
        {
          "linkText": "PARKOUR ON DISPLAYS",
          "passageName": "(R)Ending 2",
          "original": "[[PARKOUR ON DISPLAYS->(R)Ending 2]]"
        },
        {
          "linkText": "DISGUISE AS ROBOT",
          "passageName": "(R)Science Security Room",
          "original": "[[DISGUISE AS ROBOT->(R)Science Security Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?"
    },
    {
      "name": "(R)Egyptian Hall",
      "tags": "",
      "id": "54",
      "text": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?\n\n[[FIND THE SOURCE->(R)Pharaoh's Room]]\n[[LEAVE->(R)Ending 3]]",
      "links": [
        {
          "linkText": "FIND THE SOURCE",
          "passageName": "(R)Pharaoh's Room",
          "original": "[[FIND THE SOURCE->(R)Pharaoh's Room]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "(R)Ending 3",
          "original": "[[LEAVE->(R)Ending 3]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?"
    },
    {
      "name": "(SE)Renaissance Hall",
      "tags": "",
      "id": "55",
      "text": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?\n\n[[HELP THE KING->(SE)King's Request]]\n[[DON'T HELP->(SE)King's Punishment]]",
      "links": [
        {
          "linkText": "HELP THE KING",
          "passageName": "(SE)King's Request",
          "original": "[[HELP THE KING->(SE)King's Request]]"
        },
        {
          "linkText": "DON'T HELP",
          "passageName": "(SE)King's Punishment",
          "original": "[[DON'T HELP->(SE)King's Punishment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?"
    },
    {
      "name": "(SE)King's Request",
      "tags": "",
      "id": "56",
      "text": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline.\n\n[[MARRY THE PRINCESS->(SE)Marriage]]\n[[DECLINE HIS OFFER->(SE)Ending 4]]",
      "links": [
        {
          "linkText": "MARRY THE PRINCESS",
          "passageName": "(SE)Marriage",
          "original": "[[MARRY THE PRINCESS->(SE)Marriage]]"
        },
        {
          "linkText": "DECLINE HIS OFFER",
          "passageName": "(SE)Ending 4",
          "original": "[[DECLINE HIS OFFER->(SE)Ending 4]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline."
    },
    {
      "name": "(SE)King's Punishment",
      "tags": "",
      "id": "57",
      "text": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever.\n\n[[MARRY HIS DAUGHTER->(SE)Marriage]]\n[[LIVE LIFE AS A PRISONER->(SE)Ending 5]]",
      "links": [
        {
          "linkText": "MARRY HIS DAUGHTER",
          "passageName": "(SE)Marriage",
          "original": "[[MARRY HIS DAUGHTER->(SE)Marriage]]"
        },
        {
          "linkText": "LIVE LIFE AS A PRISONER",
          "passageName": "(SE)Ending 5",
          "original": "[[LIVE LIFE AS A PRISONER->(SE)Ending 5]]"
        }
      ],
      "hooks": [],
      "cleanText": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever."
    },
    {
      "name": "(SE)Marriage",
      "tags": "",
      "id": "58",
      "text": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around.\n\n[[TAKE A DRINK->(SE)Ending 6]]\n[[TRY TO FIND THE TREASURE ROOM->(SE)King's Treasure]]",
      "links": [
        {
          "linkText": "TAKE A DRINK",
          "passageName": "(SE)Ending 6",
          "original": "[[TAKE A DRINK->(SE)Ending 6]]"
        },
        {
          "linkText": "TRY TO FIND THE TREASURE ROOM",
          "passageName": "(SE)King's Treasure",
          "original": "[[TRY TO FIND THE TREASURE ROOM->(SE)King's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around."
    },
    {
      "name": "(SE)Ending 4",
      "tags": "",
      "id": "59",
      "text": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!\n\n[[TRY AGAIN->(SE)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(SE)Renaissance Hall",
          "original": "[[TRY AGAIN->(SE)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!"
    },
    {
      "name": "(SE)Ending 5",
      "tags": "",
      "id": "60",
      "text": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!\n\n[[TRY AGAIN->(SE)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(SE)Renaissance Hall",
          "original": "[[TRY AGAIN->(SE)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!"
    },
    {
      "name": "(SE)Ending 6",
      "tags": "",
      "id": "61",
      "text": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!\n\n[[TRY AGAIN->(SE)Marriage]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(SE)Marriage",
          "original": "[[TRY AGAIN->(SE)Marriage]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!"
    },
    {
      "name": "(SE)King's Treasure",
      "tags": "",
      "id": "62",
      "text": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in.\n\n[[THE KING'S SWORD->(SE)King's Sword]]\n[[CROWN WITH GIGANTIC GEM->(SE)Crown]]\n[[CAPE WITH PORTAL FOR INFINITE STORAGE->(SE)Cape]]",
      "links": [
        {
          "linkText": "THE KING'S SWORD",
          "passageName": "(SE)King's Sword",
          "original": "[[THE KING'S SWORD->(SE)King's Sword]]"
        },
        {
          "linkText": "CROWN WITH GIGANTIC GEM",
          "passageName": "(SE)Crown",
          "original": "[[CROWN WITH GIGANTIC GEM->(SE)Crown]]"
        },
        {
          "linkText": "CAPE WITH PORTAL FOR INFINITE STORAGE",
          "passageName": "(SE)Cape",
          "original": "[[CAPE WITH PORTAL FOR INFINITE STORAGE->(SE)Cape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in."
    },
    {
      "name": "(SE)King's Sword",
      "tags": "",
      "id": "63",
      "text": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(SER)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SER)Main Hall",
          "original": "[[CONTINUE->(SER)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(SE)Crown",
      "tags": "",
      "id": "64",
      "text": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(SER)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SER)Main Hall",
          "original": "[[CONTINUE->(SER)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(SE)Cape",
      "tags": "",
      "id": "65",
      "text": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(SER)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SER)Main Hall",
          "original": "[[CONTINUE->(SER)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(SER)Main Hall",
      "tags": "",
      "id": "66",
      "text": "You have finally taken one treasure from each hall now time to find out how much money you've made.\n\n[[TOTAL->TOTAL MONEY]]",
      "links": [
        {
          "linkText": "TOTAL",
          "passageName": "TOTAL MONEY",
          "original": "[[TOTAL->TOTAL MONEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have finally taken one treasure from each hall now time to find out how much money you've made."
    },
    {
      "name": "(S)King's Request",
      "tags": "",
      "id": "67",
      "text": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline.\n\n[[MARRY THE PRINCESS->(S)Marriage]]\n[[DECLINE HIS OFFER->(S)Ending 4]]",
      "links": [
        {
          "linkText": "MARRY THE PRINCESS",
          "passageName": "(S)Marriage",
          "original": "[[MARRY THE PRINCESS->(S)Marriage]]"
        },
        {
          "linkText": "DECLINE HIS OFFER",
          "passageName": "(S)Ending 4",
          "original": "[[DECLINE HIS OFFER->(S)Ending 4]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline."
    },
    {
      "name": "(S)King's Punishment",
      "tags": "",
      "id": "68",
      "text": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever.\n\n[[MARRY HIS DAUGHTER->(S)Marriage]]\n[[LIVE LIFE AS A PRISONER->(S)Ending 5]]",
      "links": [
        {
          "linkText": "MARRY HIS DAUGHTER",
          "passageName": "(S)Marriage",
          "original": "[[MARRY HIS DAUGHTER->(S)Marriage]]"
        },
        {
          "linkText": "LIVE LIFE AS A PRISONER",
          "passageName": "(S)Ending 5",
          "original": "[[LIVE LIFE AS A PRISONER->(S)Ending 5]]"
        }
      ],
      "hooks": [],
      "cleanText": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever."
    },
    {
      "name": "(S)Marriage",
      "tags": "",
      "id": "69",
      "text": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around.\n\n[[TAKE A DRINK->(S)Ending 6]]\n[[TRY TO FIND THE TREASURE ROOM->(S)King's Treasure]]",
      "links": [
        {
          "linkText": "TAKE A DRINK",
          "passageName": "(S)Ending 6",
          "original": "[[TAKE A DRINK->(S)Ending 6]]"
        },
        {
          "linkText": "TRY TO FIND THE TREASURE ROOM",
          "passageName": "(S)King's Treasure",
          "original": "[[TRY TO FIND THE TREASURE ROOM->(S)King's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around."
    },
    {
      "name": "(S)Ending 6",
      "tags": "",
      "id": "70",
      "text": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!\n\n[[TRY AGAIN->(S)Marriage]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(S)Marriage",
          "original": "[[TRY AGAIN->(S)Marriage]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!"
    },
    {
      "name": "(S)King's Treasure",
      "tags": "",
      "id": "71",
      "text": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in.\n\n[[THE KING'S SWORD->(S)King's Sword]]\n[[CROWN WITH GIGANTIC GEM->(S)Crown]]\n[[CAPE WITH PORTAL FOR INFINITE STORAGE->(S)Cape]]",
      "links": [
        {
          "linkText": "THE KING'S SWORD",
          "passageName": "(S)King's Sword",
          "original": "[[THE KING'S SWORD->(S)King's Sword]]"
        },
        {
          "linkText": "CROWN WITH GIGANTIC GEM",
          "passageName": "(S)Crown",
          "original": "[[CROWN WITH GIGANTIC GEM->(S)Crown]]"
        },
        {
          "linkText": "CAPE WITH PORTAL FOR INFINITE STORAGE",
          "passageName": "(S)Cape",
          "original": "[[CAPE WITH PORTAL FOR INFINITE STORAGE->(S)Cape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in."
    },
    {
      "name": "(S)King's Sword",
      "tags": "",
      "id": "72",
      "text": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(SR)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SR)Main Hall",
          "original": "[[CONTINUE->(SR)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(S)Crown",
      "tags": "",
      "id": "73",
      "text": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(SR)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SR)Main Hall",
          "original": "[[CONTINUE->(SR)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(S)Cape",
      "tags": "",
      "id": "74",
      "text": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(SR)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SR)Main Hall",
          "original": "[[CONTINUE->(SR)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(SR)Main Hall",
      "tags": "",
      "id": "75",
      "text": "There is one hall left to explore.\n\n[[EGYPTIAN HALL->(SR)Egyptian Hall]]",
      "links": [
        {
          "linkText": "EGYPTIAN HALL",
          "passageName": "(SR)Egyptian Hall",
          "original": "[[EGYPTIAN HALL->(SR)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is one hall left to explore."
    },
    {
      "name": "(SR)Egyptian Hall",
      "tags": "",
      "id": "76",
      "text": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?\n\n[[FIND THE SOURCE->(SR)Pharaoh's Room]]\n[[LEAVE->(SR)Ending 3]]",
      "links": [
        {
          "linkText": "FIND THE SOURCE",
          "passageName": "(SR)Pharaoh's Room",
          "original": "[[FIND THE SOURCE->(SR)Pharaoh's Room]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "(SR)Ending 3",
          "original": "[[LEAVE->(SR)Ending 3]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?"
    },
    {
      "name": "(S)Ending 4",
      "tags": "",
      "id": "77",
      "text": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!\n\n[[TRY AGAIN->(S)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(S)Renaissance Hall",
          "original": "[[TRY AGAIN->(S)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!"
    },
    {
      "name": "(S)Ending 5",
      "tags": "",
      "id": "78",
      "text": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!\n\n[[TRY AGAIN->(S)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(S)Renaissance Hall",
          "original": "[[TRY AGAIN->(S)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!"
    },
    {
      "name": "(SR)Pharaoh's Room",
      "tags": "",
      "id": "79",
      "text": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?\n\n[[TELL HIM YOU'RE HIS MOTHER->(SR)Mother]]\n[[BEAT HIM UP->(SR)WWE SMACKDOWN]]",
      "links": [
        {
          "linkText": "TELL HIM YOU'RE HIS MOTHER",
          "passageName": "(SR)Mother",
          "original": "[[TELL HIM YOU'RE HIS MOTHER->(SR)Mother]]"
        },
        {
          "linkText": "BEAT HIM UP",
          "passageName": "(SR)WWE SMACKDOWN",
          "original": "[[BEAT HIM UP->(SR)WWE SMACKDOWN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?"
    },
    {
      "name": "(SR)Ending 3",
      "tags": "",
      "id": "80",
      "text": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!\n\n[[TRY AGAIN->(SR)Egyptian Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(SR)Egyptian Hall",
          "original": "[[TRY AGAIN->(SR)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!"
    },
    {
      "name": "(SR)Mother",
      "tags": "",
      "id": "81",
      "text": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm.\n\n[[CONTINUE->(SR)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SR)Pharaoh's Treasure",
          "original": "[[CONTINUE->(SR)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm."
    },
    {
      "name": "(SR)WWE SMACKDOWN",
      "tags": "",
      "id": "82",
      "text": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm.\n\n[[Continue->(SR)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(SR)Pharaoh's Treasure",
          "original": "[[Continue->(SR)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm."
    },
    {
      "name": "(SR)Pharaoh's Treasure",
      "tags": "",
      "id": "83",
      "text": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?\n\n[[24K SOLID GOLD ANKH WITH DIAMONDS->(SR)Ankh]]\n[[CURSED FINGER OF THE PHARAOH->(SR)Cursed Finger]]\n[[MAGIC STAFF THAT CAN MOVE SAND->(SR)Magic Staff]]",
      "links": [
        {
          "linkText": "24K SOLID GOLD ANKH WITH DIAMONDS",
          "passageName": "(SR)Ankh",
          "original": "[[24K SOLID GOLD ANKH WITH DIAMONDS->(SR)Ankh]]"
        },
        {
          "linkText": "CURSED FINGER OF THE PHARAOH",
          "passageName": "(SR)Cursed Finger",
          "original": "[[CURSED FINGER OF THE PHARAOH->(SR)Cursed Finger]]"
        },
        {
          "linkText": "MAGIC STAFF THAT CAN MOVE SAND",
          "passageName": "(SR)Magic Staff",
          "original": "[[MAGIC STAFF THAT CAN MOVE SAND->(SR)Magic Staff]]"
        }
      ],
      "hooks": [],
      "cleanText": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?"
    },
    {
      "name": "(SR)Ankh",
      "tags": "",
      "id": "84",
      "text": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(SRE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SRE)Main Hall",
          "original": "[[CONTINUE->(SRE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(SR)Cursed Finger",
      "tags": "",
      "id": "85",
      "text": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall.\n\n[[Continue->(SRE)Main Hall]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(SRE)Main Hall",
          "original": "[[Continue->(SRE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(SR)Magic Staff",
      "tags": "",
      "id": "86",
      "text": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(SRE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(SRE)Main Hall",
          "original": "[[CONTINUE->(SRE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(SRE)Main Hall",
      "tags": "",
      "id": "87",
      "text": "You have finally taken one treasure from each hall now time to find out how much money you've made.\n\n[[TOTAL->TOTAL MONEY]]",
      "links": [
        {
          "linkText": "TOTAL",
          "passageName": "TOTAL MONEY",
          "original": "[[TOTAL->TOTAL MONEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have finally taken one treasure from each hall now time to find out how much money you've made."
    },
    {
      "name": "(ES)Renaissance Hall",
      "tags": "",
      "id": "88",
      "text": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?\n\n[[HELP THE KING->(ES)King's Request]]\n[[DON'T HELP->(ES)King's Punishment]]",
      "links": [
        {
          "linkText": "HELP THE KING",
          "passageName": "(ES)King's Request",
          "original": "[[HELP THE KING->(ES)King's Request]]"
        },
        {
          "linkText": "DON'T HELP",
          "passageName": "(ES)King's Punishment",
          "original": "[[DON'T HELP->(ES)King's Punishment]]"
        }
      ],
      "hooks": [],
      "cleanText": "You some steps into the Renaisance Hall and find cool medieval art displayed. Things from suits of armor to giant catapults can be seen around the room. You walk around amazed by all the cool contraptions when the wax figure of a King comes to life. He requests your help, what do you do?"
    },
    {
      "name": "(ES)King's Request",
      "tags": "",
      "id": "89",
      "text": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline.\n\n[[MARRY THE PRINCESS->(ES)Marriage]]\n[[DECLINE HIS OFFER->(ES)Ending 4]]",
      "links": [
        {
          "linkText": "MARRY THE PRINCESS",
          "passageName": "(ES)Marriage",
          "original": "[[MARRY THE PRINCESS->(ES)Marriage]]"
        },
        {
          "linkText": "DECLINE HIS OFFER",
          "passageName": "(ES)Ending 4",
          "original": "[[DECLINE HIS OFFER->(ES)Ending 4]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline."
    },
    {
      "name": "(ES)King's Punishment",
      "tags": "",
      "id": "90",
      "text": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever.\n\n[[MARRY HIS DAUGHTER->(ES)Marriage]]\n[[LIVE LIFE AS A PRISONER->(ES)Ending 5]]",
      "links": [
        {
          "linkText": "MARRY HIS DAUGHTER",
          "passageName": "(ES)Marriage",
          "original": "[[MARRY HIS DAUGHTER->(ES)Marriage]]"
        },
        {
          "linkText": "LIVE LIFE AS A PRISONER",
          "passageName": "(ES)Ending 5",
          "original": "[[LIVE LIFE AS A PRISONER->(ES)Ending 5]]"
        }
      ],
      "hooks": [],
      "cleanText": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever."
    },
    {
      "name": "(E)King's Request",
      "tags": "",
      "id": "91",
      "text": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline.\n\n[[MARRY THE PRINCESS->(E)Marriage]]\n[[DECLINE HIS OFFER->(E)Ending 4]]",
      "links": [
        {
          "linkText": "MARRY THE PRINCESS",
          "passageName": "(E)Marriage",
          "original": "[[MARRY THE PRINCESS->(E)Marriage]]"
        },
        {
          "linkText": "DECLINE HIS OFFER",
          "passageName": "(E)Ending 4",
          "original": "[[DECLINE HIS OFFER->(E)Ending 4]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to aid the king in anyway you can. He walks with you telling you all about the history of his Kingdom and how he has fallen ill with an uncurable disease. He wants you to marry his daughter the princess because he needs a someone to rule the kingdom and continue his bloodline."
    },
    {
      "name": "(E)King's Punishment",
      "tags": "",
      "id": "92",
      "text": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever.\n\n[[MARRY HIS DAUGHTER->(E)Marriage]]\n[[LIVE LIFE AS A PRISONER->(E)Ending 5]]",
      "links": [
        {
          "linkText": "MARRY HIS DAUGHTER",
          "passageName": "(E)Marriage",
          "original": "[[MARRY HIS DAUGHTER->(E)Marriage]]"
        },
        {
          "linkText": "LIVE LIFE AS A PRISONER",
          "passageName": "(E)Ending 5",
          "original": "[[LIVE LIFE AS A PRISONER->(E)Ending 5]]"
        }
      ],
      "hooks": [],
      "cleanText": "You tell him that you aren't interested in helping him and that you're here because you have your own thing. The King gets angry and with a snap of his finger the suits of armor come to life and apprehend you. They take you downstairs and toss you into a cell. The King tells you to stay down here until you decide to change your mind about marrying his daughter or rot in here forever."
    },
    {
      "name": "(ES)Marriage",
      "tags": "",
      "id": "93",
      "text": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around.\n\n[[TAKE A DRINK->(ES)Ending 6]]\n[[TRY TO FIND THE TREASURE ROOM->(ES)King's Treasure]]",
      "links": [
        {
          "linkText": "TAKE A DRINK",
          "passageName": "(ES)Ending 6",
          "original": "[[TAKE A DRINK->(ES)Ending 6]]"
        },
        {
          "linkText": "TRY TO FIND THE TREASURE ROOM",
          "passageName": "(ES)King's Treasure",
          "original": "[[TRY TO FIND THE TREASURE ROOM->(ES)King's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around."
    },
    {
      "name": "(ES)Ending 4",
      "tags": "",
      "id": "94",
      "text": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!\n\n[[TRY AGAIN->(ES)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(ES)Renaissance Hall",
          "original": "[[TRY AGAIN->(ES)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!"
    },
    {
      "name": "(E)Marriage",
      "tags": "",
      "id": "95",
      "text": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around.\n\n[[TAKE A DRINK->(E)Ending 6]]\n[[TRY TO FIND THE TREASURE ROOM->(E)King's Treasure]]",
      "links": [
        {
          "linkText": "TAKE A DRINK",
          "passageName": "(E)Ending 6",
          "original": "[[TAKE A DRINK->(E)Ending 6]]"
        },
        {
          "linkText": "TRY TO FIND THE TREASURE ROOM",
          "passageName": "(E)King's Treasure",
          "original": "[[TRY TO FIND THE TREASURE ROOM->(E)King's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to marry the princess. They celebrate the wedding with a huge feast. So much delicious food and drinks all around the table. There is music playing and lots of the King's subjects dancing all around."
    },
    {
      "name": "(E)Ending 4",
      "tags": "",
      "id": "96",
      "text": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!\n\n[[TRY AGAIN->(E)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(E)Renaissance Hall",
          "original": "[[TRY AGAIN->(E)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "The King is upset that he told you his super sad sob story and you refused to help him even though you said you would. Suddenly his men surround you and fills your body up with arrows. GAME OVER!"
    },
    {
      "name": "(E)Ending 5",
      "tags": "",
      "id": "97",
      "text": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!\n\n[[TRY AGAIN->(E)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(E)Renaissance Hall",
          "original": "[[TRY AGAIN->(E)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!"
    },
    {
      "name": "(ES)Ending 5",
      "tags": "",
      "id": "98",
      "text": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!\n\n[[TRY AGAIN->(ES)Renaissance Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(ES)Renaissance Hall",
          "original": "[[TRY AGAIN->(ES)Renaissance Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to live your life as a prisoner. You enjoy being hung from your hands above your head 12 hours of the day, doing manual labor, and eating slop with grey water everyday for the rest of your life. GAME OVER!"
    },
    {
      "name": "(E)Ending 6",
      "tags": "",
      "id": "99",
      "text": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!\n\n[[TRY AGAIN->(E)Marriage]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(E)Marriage",
          "original": "[[TRY AGAIN->(E)Marriage]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!"
    },
    {
      "name": "(E)King's Treasure",
      "tags": "",
      "id": "100",
      "text": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in.\n\n[[THE KING'S SWORD->(E)King's Sword]]\n[[CROWN WITH GIGANTIC GEM->(E)Crown]]\n[[CAPE WITH PORTAL FOR INFINITE STORAGE->(E)Cape]]",
      "links": [
        {
          "linkText": "THE KING'S SWORD",
          "passageName": "(E)King's Sword",
          "original": "[[THE KING'S SWORD->(E)King's Sword]]"
        },
        {
          "linkText": "CROWN WITH GIGANTIC GEM",
          "passageName": "(E)Crown",
          "original": "[[CROWN WITH GIGANTIC GEM->(E)Crown]]"
        },
        {
          "linkText": "CAPE WITH PORTAL FOR INFINITE STORAGE",
          "passageName": "(E)Cape",
          "original": "[[CAPE WITH PORTAL FOR INFINITE STORAGE->(E)Cape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in."
    },
    {
      "name": "(ES)Ending 6",
      "tags": "",
      "id": "101",
      "text": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!\n\n[[TRY AGAIN->(ES)Marriage]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(ES)Marriage",
          "original": "[[TRY AGAIN->(ES)Marriage]]"
        }
      ],
      "hooks": [],
      "cleanText": "You grab a drink \"Maybe this won't be so bad\" you say to yourself. You drink until you pass out and party with the King and his people. You have so much fun partying with people from the renaissance. In the morning you get thrown into a suit and next thing you know you are standing in front of the princess. You get married and as soon as you become the new king, the old king's rival burst in out of nowhere with his army and attack. GAME OVER!"
    },
    {
      "name": "(ES)King's Treasure",
      "tags": "",
      "id": "102",
      "text": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in.\n\n[[THE KING'S SWORD->(ES)King's Sword]]\n[[CROWN WITH GIGANTIC GEM->(ES)Crown]]\n[[CAPE WITH PORTAL FOR INFINITE STORAGE->(ES)Cape]]",
      "links": [
        {
          "linkText": "THE KING'S SWORD",
          "passageName": "(ES)King's Sword",
          "original": "[[THE KING'S SWORD->(ES)King's Sword]]"
        },
        {
          "linkText": "CROWN WITH GIGANTIC GEM",
          "passageName": "(ES)Crown",
          "original": "[[CROWN WITH GIGANTIC GEM->(ES)Crown]]"
        },
        {
          "linkText": "CAPE WITH PORTAL FOR INFINITE STORAGE",
          "passageName": "(ES)Cape",
          "original": "[[CAPE WITH PORTAL FOR INFINITE STORAGE->(ES)Cape]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to sneak away and look for the King's Treasure room. While everyone is getting too drunk you come across the the room. You take a peak inside and there was treasure and gold everywhere. You grin with delight. You find three treasures that you are interested in."
    },
    {
      "name": "(ES)King's Sword",
      "tags": "",
      "id": "103",
      "text": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(ESR)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ESR)Main Hall",
          "original": "[[CONTINUE->(ESR)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(ES)Crown",
      "tags": "",
      "id": "104",
      "text": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(ESR)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ESR)Main Hall",
          "original": "[[CONTINUE->(ESR)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(ES)Cape",
      "tags": "",
      "id": "105",
      "text": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(ESR)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ESR)Main Hall",
          "original": "[[CONTINUE->(ESR)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(E)King's Sword",
      "tags": "",
      "id": "106",
      "text": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(ER)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ER)Main Hall",
          "original": "[[CONTINUE->(ER)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the King's Sword. You swing it around and accidentally launch an energy projectile at the bust of the King. You put the King's Sword into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(E)Crown",
      "tags": "",
      "id": "107",
      "text": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(ER)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ER)Main Hall",
          "original": "[[CONTINUE->(ER)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Crown with a gigantic gem. It is a lot heavier on your head than you thought, you head gives in and you fall over. You put the Crown into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(E)Cape",
      "tags": "",
      "id": "108",
      "text": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall.\n\n[[CONTINUE->(ER)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ER)Main Hall",
          "original": "[[CONTINUE->(ER)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cape. You put it on and reach inside and feel around for something. You pull out a chalice half full with wine. Looks like the King has more problems more than his illness. You put the Cape into your backpack. You leave the Renaissance Hall."
    },
    {
      "name": "(ER)Main Hall",
      "tags": "",
      "id": "109",
      "text": "There is one hall left to explore.\n\n[[SCIENCE HALL->(ER)Science Hall]]",
      "links": [
        {
          "linkText": "SCIENCE HALL",
          "passageName": "(ER)Science Hall",
          "original": "[[SCIENCE HALL->(ER)Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is one hall left to explore."
    },
    {
      "name": "(ESR)Main Hall",
      "tags": "",
      "id": "110",
      "text": "You have finally taken one treasure from each hall now time to find out how much money you've made.\n\n[[TOTAL->TOTAL MONEY]]",
      "links": [
        {
          "linkText": "TOTAL",
          "passageName": "TOTAL MONEY",
          "original": "[[TOTAL->TOTAL MONEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have finally taken one treasure from each hall now time to find out how much money you've made."
    },
    {
      "name": "(ER)Science Hall",
      "tags": "",
      "id": "111",
      "text": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?\n\n[[PARKOUR ON DISPLAYS->(ER)Ending 2]]\n[[DISGUISE AS ROBOT->(ER)Science Security Room]]",
      "links": [
        {
          "linkText": "PARKOUR ON DISPLAYS",
          "passageName": "(ER)Ending 2",
          "original": "[[PARKOUR ON DISPLAYS->(ER)Ending 2]]"
        },
        {
          "linkText": "DISGUISE AS ROBOT",
          "passageName": "(ER)Science Security Room",
          "original": "[[DISGUISE AS ROBOT->(ER)Science Security Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?"
    },
    {
      "name": "(ER)Ending 2",
      "tags": "",
      "id": "112",
      "text": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!\n\n[[TRY AGAIN->(ER)Science Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(ER)Science Hall",
          "original": "[[TRY AGAIN->(ER)Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!"
    },
    {
      "name": "(ER)Science Security Room",
      "tags": "",
      "id": "113",
      "text": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?\n\n[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(ER)Experiment Raygun]]\n[[SKULL OF NEIL ARMSTRONG->(ER)Skull of Neil]]\n[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(ER)Ghost Punching Gloves]]",
      "links": [
        {
          "linkText": "EXPERIMENTAL ORBITAL BEAM RAYGUN",
          "passageName": "(ER)Experiment Raygun",
          "original": "[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(ER)Experiment Raygun]]"
        },
        {
          "linkText": "SKULL OF NEIL ARMSTRONG",
          "passageName": "(ER)Skull of Neil",
          "original": "[[SKULL OF NEIL ARMSTRONG->(ER)Skull of Neil]]"
        },
        {
          "linkText": "BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS",
          "passageName": "(ER)Ghost Punching Gloves",
          "original": "[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(ER)Ghost Punching Gloves]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?"
    },
    {
      "name": "(R)Ending 2",
      "tags": "",
      "id": "114",
      "text": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!\n\n[[TRY AGAIN->(R)Science Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(R)Science Hall",
          "original": "[[TRY AGAIN->(R)Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!"
    },
    {
      "name": "(R)Science Security Room",
      "tags": "",
      "id": "115",
      "text": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?\n\n[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(R)Experiment Raygun]]\n[[SKULL OF NEIL ARMSTRONG->(R)Skull of Neil]]\n[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(R)Ghost Punching Gloves]]",
      "links": [
        {
          "linkText": "EXPERIMENTAL ORBITAL BEAM RAYGUN",
          "passageName": "(R)Experiment Raygun",
          "original": "[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(R)Experiment Raygun]]"
        },
        {
          "linkText": "SKULL OF NEIL ARMSTRONG",
          "passageName": "(R)Skull of Neil",
          "original": "[[SKULL OF NEIL ARMSTRONG->(R)Skull of Neil]]"
        },
        {
          "linkText": "BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS",
          "passageName": "(R)Ghost Punching Gloves",
          "original": "[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(R)Ghost Punching Gloves]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?"
    },
    {
      "name": "(ER)Experiment Raygun",
      "tags": "",
      "id": "116",
      "text": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall\n\n[[CONTINUE->(ERS)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ERS)Main Hall",
          "original": "[[CONTINUE->(ERS)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall"
    },
    {
      "name": "(ER)Skull of Neil",
      "tags": "",
      "id": "117",
      "text": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall.\n\n[[CONTINUE->(ERS)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ERS)Main Hall",
          "original": "[[CONTINUE->(ERS)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall."
    },
    {
      "name": "(ER)Ghost Punching Gloves",
      "tags": "",
      "id": "118",
      "text": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall.\n\n[[CONTINUE->(ERS)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(ERS)Main Hall",
          "original": "[[CONTINUE->(ERS)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall."
    },
    {
      "name": "(R)Experiment Raygun",
      "tags": "",
      "id": "119",
      "text": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall\n\n[[CONTINUE->(RS)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RS)Main Hall",
          "original": "[[CONTINUE->(RS)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall"
    },
    {
      "name": "(R)Skull of Neil",
      "tags": "",
      "id": "120",
      "text": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall.\n\n[[CONTINUE->(RS)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RS)Main Hall",
          "original": "[[CONTINUE->(RS)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall."
    },
    {
      "name": "(R)Ghost Punching Gloves",
      "tags": "",
      "id": "121",
      "text": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall.\n\n[[CONTINUE->(RS)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RS)Main Hall",
          "original": "[[CONTINUE->(RS)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall."
    },
    {
      "name": "(RS)Main Hall",
      "tags": "",
      "id": "122",
      "text": "There is one hall left to explore.\n\n[[EGYPTIAN HALL->(RS)Egyptian Hall]]",
      "links": [
        {
          "linkText": "EGYPTIAN HALL",
          "passageName": "(RS)Egyptian Hall",
          "original": "[[EGYPTIAN HALL->(RS)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is one hall left to explore."
    },
    {
      "name": "(ERS)Main Hall",
      "tags": "",
      "id": "123",
      "text": "You have finally taken one treasure from each hall now time to find out how much money you've made.\n\n[[TOTAL->TOTAL MONEY]]",
      "links": [
        {
          "linkText": "TOTAL",
          "passageName": "TOTAL MONEY",
          "original": "[[TOTAL->TOTAL MONEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have finally taken one treasure from each hall now time to find out how much money you've made."
    },
    {
      "name": "(RS)Egyptian Hall",
      "tags": "",
      "id": "124",
      "text": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?\n\n[[FIND THE SOURCE->(RS)Pharaoh's Room]]\n[[LEAVE->(RS)Ending 3]]",
      "links": [
        {
          "linkText": "FIND THE SOURCE",
          "passageName": "(RS)Pharaoh's Room",
          "original": "[[FIND THE SOURCE->(RS)Pharaoh's Room]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "(RS)Ending 3",
          "original": "[[LEAVE->(RS)Ending 3]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Egyptian Hall and find incredible pieces of art displayed. Things from sculptures to the mummy's sarcophagus can be seen. You take a few steps in and all of a sudden sand starts to appear. There is a sandstorm starting in here. What do you do?"
    },
    {
      "name": "(R)Pharaoh's Room",
      "tags": "",
      "id": "125",
      "text": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?\n\n[[TELL HIM YOU'RE HIS MOTHER->(R)Mother]]\n[[BEAT HIM UP->(R)WWE SMACKDOWN]]",
      "links": [
        {
          "linkText": "TELL HIM YOU'RE HIS MOTHER",
          "passageName": "(R)Mother",
          "original": "[[TELL HIM YOU'RE HIS MOTHER->(R)Mother]]"
        },
        {
          "linkText": "BEAT HIM UP",
          "passageName": "(R)WWE SMACKDOWN",
          "original": "[[BEAT HIM UP->(R)WWE SMACKDOWN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?"
    },
    {
      "name": "(R)Ending 3",
      "tags": "",
      "id": "126",
      "text": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!\n\n[[TRY AGAIN->(R)Egyptian Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(R)Egyptian Hall",
          "original": "[[TRY AGAIN->(R)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!"
    },
    {
      "name": "(RS)Pharaoh's Room",
      "tags": "",
      "id": "127",
      "text": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?\n\n[[TELL HIM YOU'RE HIS MOTHER->(RS)Mother]]\n[[BEAT HIM UP->(RS)WWE SMACKDOWN]]",
      "links": [
        {
          "linkText": "TELL HIM YOU'RE HIS MOTHER",
          "passageName": "(RS)Mother",
          "original": "[[TELL HIM YOU'RE HIS MOTHER->(RS)Mother]]"
        },
        {
          "linkText": "BEAT HIM UP",
          "passageName": "(RS)WWE SMACKDOWN",
          "original": "[[BEAT HIM UP->(RS)WWE SMACKDOWN]]"
        }
      ],
      "hooks": [],
      "cleanText": "You put on your mask to keep the sand out of your mouth determined to find the source of this sandstorm. You push against the winds knowing that the closer you get to the source the more winds resist you. Before you know it you made to it the source, the pharaoh's room.''WHO DARES DISTURB MY SLUMBER!!!'' What do you do?"
    },
    {
      "name": "(RS)Ending 3",
      "tags": "",
      "id": "128",
      "text": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!\n\n[[TRY AGAIN->(RS)Egyptian Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(RS)Egyptian Hall",
          "original": "[[TRY AGAIN->(RS)Egyptian Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decided to choose life so you turned around and headed for the exit. Only to have the storm get even stronger. You start to get lost but keep walking forward for what it seems minutes have passed and you haven't made any progress. Eventually your lungs fill with sand and you die. GAMEOVER!"
    },
    {
      "name": "(R)Mother",
      "tags": "",
      "id": "129",
      "text": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm.\n\n[[CONTINUE->(R)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(R)Pharaoh's Treasure",
          "original": "[[CONTINUE->(R)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm."
    },
    {
      "name": "(R)WWE SMACKDOWN",
      "tags": "",
      "id": "130",
      "text": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm.\n\n[[Continue->(R)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(R)Pharaoh's Treasure",
          "original": "[[Continue->(R)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm."
    },
    {
      "name": "(RS)Mother",
      "tags": "",
      "id": "131",
      "text": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm.\n\n[[CONTINUE->(RS)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RS)Pharaoh's Treasure",
          "original": "[[CONTINUE->(RS)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "\"I'm your mother and you need to go back to sleep and stop this tantrum young man, I'm not going to tell you again\" you say to the mummy. \"OK MOTHER\" says the pharoah and lays back down into his coffin stopping the sandstorm."
    },
    {
      "name": "(RS)WWE SMACKDOWN",
      "tags": "",
      "id": "132",
      "text": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm.\n\n[[Continue->(RS)Pharaoh's Treasure]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(RS)Pharaoh's Treasure",
          "original": "[[Continue->(RS)Pharaoh's Treasure]]"
        }
      ],
      "hooks": [],
      "cleanText": "''Stop this sandstorm!!'' You yelled, throwing as many punches as you can at the mummy. The mummy's body flailing around as each fist connects to it. The evil red eyes on the mummy slowly disappeared and his body falls back into the coffin, stopping the sandstorm."
    },
    {
      "name": "(R)Pharaoh's Treasure",
      "tags": "",
      "id": "133",
      "text": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?\n\n[[24K SOLID GOLD ANKH WITH DIAMONDS->(R)Ankh]]\n[[CURSED FINGER OF THE PHARAOH->(R)Cursed Finger]]\n[[MAGIC STAFF THAT CAN MOVE SAND->(R)Magic Staff]]",
      "links": [
        {
          "linkText": "24K SOLID GOLD ANKH WITH DIAMONDS",
          "passageName": "(R)Ankh",
          "original": "[[24K SOLID GOLD ANKH WITH DIAMONDS->(R)Ankh]]"
        },
        {
          "linkText": "CURSED FINGER OF THE PHARAOH",
          "passageName": "(R)Cursed Finger",
          "original": "[[CURSED FINGER OF THE PHARAOH->(R)Cursed Finger]]"
        },
        {
          "linkText": "MAGIC STAFF THAT CAN MOVE SAND",
          "passageName": "(R)Magic Staff",
          "original": "[[MAGIC STAFF THAT CAN MOVE SAND->(R)Magic Staff]]"
        }
      ],
      "hooks": [],
      "cleanText": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?"
    },
    {
      "name": "(RS)Pharaoh's Treasure",
      "tags": "",
      "id": "134",
      "text": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?\n\n[[24K SOLID GOLD ANKH WITH DIAMONDS->(RS)Ankh]]\n[[CURSED FINGER OF THE PHARAOH->(RS)Cursed Finger]]\n[[MAGIC STAFF THAT CAN MOVE SAND->(RS)Magic Staff]]",
      "links": [
        {
          "linkText": "24K SOLID GOLD ANKH WITH DIAMONDS",
          "passageName": "(RS)Ankh",
          "original": "[[24K SOLID GOLD ANKH WITH DIAMONDS->(RS)Ankh]]"
        },
        {
          "linkText": "CURSED FINGER OF THE PHARAOH",
          "passageName": "(RS)Cursed Finger",
          "original": "[[CURSED FINGER OF THE PHARAOH->(RS)Cursed Finger]]"
        },
        {
          "linkText": "MAGIC STAFF THAT CAN MOVE SAND",
          "passageName": "(RS)Magic Staff",
          "original": "[[MAGIC STAFF THAT CAN MOVE SAND->(RS)Magic Staff]]"
        }
      ],
      "hooks": [],
      "cleanText": "When the sandstorm calms down you find yourself inside the Pharoah's Treasure Room. You find three treasure that catch your interest. What do you choose?"
    },
    {
      "name": "(R)Ankh",
      "tags": "",
      "id": "135",
      "text": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(RE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RE)Main Hall",
          "original": "[[CONTINUE->(RE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(R)Cursed Finger",
      "tags": "",
      "id": "136",
      "score": 325,
      "text": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall.\n\n[[Continue->(RE)Main Hall]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(RE)Main Hall",
          "original": "[[Continue->(RE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(R)Magic Staff",
      "tags": "",
      "id": "137",
      "score": 60,
      "text": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(RE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RE)Main Hall",
          "original": "[[CONTINUE->(RE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(RS)Ankh",
      "tags": "",
      "id": "138",
      "score": 275,
      "text": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(RSE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RSE)Main Hall",
          "original": "[[CONTINUE->(RSE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You picked up the 24K solid gold diamond encrusted Ankh. INFINITE POWER FLOWS WITHIN YOU. \"This will fetch a good price.\" you say, and puts it in your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(RS)Cursed Finger",
      "tags": "",
      "id": "139",
      "score": 325,
      "text": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall.\n\n[[Continue->(RSE)Main Hall]]",
      "links": [
        {
          "linkText": "Continue",
          "passageName": "(RSE)Main Hall",
          "original": "[[Continue->(RSE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Cursed Finger. An evil aura can be felt coming from the finger. It speaks to you in a small voice for you to consume the finger. Offering you a 1 in a million chance to gain godlike powers. You put the cursed finger into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(RS)Magic Staff",
      "tags": "",
      "id": "140",
      "score": 60,
      "text": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall.\n\n[[CONTINUE->(RSE)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RSE)Main Hall",
          "original": "[[CONTINUE->(RSE)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Magic Staff. You wave it around and sand moves to wherever you point it. You use the Magic Staff to build a little sand castle. You put the staff into your backpack. You leave the Egyptian Hall."
    },
    {
      "name": "(RE)Main Hall",
      "tags": "",
      "id": "141",
      "score": 15,
      "text": "There is one hall left to explore.\n\n[[SCIENCE HALL->(RE)Science Hall]]",
      "links": [
        {
          "linkText": "SCIENCE HALL",
          "passageName": "(RE)Science Hall",
          "original": "[[SCIENCE HALL->(RE)Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "There is one hall left to explore."
    },
    {
      "name": "(RSE)Main Hall",
      "tags": "",
      "id": "142",
      "score": 25,
      "text": "You have finally taken one treasure from each hall now time to find out how much money you've made.\n\n[[TOTAL->TOTAL MONEY]]",
      "links": [
        {
          "linkText": "TOTAL",
          "passageName": "TOTAL MONEY",
          "original": "[[TOTAL->TOTAL MONEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have finally taken one treasure from each hall now time to find out how much money you've made."
    },
    {
      "name": "(RE)Science Hall",
      "tags": "",
      "id": "143",
      "score": 5,
      "text": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?\n\n[[PARKOUR ON DISPLAYS->(RE)Ending 2]]\n[[DISGUISE AS ROBOT->(RE)Science Security Room]]",
      "links": [
        {
          "linkText": "PARKOUR ON DISPLAYS",
          "passageName": "(RE)Ending 2",
          "original": "[[PARKOUR ON DISPLAYS->(RE)Ending 2]]"
        },
        {
          "linkText": "DISGUISE AS ROBOT",
          "passageName": "(RE)Science Security Room",
          "original": "[[DISGUISE AS ROBOT->(RE)Science Security Room]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the Science Hall and find incredible pieces of technology displayed. Things from giant robots to the first model of airplanes can be seen. But before you can take a step you notice the whole section of the museum is covered with lasers and high tech security robots. You spot the security room across the hall. What do you do?"
    },
    {
      "name": "(RE)Ending 2",
      "tags": "",
      "id": "144",
      "score": -20,
      "text": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!\n\n[[TRY AGAIN->(RE)Science Hall]]",
      "links": [
        {
          "linkText": "TRY AGAIN",
          "passageName": "(RE)Science Hall",
          "original": "[[TRY AGAIN->(RE)Science Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You make a running start and you leap onto the model airplane and it starts tipping over the one side, you find yourself slipping and holding on for dear life. You eventually lose grip and fall onto the lasers alerting the robot guards to surround you and take you out. GAME OVER!"
    },
    {
      "name": "(RE)Science Security Room",
      "tags": "",
      "id": "145",
      "score": 15,
      "text": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?\n\n[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(RE)Experiment Raygun]]\n[[SKULL OF NEIL ARMSTRONG->(RE)Skull of Neil]]\n[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(RE)Ghost Punching Gloves]]",
      "links": [
        {
          "linkText": "EXPERIMENTAL ORBITAL BEAM RAYGUN",
          "passageName": "(RE)Experiment Raygun",
          "original": "[[EXPERIMENTAL ORBITAL BEAM RAYGUN->(RE)Experiment Raygun]]"
        },
        {
          "linkText": "SKULL OF NEIL ARMSTRONG",
          "passageName": "(RE)Skull of Neil",
          "original": "[[SKULL OF NEIL ARMSTRONG->(RE)Skull of Neil]]"
        },
        {
          "linkText": "BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS",
          "passageName": "(RE)Ghost Punching Gloves",
          "original": "[[BOXING GLOVES THAT ALLOW YOU TO PUNCH GHOSTS->(RE)Ghost Punching Gloves]]"
        }
      ],
      "hooks": [],
      "cleanText": "You take out the nearest robot guard and disguised yourself as one of them. You walk towards the security room. Waving and saying wassup to the other robot guards trying to blend in. This works and you make it to the front door. You enter to see one guard sitting in front of all the screens he was asleep all this time. You disable the cameras and walk back out, you see three treasures that peak your interest. Which one will you choose the take?"
    },
    {
      "name": "(RE)Experiment Raygun",
      "tags": "",
      "id": "146",
      "score": 100,

      "text": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall\n\n[[CONTINUE->(RES)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RES)Main Hall",
          "original": "[[CONTINUE->(RES)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the Experimental Orbital Beam Raygun. You attempt to fire it but nothing happened. Must be out of batteries. You put the raygun into your backpack and left the Science Hall"
    },
    {
      "name": "(RE)Skull of Neil",
      "tags": "",
      "id": "147",
      "score": 70,
      "text": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall.\n\n[[CONTINUE->(RES)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RES)Main Hall",
          "original": "[[CONTINUE->(RES)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up Neil Armstrong's Skull, I guess you like old people's bones for some reason, still it will fetch a hefty price. You put the skull into your backpack and left the Science Hall."
    },
    {
      "name": "(RE)Ghost Punching Gloves",
      "tags": "",
      "id": "148",
      "score": 200,
      "text": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall.\n\n[[CONTINUE->(RES)Main Hall]]",
      "links": [
        {
          "linkText": "CONTINUE",
          "passageName": "(RES)Main Hall",
          "original": "[[CONTINUE->(RES)Main Hall]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pick up the boxing gloves that can punch ghosts. You put them on and swung around in the air. Nothing happened because you don't believe in ghost therefore no ghosts revealed themselves to you. (in reality you just punched out 4 ghosts around you.) You put the gloves into your backpack and left the Science Hall."
    },
    {
      "name": "(RES)Main Hall",
      "tags": "",
      "id": "149",
      "score": 5,
      "text": "You have finally taken one treasure from each hall now time to find out how much money you've made.\n\n[[TOTAL->TOTAL MONEY]]",
      "links": [
        {
          "linkText": "TOTAL",
          "passageName": "TOTAL MONEY",
          "original": "[[TOTAL->TOTAL MONEY]]"
        }
      ],
      "hooks": [],
      "cleanText": "You have finally taken one treasure from each hall now time to find out how much money you've made."
    },
    {
      "name": "TOTAL MONEY",
      "tags": "",
      "id": "150",
      "text": "Double-click this passage to edit it.",
      "links": [],
      "hooks": [],
      "cleanText": "Double-click this passage to edit it."
    }
  ]
}


# ----------------------------------------------------------------

def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
        print("Moves:{},Score:{}".format(moves, score))
        print("You are at the " + str(current_location["name"]))
	    print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "South of Museum"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
		break
        moves = moves + 1
	location_label = update(current_location, location_label, response)
	current_location = find_current_location(location_label)
    
        if "score" in current_location:
            score = score + current_location["score"]

	render(current_location, score, moves)
	response = get_input()


print("Thanks for playing!")