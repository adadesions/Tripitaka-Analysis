import re
import requests
import wget


def get_source(url, dst_file):
    res = requests.get(url)
    dst_file += ".html"
    with open(dst_file, 'w') as file:
        file.write(res.content.decode(encoding='cp874', errors="ignore"))


def get_links(source_file, dst_file, prefix=""):
    source_file += ".html"
    dst_file += ".txt"
    with open(source_file, 'r') as file:
        for cnt, line in enumerate(file):
            txt = re.search(r"href=\"", line)
            if txt:
                (x, y) = txt.span()
                info = txt.string
                start_index = x+6
                end_index = info.find('zip')+3
                link = info[start_index:end_index]
                if len(link) > 10:
                    full_link = ''.join([prefix, link])
                    print(full_link)
                    with open(dst_file, 'a') as file:
                        file.write(full_link)
                        file.write('\n')
        print("Done Get Link")


def download_files(filename, destination):
    filename += ".txt"
    with open(filename, 'r') as file:
        for cnt, line in enumerate(file):
            mod_line = line.replace("\n", "")
            wget.download(mod_line, destination)

def main():
    source_file = "source_thai"
    get_source("http://www.learntripitaka.com/Tripitaka-Thai2.html", source_file)
    get_links(source_file=source_file, dst_file=source_file, prefix="http://www.learntripitaka.com/")
    download_files(source_file, "data/tripitaka-thai")


if __name__ == "__main__":
    main()