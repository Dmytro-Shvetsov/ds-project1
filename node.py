import cmd

class Main(cmd.Cmd):
    prompt = '> '

    def do_Start_game(self, args):
        """Greet the user."""
        print("Game started")

    def do_Set_symbol(self, args):
        print("Symbol set")

    def do_List_board(self, args):
        print("Board listed")

    def do_Set_node_time(self, args):
        print("Node time set")

    def do_Set_time_out(self, args):
        print("Timeout set")

if __name__ == '__main__':
    cli = Main()
    cli.cmdloop()