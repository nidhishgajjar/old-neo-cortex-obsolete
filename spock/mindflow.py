class MindFlow:
    def __init__(self, user_input, livelymind, lazymind):
        self.livelymind = livelymind
        self.lazymind = lazymind
        self.user_input = user_input

    def system1(self):
        return self.livelymind.run()
    
    def system2(self):
        response = self.livelymind.introspection()
        if response != {} and self.job_manager.add_job(self.user_input):
            return self.lazymind.run()
        else:
            return self.livelymind.run()