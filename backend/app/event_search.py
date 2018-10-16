from app import db_list


def convert_root_to_dict(root):
    event_dict = dict()

    for child in root.getchildren():
        if len(child.text.strip()) > 0:
            value = child.text
        else:
            value = convert_root_to_dict(child)
        if child.get("name") in event_dict:
            if type(event_dict[child.get("name")]) == list:
                event_dict[child.get("name")].append(value)
            else:
                temp = event_dict.get(child.get("name"))
                event_dict[child.get("name")] = [temp, value]
        else:
            event_dict[child.get("name")] = value
    return event_dict


def key_value_recursion(key, value):
    if type(value) == dict:
        base = "[.//parameter[@name='{0}']".format(key)
        for recursion_key, recursion_value in value.items():
            base += "//parameter"
            if type(recursion_value) == dict:
                base += key_value_recursion(recursion_key, recursion_value)
            else:
                if type(recursion_value) == int:
                    base += "[@name='{0}' and {1}={2}]]".format(recursion_key, "number()", recursion_value)
                else:
                    base += "[@name='{0}' and {1}={2}]]".format(recursion_key, "text()", "'" + recursion_value + "'")
        return base
    else:
        base = "[.//parameter[@name='{0}' and {1}={2}]]"
        if type(value) == int:
            return base.format(key, 'number()', value)
        else:
            return base.format(key, 'text()', "'" + value + "'")


def convert_search_terms_to_xquery(json_search):
    base = "//root/parameter"

    for key, value in json_search.items():
        base += key_value_recursion(key, value)

    return base


def search_by_xquery(xquery):
    results = []
    for db in db_list:
        results = results + db.xpath(xquery)
    return results
