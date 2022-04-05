"""
The code prints the first state on the FILE_NAME file which all of its name's character are at the same
row on the keyboard.
"""
ROW1 = set("q,w,e,r,t,y,u,i,o,p".split(","))
ROW2 = set("a,s,d,f,g,h,j,k,l".split(","))
ROW3 = set("z,x,c,v,b,n,m".split(","))
FILE_NAME = "states.txt"


def find_special_state() -> str:
    """
    The function is finding the first state which all of its name's characters
    are at the same row on the keyboard.
    :return: The state that all of its name's characters are at the same keyboard row.
    """
    with open(FILE_NAME, 'r') as reader:
        for state in reader:
            if is_special_state(state.strip()):
                return state.strip()


def is_special_state(state_name: str) -> bool:
    """
    The function return if all of the received state name's character are at the same
    row on the keyboard.
    :param state_name: The tested state.
    :return: If all of the received state name's character are at the same row on the keyboard.
    """
    state_name_set = {x for x in state_name}
    return not state_name_set - ROW1 or not state_name_set - ROW2 or not state_name_set - ROW3


if __name__ == "__main__":
    print(find_special_state())
