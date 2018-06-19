import os
import xml.etree.ElementTree as ET
import pandas as pd


file_list=os.listdir()
meta_set=set(["docid", "title", "author", "created", "topic", "tagging"])
df=pd.DataFrame(columns=["doc_id", "title", "author", "created", "topic", "tagging"])

for filename in file_list:
    d_dict={}
    if filename[0]=='_':
        with open(filename,"r", encoding="windows-1251") as file:
            root=ET.fromstring(file.read())
            title=root.find("head").find("title").text
            d_dict["title"]=[title]
            for meta in root.find("head").findall("meta"):
                name=meta.get("name")
                content=meta.get("content")
                if name in meta_set:
                    if (name!="docid"):
                        d_dict[name]=[content]
                    else:
                        d_dict["doc_id"]=[content]
    file_df=pd.DataFrame.from_dict(d_dict)
    df=pd.concat([df,file_df])
df=df[["doc_id","title","author","created","topic","tagging"]]
df.to_csv("test3.csv")

