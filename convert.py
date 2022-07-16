class convert:
    class json:
        def __init__(self, variable:dict):
            self.value = variable
        
        def to_tuple(self):
            variable_list = []
            value_list = []
            for i in self.value:
                variable_list.append(i)
                value_list.append(self.value[i])
            return (tuple(variable_list), tuple(value_list))