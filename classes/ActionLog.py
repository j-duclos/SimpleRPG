class ActionLog:
    def __init__(self):
        self.action_list = []

    def update_action_log(self, *args):
        for a in args:
            print(a)
            self.action_list.append(a)

    def write_action_log_to_file(self):
        with open("game_logs.txt", "w") as f:
            for a in self.action_list:
                f.write(a+"\n")
