import json

class Log:
    def __init__(self, fleet):
        self.history = []
        self.fleet = fleet

    def get_log(self, to_string = True):
    	log = {"fleet" : self.fleet, "history" : self.history }
    	return [log, json.dumps(log)][to_string]