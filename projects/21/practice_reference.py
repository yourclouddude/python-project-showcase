from urllib.parse import urlparse
def validate_profile(data):
    for key in ('name','headline','about'):
        if not isinstance(data.get(key),str) or not data[key].strip():
            raise ValueError('Missing '+key)
    if not isinstance(data.get('projects'),list):
        raise ValueError('Projects list required.')
    for project in data['projects']:
        if not isinstance(project,dict) or not all(isinstance(project.get(k),str) and project[k].strip() for k in ('title','description','url')):
            raise ValueError('Incomplete project.')
        link=urlparse(project['url'])
        if link.scheme!='https' or not link.netloc:
            raise ValueError('HTTPS link required.')
    return data
