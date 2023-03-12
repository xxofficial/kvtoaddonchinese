import re
class Ability(object):
    upgrade_map = {
        "NoUpgrade": "",
        "HasShardUpgrade" : "shard",
        "HasScepterUpgrade" : "scepter"
    }
    def __init__(self, name, special, upgrade = "NoUpgrade"):
        self.name = name
        self.special = special
        self.upgrade = self.upgrade_map[upgrade]

def loadKv(filename):
    abilitycachefile = open("ability_cache.txt", "a+")
    abilitycachefile.seek(0)
    abilitycache = [line.rstrip('\n') for line in abilitycachefile]
    file = open(filename, "r")
    res = {}
    abilitylist = []
    # currentkey = ""
    currentmap = res
    lastmap = res
    laststr = ""
    currentlevel = 0
    ability = ""
    for line in file:
        list = line.split("\"")
        newlist = []
        for str in list:
            str = re.sub(r"//.*", "", str)
            str = str.strip('\t').strip('\n').strip()
            if str != '':
                newlist.append(str)
        if len(newlist) == 0:
            continue
        if len(newlist) == 1 and newlist[0] != '{' and newlist[0] != '}':
            currentkey = newlist[0]
        elif newlist[0] == '{':
            lastmap = currentmap
            currentmap[currentkey] = {}
            currentmap = currentmap[currentkey]
            currentlevel = currentlevel + 1
            if currentlevel == 2 and currentkey not in abilitycache:
                ability = Ability(currentkey, {})
                abilitylist.append(ability)
                abilitycachefile.write(currentkey)
                abilitycachefile.write("\n")
        elif len(newlist) > 1:
            currentmap[newlist[0]] = newlist[1]
            if ability != "":
                if laststr == "var_type":
                    ability.special[newlist[0]] = newlist[1]
                laststr = newlist[0]
                if newlist[0] == "HasShardUpgrade" or newlist[0] == "HasScepterUpgrade":
                    ability.upgrade = ability.upgrade_map[newlist[0]]
        elif newlist[0] == '}':
            currentmap = lastmap
            currentlevel = currentlevel - 1
    abilitycachefile.close()
    file.close()
    return res, abilitylist
def LoadAbilityList(filename):
    _, abilitylist = loadKv(filename)
    return abilitylist
        

# res, _ = loadKv("npc_abilities_custom.txt")
# print(res)
# generateAddonChinese("npc_abilities_custom.txt")
# print(len(LoadAbilityList("npc_abilities_custom.txt")))