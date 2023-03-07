from xmlrpc.client import ServerProxy, MultiCall

url = "<u><link=http://localhost:9000>http://localhost:9000</link></u>"

with ServerProxy(url, verbose=True) as server:
    multicall = MultiCall(server)

    # Bündeln der Funktionsaufrufe
    multicall.dividieren(4, 4)
    multicall.multiplizieren(2, 4)
    multicall.summe(2, 4)

    for response in multicall():
        print("Ergebnis: ", response)
