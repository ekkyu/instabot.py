class FilterExample:
    
    def __init__(self, filter_key):
        self.filter_key = filter_key

    def username_filter(self, username):
        if not self.filter_key:
            return False
