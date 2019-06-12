import click
from tkinter import *
import re
from os import path


class sizes:
    lblWidth = 10
    fldWidth = 20


class Templater:
    def __init__(self, input_str, output, path=False):
        self.input = input_str
        self.path_to_write = output
        self.cur_row = 0
        self.fields = {}
        self.text_in = ""
        self.test_out = "No text yet"
        self.window = Tk()
        self.mode_input_is_path = path
        lbl = Label(self.window, text="Output name")
        lbl.grid(column=0, row=self.cur_row)
        self.file_name_fld = Entry(self.window, width=sizes.fldWidth)
        self.file_name_fld.grid(column=1, row=self.cur_row)
        self.cur_row += 1
        self.__load_input()
        self.__ui()

    def __ui_add_var_field(self, field_dict: dict, var_name):
        lbl = Label(self.window, text=var_name)
        lbl.grid(column=0, row=self.cur_row)
        txt = Entry(self.window, width=sizes.fldWidth)
        txt.grid(column=1, row=self.cur_row)
        field_dict.update({var_name: txt})
        self.cur_row += 1

    def __ui(self):
        match = re.findall(r'\$\{[^\}]+\}', self.text_in)

        if len(match):
            for m in match:
                self.__ui_add_var_field(self.fields, m)
        self.window.title("Create a template")
        btn = Button(self.window, text="Done!", command=self.__on_click)
        self.window.geometry('100x' + str((self.cur_row + 1) * 23))
        btn.grid(column=1, row=self.cur_row)
        self.window.mainloop()

    def __load_input(self):
        if self.mode_input_is_path:
            if not path.exists(self.input):
                print("There is no input file")
                return
            with open(self.input) as f:
                self.text_in = f.read()
        else:
            self.text_in = self.input

    def __get_output_text(self):
        text_out = self.text_in  # type: str
        variables = self.get_variables()
        for var, val in variables.items():
            text_out = text_out.replace(var, val)
        self.test_out = text_out

    def __on_click(self):
        self.window.title("Clicked!")
        self.__get_output_text()
        print(self.get_variables())
        print(self.test_out)
        if self.path_to_write is not None:
            self.write()
        self.window.destroy()

    def get_variables(self):
        variables = {}
        for var, field in self.fields.items():
            variables.update({var: field.get()})
        return variables

    def write(self):
        path2w = path.join(path.abspath(self.path_to_write), self.file_name_fld.get())
        if path.isfile(path2w):
            f = open(path2w, "w+")
        else:
            f = open(path2w, "x")
        f.write(self.test_out)


@click.command()
@click.option("--input_str", "-i",
              prompt='Input text or path',
              type=str,
              default=None,
              required=True,
              help='Input text or path')
@click.option("--path/--text", "-p/-t",
              # prompt=None,
              # type=str,
              default=False,
              help='Text or path')
@click.option("--output", "-o",
              prompt=None,
              type=str,
              default=".\\",
              help='Output file path')
def main(input_str, output, path):
    a = Templater(input_str, output, path)


if __name__ == '__main__':
    # args = argparse.
    # text_in = "Hello, ${Name}\n" \
    #           "Today is ${Weather}"
    main()
