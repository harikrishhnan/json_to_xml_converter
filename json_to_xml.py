#import the reqired modules
import json #module use to work with json
import xmltodict #module used to work with xml

#function for handling the json object and append to the result list
def json_to_xml(json_obj, line_padding=""):
    result = list()
    json_obj_type = type(json_obj)
    if(json_obj_type=="str"):
        sub_elem=str(sub_elem)
        if(type(sub_elem=="str")):
            sub_elem=="string"
    elif(json_obj_type=="array"):
        sub_elem=bool(sub_elem)
        if(type(sub_elem=="bool")):
             sub_elem=="bool"   
#checking whether json_obj_type is a list
    if json_obj_type is list:
        for sub_elem in json_obj:
            result.append(json_to_xml("<array>", line_padding))
            result.append(json_to_xml(sub_elem, line_padding))
            result.append(json_to_xml("</array>", line_padding))
        return "\n".join(result)
#checking whether json_obj_type is a dictionary
    if json_obj_type is dict:
        for tag_name in json_obj:
            sub_obj = json_obj[tag_name]
            result.append("<object>")
            result.append("%s<%s>" % (line_padding, tag_name))
            result.append(json_to_xml(sub_obj, "\t" + line_padding))
            result.append("%s</%s>" % (line_padding, tag_name))
            result.append("</object>")
        return "\n".join(result)
    return "%s%s" % (line_padding, json_obj)
    

#function which reads the json file and writes the xml file 
def display(json_file, xml_file):
    with open(json_file, 'r') as f:
        json_content = json.load(f)

    xml_content = json_to_xml(json_content)

    with open(xml_file, 'w') as f:
        f.write(xml_content)
#getting the user input
json_file =input("Enter the json filename:")
xml_file = 'data.xml'
display(json_file,xml_file)
