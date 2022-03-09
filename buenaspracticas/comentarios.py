# un comentario de una linea
"""
comentario de varias lineas
"""


def suma(a,b):
    """
    params: two ints
    action: sum of the first and the second number
    returns: the result of the sum
    """
    print(a+b)

inp = input("")
try:
    print(int(inp))
except Exception as e:
    print(e)

