print('This is a website checker')
url = input('\nEnter the URL here: ')

if url.startswith('https'):
    print('This website is secure')
elif url.startswith('http'):
    print('This website is not secure')
else:
    print('This does not look like a complete URL.')