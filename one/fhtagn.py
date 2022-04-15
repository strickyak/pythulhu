# GPL2.  Share your improvements!  --strick

class Boolean(object):
    def __init__(self, value):
        self.value = value
        self.count = 0

    def __len__(self):
        self.count += 1
        if self.count > 255:
            return 1 if (not self.value) else 0
        else:
            return 1 if (self.value) else 0
