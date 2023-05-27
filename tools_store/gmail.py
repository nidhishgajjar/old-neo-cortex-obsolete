class Gmail:
    def __init__(self):
        self.action = None
        self.info_required = None

    def __getattr__(self, name):
        if name in ["create_email", "read_email", "send_email", "find_email", "filter_email", "delete_email"]:
            self.action = name
            return self
        elif self.action and not self.info_required:
            self.info_required = name
            return self
        else:
            raise AttributeError(f"{self.__class__.__name__} object has no attribute '{name}'")

    def execute(self):
        if self.action == "create_email":
            if self.info_required:
                print(f"Creating email with info: {self.info_required}")
            else:
                print("Creating email")
        elif self.action == "read_email":
            if self.info_required:
                print(f"Reading email with info: {self.info_required}")
            else:
                print("Reading email")
        elif self.action == "send_email":
            if self.info_required:
                print(f"Sending email with info: {self.info_required}")
            else:
                print("Sending email")
        elif self.action == "find_email":
            if self.info_required:
                print(f"Finding email with info: {self.info_required}")
            else:
                print("Finding email")
        elif self.action == "filter_email":
            if self.info_required:
                print(f"Filtering email with info: {self.info_required}")
            else:
                print("Filtering email")
        elif self.action == "delete_email":
            if self.info_required:
                print(f"Deleting email with info: {self.info_required}")
            else:
                print("Deleting email")
        else:
            raise ValueError("Invalid action or information")