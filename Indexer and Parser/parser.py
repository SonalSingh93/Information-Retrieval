
from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
import ssl
import re
import string
import os

global set_lower
global punc

# function to remove punctuations from strings and preserve in digits
def remove_punctuation(list_strings):
    # regular expression to remove punctuations from string but preserve it in digits
    pattern = re.compile(r'((?<!\d)([!%\"#$&\'()*+,.:;<=>\/?@[\]^_`{|}~]+))|([,!@:()\\;.])(?![0-9])|([^\x00-\x7F]+)')

    #modifies the title
    title_temp = list_strings[0]
    title_temp = re.sub(pattern, " " , title_temp)
    title_temp = re.sub(r'-' ,"" , title_temp)
    final_text = [title_temp.lower()]
    # removes punctuation from the entire text
    for i in range(1,len(list_strings)):
        text = list_strings[i]
        text = re.sub(pattern, "" , text)
        final_text.append(text)
    return final_text

# source folder path => parses the file and stores it in the destination folder
def parse_files(folderpath, dest_folder_path, set_lower , punc):
    text = []
    source_folder_path = folderpath

    #for every file in the given directory, do the parsing
    for file in os.listdir(source_folder_path):
        # if the file isn't DS store (added by mac os by default)
        if (file != ".DS_Store"):
            file_path = source_folder_path + "/"+ file
            fhand = open(file_path, "r+")
            content = fhand.read()

            # parses the title and stores it appropriately
            pattern = re.compile(r'((?<!\d)([!%\"#$&\'()*+,.:;<=>\/?@[\]^_`{|}~]+))|([,!@:()\\;.])(?![0-9])|([^\x00-\x7F]+)')
            title = BeautifulSoup(content, "html.parser" , parse_only = SoupStrainer("title"))
            print ("This is the title\n" ,re.sub(pattern, "" , title.get_text()),"\n")

            text.append(title.get_text())
            # get all the <p> tags from the htm content from the file
            soup = BeautifulSoup(content,"html.parser", parse_only=SoupStrainer("p"))
            fhand.close()

            # modify the parsed file name by adding the path to it
            parsed_file_path = dest_folder_path + "/" + file

            # remove span tag from the soup
            # taken from a solution on stack overflow

            for span_tag in soup.findAll('span'):
                span_tag.replace_with('')

            #remove sup tags from the soup
            for sup_tag in soup.findAll('sup'):
                sup_tag.replace_with('')

            #get the text from the soup
            content = soup.get_text()

            # if set_lower is set, convert it to lower case
            if set_lower == True:
                content = content.lower()
            text.append(content)

            # if punc is set, remove punctuations from the text
            if punc == True:
                text = remove_punctuation(text)
            print(text)

            # write to the destination file
            fhand = open (parsed_file_path,"w")
            for t in text:
                fhand.write(str(t)+ " ")
            text.clear()

            file_names_final = "list_of_final_files.txt"

def main():
    # lower case and remove punctuations set to true by default
    lower_case = True
    remove_punc = True
    source_folder = input("Enter the path of the corpus folder \n")
    destination_folder = input("Enter the path of the destination folder i.e where to store the parsed docs\n")
    lower_case = input("Enter 'True' if you want to change to lowercase\n")

    if(lower_case.lower() != "true"):
        lower_case = False
    else:
        lower_case = True
    remove_punc = input("Enter 'True' if you want to remove punctuation\n")
    if(remove_punc.lower() == "true"):
        remove_punc = True
    else:
        remove_punc = False

    # calls the function to parse files
    parse_files(source_folder,destination_folder, lower_case , remove_punc)

main()
