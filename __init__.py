from mycroft import MycroftSkill, intent_file_handler


class TankEndo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('endo.tank.intent')
    def handle_endo_tank(self, message):
        self.speak_dialog('endo.tank')


def create_skill():
    return TankEndo()

