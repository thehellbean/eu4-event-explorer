import event_parser
import lexer

def recurse_structure(parameters: event_parser.Parameter):
    with open("outfile.xml", "a") as ofile:
        if type(parameters.values) == str:
            ofile.write("<parameter name='{0}'>{1}</parameter>\n".format(parameters.name, parameters.values))
            return
        ofile.write("<parameter name='{0}'>\n".format(parameters.name))
        ofile.flush()
        for sub_parameter in parameters.values:
            recurse_structure(sub_parameter)
        ofile.write("</parameter>\n".format(parameters.name))


if __name__ == "__main__":
    lex = lexer.Lexer("Buddhism.txt")

    parser = event_parser.Parser()
    parser.event_file(lex)

    with open("outfile.xml", "w") as ofile:
        ofile.write("<root>\n")

    for event in parser.events:
        recurse_structure(event)

    #recurse_structure(parser.events[0])

    with open("outfile.xml", "a") as ofile:
        ofile.write("</root>")