# Copyright 2020, Brigham Young University-Idaho. All rights reserved.

"""This module contains two classes, IntEntry and FloatEntry, that allow
a user to enter an integer or a floating-point number into a tkinter
Entry widget.
"""
import tkinter as tk
from tkinter import Entry
from numbers import Number
from sys import float_info
from tkinter import Frame, Label, Button
from number_entry import IntEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Area of a Rectangle")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Age:"
    lbl_age = Label(frm_main, text="Width: ")

    # Create an integer entry box where the user will enter her age.
    ent_age = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=90)
    
    # Create a label that displays "Age:"
    lbl_age = Label(frm_main, text="Height: ")

    # Create an integer entry box where the user will enter her age.
    ent_age = IntEntry(frm_main, width=4, lower_bound=0, upper_bound=90)

    # Create a label that displays "years"
    lbl_age_units = Label(frm_main, text="years")

    # Create a label that displays "Rates:"
    lbl_rates = Label(frm_main, text="Rates:")

    # Create labels that will display the results.
    lbl_slow = Label(frm_main, width=3)
    lbl_fast = Label(frm_main, width=3)
    lbl_rate_units = Label(frm_main, text="beats/minute")

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear")

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_age.grid(      row=0, column=0, padx=3, pady=3)
    ent_age.grid(      row=0, column=1, padx=3, pady=3)
    lbl_age_units.grid(row=0, column=2, padx=0, pady=3)

    lbl_rates.grid(     row=1, column=0, padx=(30,3), pady=3)
    lbl_slow.grid(      row=1, column=1, padx=3, pady=3)
    lbl_fast.grid(      row=1, column=2, padx=3, pady=3)
    lbl_rate_units.grid(row=1, column=3, padx=0, pady=3)

    btn_clear.grid(row=2, column=0, padx=3, pady=3, columnspan=4, sticky="w")


    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            # Get the user's age.
            age = ent_age.get()

            # Compute the user's maximum heart rate.
            max_rate = 220 - age

            # Compute the user's slowest and
            # fastest beneficial heart rates.
            slow = max_rate * 0.65
            fast = max_rate * 0.85

            # Display the slowest and fastest benficial
            # heart rates for the user to see.
            lbl_slow.config(text=f"{slow:.0f}")
            lbl_fast.config(text=f"{fast:.0f}")

        except ValueError:
            # When the user deletes all the digits in the age
            # entry box, clear the slowest and fastest labels.
            lbl_slow.config(text="")
            lbl_fast.config(text="")


    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_age.clear()
        lbl_slow.config(text="")
        lbl_fast.config(text="")
        ent_age.focus()

    # Bind the calculate function to the age entry box so
    # that the computer will call the calculate function
    # when the user changes the text in the entry box.
    ent_age.bind("<KeyRelease>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button.
    btn_clear.config(command=clear)

    # Give the keyboard focus to the age entry box.
    ent_age.focus()


# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()


class _NumberEntry(Entry):
    _ERROR_STYLE = {"bg":"pink", "fg":"black"}


    def __init__(self, parent, datatype, dataname,
            lower_bound, upper_bound, default, kwargs):
        super().__init__(parent)

        assert type(self) != _NumberEntry, \
            "can't create a _NumberEntry object; " \
            "only children classes of _NumberEntry can be instantiated"
        assert isinstance(lower_bound, datatype), \
            f"lower_bound must be " + dataname
        assert isinstance(upper_bound, datatype), \
            f"upper_bound must be " + dataname
        assert lower_bound < upper_bound, \
            "lower_bound must be less than upper_bound"

        self.__datatype = datatype
        self.__dataname = dataname
        self.__lower_bound = lower_bound
        self.__upper_bound = upper_bound

        if default is not None:
            assert isinstance(default, datatype), \
                f"default must be " + dataname
            assert self._in_bounds(default), \
                "default must be between lower_bound and upper_bound"
            self.delete(0, tk.END)
            self.insert(0, str(default))

        self.__set_tk_args(kwargs)
        self.bind("<FocusIn>", _NumberEntry.__select_all)


    def __set_tk_args(self, kwargs):
        """Set the arguments that are used by tkinter."""
        if "justify" not in kwargs:
            kwargs["justify"] = "right"
        if "width" not in kwargs:
            kwargs["width"] = \
                max(len(str(self.__lower_bound)), len(str(self.__upper_bound)))
        kwargs["validate"] = "focusin"
        kwargs["validatecommand"] = \
                (self.register(self.__validate_all), "%V", "%s", "%P")
        self.config(**kwargs)
        self._original_style = {"bg":self["bg"], "fg":self["fg"]}


    # Each time a _NumberEntry gets the keyboard focus,
    # select all the text in that entry.
    @staticmethod
    def __select_all(event):
        """Select all the characters in the entry."""
        entry = event.widget
        entry.select_range(0, tk.END)
        entry.icursor(tk.END)


    @staticmethod
    def _contains_space(text):
        has_space = False
        for ch in text:
            has_space = ch.isspace()
            if has_space:
                break
        return has_space


    def __validate_all(self, reason, current_text, text_if_allowed):
        valid = False
        if reason == "key":
            valid = self._validate_key(current_text, text_if_allowed)
        elif reason == "focusin":
            valid = self.__focus_in(current_text)
        elif reason == "focusout":
            valid = self.__focus_out(current_text)
        return valid


    def __focus_in(self, current_text):
        self.config({"validate": "all"})
        return self.__validate_focus(current_text)

    def __focus_out(self, current_text):
        self.config({"validate": "focusin"})
        return self.__validate_focus(current_text)

    def __validate_focus(self, current_text):
        valid = False
        try:
            n = self._convert(current_text)
            valid = self._in_bounds(n)
        except ValueError:
            pass
        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return valid


    def _in_bounds(self, n):
        return self.__lower_bound <= n <= self.__upper_bound


    def set(self, n):
        """Display a number for the user to see."""
        assert isinstance(n, self.__datatype), \
            "n must be " + self.__dataname
        assert self._in_bounds(n), \
            f"n must be between {self.__lower_bound} and {self.__upper_bound}"
        self.delete(0, tk.END)
        self.insert(0, str(n))


    def get(self):
        """Return the number that the user entered."""
        n = self._convert(super().get())
        if not self._in_bounds(n):
            raise ValueError("number must be between"
                f" {self.__lower_bound} and {self.__upper_bound}")
        return n


    def clear(self):
        self.config({"validate": "focusin"})
        self.config(self._original_style)
        self.delete(0, tk.END)


class IntEntry(_NumberEntry):
    """An Entry widget that accepts only integers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *, lower_bound=-2**63,
            upper_bound=2**63 - 1, default=None, **kwargs):
        super().__init__(parent, int, "an integer",
                lower_bound, upper_bound, default, kwargs)

        self.__lower_entry = lower_bound if lower_bound <= 1 else 1
        self.__upper_entry = upper_bound if upper_bound >= -1 else -1
        self.__allow_negative = (lower_bound < 0)


    def _validate_key(self, current_text, text_if_allowed):
        allowed = valid = False
        try:
            if not _NumberEntry._contains_space(text_if_allowed):
                n = int(text_if_allowed)
                allowed = self.__lower_entry <= n <= self.__upper_entry
                # If text_if_allowed is allowed, we must allow it, and
                # we must check only text_if_allowed for validity.
                if allowed:
                    valid = self._in_bounds(n)
        except ValueError:
            allowed = (len(text_if_allowed) == 0 or
                    (self.__allow_negative and text_if_allowed == "-"))

        # If text_if_allowed is not allowed, we must not allow
        # it, and we must check only current_text for validity.
        if not allowed:
            try:
                n = int(current_text)
                valid = self._in_bounds(n)
            except ValueError:
                pass

        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return allowed


    @staticmethod
    def _convert(text): return int(text)


class FloatEntry(_NumberEntry):
    """An Entry widget that accepts only numbers between
    an optional lower bound and an optional upper bound.
    """
    def __init__(self, parent, *, lower_bound=-float_info.max,
            upper_bound=float_info.max, default=None, **kwargs):
        super().__init__(parent, Number, "a number",
                lower_bound, upper_bound, default, kwargs)

        if lower_bound < 0:    # [-, 0)
            self.__lower_entry = lower_bound
        elif lower_bound < 1:  # [0, 1)
            self.__lower_entry = 0
        else:                  # [1, +]
            self.__lower_entry = 1

        if upper_bound <= -1:   # [-, -1]
            self.__upper_entry = -1
        elif upper_bound <= 0:  # (-1, 0]
            self.__upper_entry = 0
        else:                   # (0, +]
            self.__upper_entry = upper_bound

        self.__allow_negative = (lower_bound < 0)
        self.__allow_leading_dot = (
                (-1 < lower_bound < 1) or
                (-1 < upper_bound < 1) or
                (lower_bound <= -1 and 1 <= upper_bound))


    def _validate_key(self, current_text, text_if_allowed):
        allowed = valid = False
        try:
            if not _NumberEntry._contains_space(text_if_allowed):
                n = float(text_if_allowed)
                allowed = self.__lower_entry <= n <= self.__upper_entry
                # If text_if_allowed is allowed, we must allow it, and
                # we must check only text_if_allowed for validity.
                if allowed:
                    valid = self._in_bounds(n)
        except ValueError:
            allowed = (len(text_if_allowed) == 0 or
                    (self.__allow_negative and text_if_allowed == "-") or
                    (self.__allow_leading_dot and text_if_allowed == ".") or
                    (self.__allow_negative and self.__allow_leading_dot
                        and text_if_allowed == "-."))

        # If text_if_allowed is not allowed, we must not allow
        # it, and we must check only current_text for validity.
        if not allowed:
            try:
                n = float(current_text)
                valid = self._in_bounds(n)
            except ValueError:
                pass

        style = self._original_style if valid else _NumberEntry._ERROR_STYLE
        self.config(style)
        return allowed


    @staticmethod
    def _convert(text): return float(text)
