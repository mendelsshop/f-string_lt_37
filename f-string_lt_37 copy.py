#combine var_handle and f to make a function that can handle all the var stuff
# fix spagghetti code in f class 


# make multi level if elses
# if found_ariable
# if past_semicolon
# etc


class f(str):
    def __init__(self, string) -> None:
        self.string = string
        self.version = '0.0.1-alpha'
    def phase_change(self, phase) -> None:
        self.current_phase = phase
        # print('changing to ' + phase)
        return None
    def var_handle(self,var) -> str:
        # need to work on gloabal and local variables handling
        # print('var: ' + var)
        try:
            exec('global var')
            var = eval(var)

        except SyntaxError:
            print('error: variable')
            pass
 
        return var
    def f_string_parse(self) -> str:
        self.current_phase = 'parsing'
        # print('parsing', current_phase)
        self.i = 0
        self.output = ''
        self.var_handling = True
        self.var = ''
        self.dummy_var = ''


        def info():
            # print('================================================================')
            # print('| f string parser version: ' + self.version,'|')
            # print('| current phase: ' + self.current_phase)
            # print('| current substring: ' + self.string[self.i], '|')
            # print('| var: ' + self.var, '|')
            # print('| output: ' + self.output)
            # print('| var handling: ' + str(self.var_handling), '|')
            # print('| dummy_var', self.dummy_var, '|')
            # print('================================================================')
            # print()
            return None
        

        while len(self.string) > self.i:
            print(len(self.output))
            print(self.output)
            # for self.i in range(len(self.string)):       
            if self.current_phase == 'parsing':
                if self.string[self.i] == '{':
                    self.phase_change('f_string')
                    self.i += 1
                    info()
                    # print('changing to f_string parsing')
                      
                else:
                    self.output += self.string[self.i]
                    # print(self.output)
                    self.i += 1
                    info()
                    # print('adding to output')
                   
            elif self.current_phase == 'f_string':
                if self.string[self.i] in  ['\"','\''] and self.var_handling == True: 
                    self.var_handling = False
                    self.var += self.string[self.i]
                    self.i += 1
                    info()
                    # print('adding to var without var handling')
                   
                elif self.string[self.i] in ['\'','\"'] and self.var_handling == False:
                    self.var_handling = True
                    self.i += 1
                    info()
                    # print('stop adding to var with var handling')
                   
                elif self.string[self.i] == '}' and self.var_handling == True:
                    self.phase_change('parsing')
                    if self.var[0] in ['\'','\"']:
                        self.var = self.var.strip('\"\'')
                        # print(self.var)
                    else:
                        self.var = self.var_handle(self.var)
                    if len(self.string) > self.i:
                        self.i += 1
                        self.output += self.var
                        self.var = ''
                        # print(self.output)

                    else:
                        self.output += self.var
                        self.var = ''
                        self.i += 1
                    # print('adding var to output')
                    
                   
                elif self.string[self.i] == ':' and self.var_handling == True:
                    self.phase_change('after f_string')
                    self.i += 1
                    info()
                    # print('changing to after f_string parsing')
                   
                else:
                    self.var += self.string[self.i]
                    # print('adding to var', self.string[self.i])
                    self.i += 1  
                    info()
                    # print('adding to var with var handling')

            elif self.current_phase == 'after f_string':
                if self.string[self.i] == '}':
                    self.phase_change('f_string')
                


                    info()
                    # print('changing to f_string parsing')
                else:
                    if self.string[self.i] in ['<','>']:
                        pass
                    self.dummy_var += self.string[self.i]
                    self.i += 1

                    info()
                    # print('handling padding')
        return self.output
        


    def __repr__(self) -> str:
        return '\'' + self.f_string_parse() + '\''
    def __str__(self) -> str:
        return self.f_string_parse()

def main() -> None:
    global hello, world
    hello = "Hello,"
    world = "wo" 
    # string = '{hello} {world:<8}hiyyy'
    # string1 = f'{hello} {world:<13}hiyyy'


    string = f('{hello} {world}hiyyy')
    string1 = f'{hello} {world}hiyyy'

    
    
    print(string)
    print(len(string))
    print('=================')
    print(len(string1))
    print(string1)
    # need to fix type
    # print(type(string)) 
    # print(type(f'{"hello"}'))


if __name__ == '__main__':
    main()
