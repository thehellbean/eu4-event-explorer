import event_parser
import lexer
import re
import os


"""def find_parameter_string(parameters, name_to_find):
    for parameter in parameters:
        if parameter.name == name_to_find:
            return parameter.values

    for parameter in parameters:
        return find_parameter_string(parameter.values, name_to_find)"""


def find_localisation(localisation_id, name_to_find):
    """if type(localisation_id) != str:
        parameter_string = find_parameter_string(localisation_id, name_to_find)
        return find_localisation(parameter_string, name_to_find)"""

    if localisation_id[0] == localisation_id[-1] == '"':
        localisation_id = localisation_id[1:-1]

    prefix = re.search("([A-Za-z_\d]+)[.:]", localisation_id)
    if prefix:
        prefix = prefix.group(1)
    else:
        prefix = localisation_id
    with open("localisation_index.index", "r") as index_file:
        for index_line in index_file:
            split_line = index_line.split("~")

            if split_line[0] == prefix:
                localisation_filename = split_line[1]
                with open("localisation/"+localisation_filename.strip(), "r") as localisation_file:
                    for line in localisation_file:
                        id_location = line.find(localisation_id)
                        if id_location != -1:
                            return line[id_location+len(localisation_id) + 2:]


def recurse_structure(parameters: event_parser.Parameter, filename):
    with open(filename, "a") as ofile:
        if parameters.name == 'title' and type(parameters.values) == str:
            title = find_localisation(parameters.values, "title")
            ofile.write("<parameter name='english_title'>{0}</parameter>\n".format(title.strip()))
        elif parameters.name == "desc" and type(parameters.values) == str:
            description = find_localisation(parameters.values, "desc")
            ofile.write("<parameter name='english_desc'>{0}</parameter>\n".format(description.strip()))
        elif parameters.name == "name" and type(parameters.values) == str:
            name = find_localisation(parameters.values, "name")
            if name:
                ofile.write("<parameter name='english_name'>{0}</parameter>\n".format(name.strip()))

        if type(parameters.values) == str:
            ofile.write("<parameter name='{0}'>{1}</parameter>\n".format(parameters.name, parameters.values))
            return

        ofile.write("<parameter name='{0}'>\n".format(parameters.name))
        ofile.flush()
        for sub_parameter in parameters.values:
            recurse_structure(sub_parameter, filename)
        ofile.write("</parameter>\n".format(parameters.name))


if __name__ == "__main__":
    for filename in os.listdir("events"):
        outfile_name = "parsed_events/" + filename.replace("txt", "xml")
        if os.path.isfile(outfile_name):
            continue
        print("Parsing from", filename)
        lex = lexer.Lexer("events/"+filename)

        parser = event_parser.Parser()
        parser.event_file(lex)

        with open(outfile_name, "w") as ofile:
            ofile.write("<root>\n")

        for event in parser.events:
            recurse_structure(event, outfile_name)

        with open(outfile_name, "a") as ofile:
            ofile.write("</root>")