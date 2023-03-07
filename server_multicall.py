from xmlrpc.server import SimpleXMLRPCServer

""" 
Multicall Server
Normalerweise wird jede Funktion hintereinander 
abgearbeitet.
Wir können Funktionsaufrufe aber auch bündeln.
"""

HOST = "localhost"
PORT = 9000


def dividieren(a: int, b: int) -> float:
    return a / b


def multiplizieren(a: int, b: int) -> int:
    return a * b


def summe(a: int, b: int) -> int:
    """Berechne Summe."""
    return a + b


if __name__ == "__main__":
    server = SimpleXMLRPCServer(addr=(HOST, PORT))

    server.register_function(summe, "summe")
    server.register_function(dividieren, "dividieren")
    server.register_function(multiplizieren, "multiplizieren")

    # Erlaube Mulitcall auf Clientseite (Bündeln von Funktionsaufrufen)
    server.register_multicall_functions()
    print(f"Server ist running on {PORT}")
    server.serve_forever()
