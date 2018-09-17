def convert_root_to_json(root):
    event_dict = dict()

    critical_parts = ["id", "desc", "title", "english_title", "english_desc"]

    for part in critical_parts:
        possibilities = root.xpath("./parameter[@name='{0}']".format(part))
        for node in possibilities:
            event_dict[part] = node.text
    return str(event_dict)