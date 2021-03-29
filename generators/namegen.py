from random import choice

names = ["jay", "jim", "roy", "axel", "billy", "charlie", "jax", "gina", "paul",
         "ringo", "ally", "nicky", "cam", "ari", "trudie", "cal", "carl", "mary", "lauren",
         "ichabod", "arthur", "ashley", "drake", "kim", "julio", "lorraine", "floyd", "janet",
         "lydia", "charles", "pedro", "bradley", "Joe", "Nik", "Ilon", "arthur", "Guido"]
surnames = [ "barker", "Simpson", "Spirits", "murphy", "blacker", "bleacher", "rogers",
            "warren", "keller", "cocker", "white", "Nickson", "Van Rossum", "Raegan", "Griffin", "Mask"]


def gen_unique_names(names, surnames, how_many):
    answer = []
    while how_many > 0:
        combo = choice(names) + ' ' + choice(surnames)
        if combo not in answer:
            answer.append(combo)
            how_many -= 1

        return combo

