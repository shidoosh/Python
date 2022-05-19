#! python3

import webbrowser

# web pages I have open when doing ATBS course
sites = ['https://automatetheboringstuff.com/',
        'https://www.udemy.com/course/automate/learn/lecture/',
        'https://onedrive.live.com/edit.aspx?resid=95C3A6897EC8D8E2!2062&cid=95c3a6897ec8d8e2&wdorigin=ondc'
        ]


for i in range(len(sites)):
    webbrowser.open(sites[i])
