def put_position(position, mss):
        verification = ["1","2","3","4","5","6","7"]
        # this while is for that the player can only enter the pisitions aviables and doesn't allow enter letters
        while position not in verification:
            print("you can only enter numbers of 1 to 7")
            position = input("again: ")
        return int(position)-1