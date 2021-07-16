import time

def create_block_hola(texto: str) -> None:
    """
    Create a text for mock porpouse

    :param texto: the texto to write
    :returns: None
    :raises FileNotFoundError: raises an exception if file doesnt exist
    """
    try:
        with open("hola.txt", "w") as f:
            for i in range(10):
                time.sleep(1)
                print(f"Linea: {i}")
                f.write(f"{texto}\n")
    except (FileExistsError, FileNotFoundError) as e:
        print(f"Error: {e}")


def create_block_medio(texto: str) -> None:
    """
    Create a text for mock porpouse

    :param texto: the texto to write
    :returns: None
    :raises FileNotFoundError: raises an exception if file doesnt exist
    """
    try:
        with open("hola.txt", "w") as f:
            for i in range(10):
                time.sleep(1)
                print(f"Linea: {i}")
                f.write(f"{texto}\n")
    except (FileExistsError, FileNotFoundError) as e:
        print(f"Error: {e}")

def printer():
    for i in range(10):
        time.sleep(1)
        print("hola")


def create_block_chau(texto: str) -> None:
    """
    Create a text for mock porpouse

    :param texto: the texto to write
    :returns: None
    :raises FileNotFoundError: raises an exception if file doesnt exist
    """
    try:
        with open("hola.txt", "w") as f:
            for i in range(10):
                time.sleep(1)
                print(f"Linea: {i}")
                f.write(f"{texto}\n")
    except (FileExistsError, FileNotFoundError) as e:
        print(f"Error: {e}")



if __name__ == "__main__":
    create_block_hola("Hola", "Pause")
