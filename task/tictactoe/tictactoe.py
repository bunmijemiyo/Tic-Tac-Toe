output = "---------"
outputs = "_________".replace("_", " ")

coord_box = ["1", "2", "3"]
print(f"{output}\n| {' '.join(outputs[:3])} |\n| {' '.join(outputs[3:6])} |\n| {' '.join(outputs[6:9])} |\n{output}")
counter = 0
while True:
    try:
        col, row = input("Enter the coordinates: ").split()

        if col.isalpha() or row.isalpha():
            print("You should enter numbers!")
        elif col not in coord_box or row not in coord_box:
            print("Coordinates should be from 1 to 3!")
        elif col in coord_box and row in coord_box:
            indexx = ((3 - int(row)) * 3) + (int(col) - 1)
            outputs = list(outputs)

            if outputs[indexx] == " ":
                counter += 1
                if counter in [1, 3, 5, 7, 9]:
                    data = "X"
                else:
                    data = "O"
                outputs[indexx] = data
                inside = list(outputs)
                y = "".join(inside)
                xy = y[2] + y[4] + y[6]
                print(f"{output}\n| {' '.join(outputs[:3])} |\n| {' '.join(outputs[3:6])} |\n| {' '.join(outputs[6:9])} |\n{output}")

                if y[:3] == "XXX" or y[3:6] == "XXX" or y[6:9] == "XXX" or y[::3] == "XXX" or y[1::3] == "XXX" or y[2::3] == "XXX" or y[::4] == "XXX" or xy == "XXX":
                    print("X wins")
                    break

                elif y[:3] == "OOO" or y[3:6] == "OOO" or y[6:9] == "OOO" or y[::3] == "OOO" or y[1::3] == "OOO" or y[2::3] == "OOO" or y[::4] == "OOO" or xy == "OOO":
                    print("O wins")
                    break
                elif y.count("X") >= 3 and (y.count("O") - y.count("X")) <= 1 and (y.count("O") + y.count("X")) == 9:
                    print("Draw")
                    break

            else:
                print("This cell is occupied! Choose another one!")
    except ValueError:
        print("You should enter numbers!")
        continue
