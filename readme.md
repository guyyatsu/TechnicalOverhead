# Technical Overhead
_Tehcnical Overhead_ refers to the ever-growing collection of boiler-plate code I've become accustomed to in my work as a developer.
The library contains tool objects built using only python builtin modules and provides a layer of abstraction over the effort involved
in adhering to my own standards.


## RuntimeSetup
_RuntimeSetup_ packages logging and argument parsing with a couple of handy functions for cleaning up logging statements and adding
arguments to your script.


### Arguments
The Arguments class acts as a __*first class function*__ that accepts only a nested dictionary (ArgumentDict) indexed by number in
no particular order containing values for long and short POSIX-Style flag operators, help text, input type (as a valid Python type,)
and an argparse compatible action text.

Given arguments are accessed after initialization by calling Arguments.args.


### Log
The Log class initializes python logging and allows custom parameters but defaults to logging.INFO level statements and outputs
to a hidden file named 'log' in the current working directory if no parameters are passed.

Log also includes a wrapper for calling various level statements by their name; ie log.INFO(msg) will print f"msg" as an INFO level
statement, and so on and so forth.
