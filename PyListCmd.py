import sys

class command(object):
    def __init__(self,
                 command_name,
                 command_args_num:int) -> None:
        if command_name=='' or type(command_name)!=str:
            raise SyntaxError('invalid command name')
        command_name='-'+command_name
        self.command_name=command_name
        self.command_args=command_args_num
        self.argv = sys.argv
    def command_exist(self):
        a=0
        
        for i in self.argv :
            if i == self.command_name:
                self.exist=(True,a)
                return True,a
            a+=1
        self.exist=(False,-1)
        return False,-1
    def delete_command(self):
        del self.command_name,self.command_args
    def run_command(self,func):
        if self.command_exist()[0]:
            FROM=self.exist[1]+1
            TO=self.exist[1]+self.command_args+1
            try:
                args=tuple(self.argv[FROM:TO])
            except IndexError as err:
                print('an error was found:')
                print(err)
                print('end of error output') 
                args=()
            try:
                func(args)
            except TypeError:
                raise SyntaxError('invalid function or args')

    def set_argv(self,l):
        self.argv = l
