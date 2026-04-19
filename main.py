def camel_case(matn):
    so'zlar = matn.split()
    natija = so'zlar[0].lower()
    for so'z in so'zlar[1:]:
        natija += so'z.capitalize()
    return natija

print(camel_case("hello world python"))  # helloWorldPython
