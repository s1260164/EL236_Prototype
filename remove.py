## remove "(", ")", "[", "]", "'", and " " from tagged.
def remover(tagged):
    string = str(tagged)
    string_new = string.replace('(', '')
    string_new = string_new.replace(')', '')
    string_new = string_new.replace('[', '')
    string_new = string_new.replace(']', '')
    string_new = string_new.replace('[', '')
    string_new = string_new.replace("'", '')
    string_new = string_new.replace(" ", '')
    tagged_new = string_new.split(",")
    return(tagged_new, string_new)
