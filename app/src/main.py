class Main(object):
    def say_hello(self, name:str):
        return f"Hello World, {name}!"

if __name__ == '__main__':
    main = Main()
    print(main.say_hello("Fulano"))