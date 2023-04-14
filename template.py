from string import Template as tp

import loadkv


def GenerateAddonChinese(filename):
    lines = []
    tmp = tp(open("specialtmp.txt", "r").read())
    tmp1 = tp(open("addon_chinese.txt", "r").read())
    tmp2 = tp(open("upgrade.txt", "r").read())
    tmp4 = tp(open("modifier.txt", "r").read())
    for ability in loadkv.LoadAbilityList(filename):
        lines.append(tmp1.substitute({"ability_name": ability.name}))
        lines.append("\n")
        if ability.upgrade != "":
            lines.append(tmp2.substitute(
                {"ability_name": ability.name, "upgrade": ability.upgrade}))
            lines.append("\n")
        for key in ability.special:
            lines.append(tmp.substitute(
                {"ability_name": ability.name, "special_key": key}))
            lines.append("\n")
        lines.append(tmp4.substitute({"ability_name": ability.name}))
        lines.append("\n")
        lines.append("\n")
    file = open("res.txt", "w")
    file.writelines(lines)
    file.close()


GenerateAddonChinese(
    "D:\\respository\\survive\\game\\survive\\scripts\\npc\\kv\\abilities\\transform_hero_abilities.kv")

# tmpFile = open('template.lua', 'r')
# tmp = tp(tmpFile.read())

# c = {"Stu","Te","Lead"}

# for name in c:
#     path = name + ".lua"
#     file = open(path, "w")
#     # lines = []
#     # lines.append(tmp.substitute({"className":name}))
#     file.write(tmp.substitute({"className":name}))
#     file.close()
# tmpFile.close()
